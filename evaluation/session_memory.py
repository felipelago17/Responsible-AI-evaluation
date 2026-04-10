"""MemPalace-style longitudinal evaluation memory.

Provides stateful, cross-run evaluation memory using a wing/room/hall
spatial hierarchy.  After each benchmark run, results are persisted so that
subsequent runs can retrieve prior context for longitudinal model tracking,
capability-drift analysis, and risk-escalation detection.

Storage hierarchy
-----------------
::

    MemPalace (root)
    └── Wing  (model family, e.g. "claude-3")
        └── Room  (benchmark, e.g. "cybergym_glasswing")
            └── Hall  (run ID / timestamp)
                └── entry (serialised BenchmarkRunResult or free-form dict)

The hierarchy is encoded as a nested directory / file structure under a
configurable ``base_dir``.  By default, results are written to
``results/mempalace/`` relative to the repository root.

Knowledge-graph hooks
---------------------
Optional graph hooks support temporal queries such as capability drift and
risk escalation over time.  When the ``knowledge_graph`` extra is installed
(``pip install networkx``), :class:`MemPalaceStore` maintains an in-memory
directed graph of result nodes, enabling queries like:

- "all runs of model X on benchmark Y, ordered by time"
- "benchmark runs where dual_use_risk_score increased between consecutive runs"

Usage
-----
::

    from evaluation.session_memory import MemPalaceStore

    store = MemPalaceStore()

    # Persist a result after a benchmark run
    store.persist(
        wing="claude-3-opus",
        room="cybergym_glasswing",
        result=benchmark_run_result,
    )

    # Retrieve prior results for temporal context
    history = store.retrieve(wing="claude-3-opus", room="cybergym_glasswing")
    for entry in history:
        print(entry["metrics"]["dual_use_risk_score"])

References
----------
- Anthropic Responsible Scaling Policy (February 2026 revision)
- MemPalace longitudinal evaluation methodology
"""

from __future__ import annotations

import json
import pathlib
from datetime import datetime, timezone
from typing import Any

# Default storage path relative to this file's grandparent (repo root)
_DEFAULT_BASE_DIR = (
    pathlib.Path(__file__).resolve().parent.parent / "results" / "mempalace"
)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _hall_key(timestamp: str) -> str:
    """Sanitise an ISO-8601 timestamp for use as a directory name.

    Replaces characters that are unsafe on Windows/POSIX filesystems.
    """
    return timestamp.replace(":", "-").replace("+", "p")


def _now_iso() -> str:
    """Return the current UTC time as an ISO-8601 string."""
    return datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# MemPalaceStore
# ---------------------------------------------------------------------------


class MemPalaceStore:
    """Persistent cross-run evaluation memory store.

    Implements a wing/room/hall hierarchy on top of the local filesystem.
    Optionally maintains an in-memory knowledge graph (requires ``networkx``)
    for temporal queries.

    Args:
        base_dir: Root directory for the MemPalace store.  Defaults to
            ``results/mempalace/`` under the repository root.
        enable_knowledge_graph: If ``True`` and ``networkx`` is installed,
            construct an in-memory directed graph of result nodes to enable
            temporal queries.  Defaults to ``False``.
    """

    def __init__(
        self,
        base_dir: str | pathlib.Path | None = None,
        *,
        enable_knowledge_graph: bool = False,
    ) -> None:
        self._base = pathlib.Path(base_dir) if base_dir else _DEFAULT_BASE_DIR
        self._base.mkdir(parents=True, exist_ok=True)
        self._graph: Any = None
        if enable_knowledge_graph:
            self._graph = self._init_graph()

    # ------------------------------------------------------------------
    # Knowledge-graph initialisation
    # ------------------------------------------------------------------

    def _init_graph(self) -> Any:
        """Initialise a networkx DiGraph and populate from persisted data.

        Returns ``None`` (with a warning) if ``networkx`` is not installed.
        """
        try:
            import networkx as nx  # type: ignore[import]
        except ImportError:
            import warnings

            warnings.warn(
                "networkx is not installed; knowledge-graph hooks are disabled."
                " Install with: pip install networkx",
                stacklevel=3,
            )
            return None

        graph = nx.DiGraph()
        # Populate graph from any existing persisted entries
        for entry_path in sorted(self._base.rglob("*.json")):
            try:
                with entry_path.open() as fh:
                    data = json.load(fh)
                self._add_graph_node(graph, data, entry_path)
            except (json.JSONDecodeError, KeyError):
                continue
        return graph

    @staticmethod
    def _add_graph_node(
        graph: Any,
        data: dict[str, Any],
        entry_path: pathlib.Path,
    ) -> None:
        """Add a result node to the knowledge graph.

        Nodes are keyed by their filesystem path.  Edges connect consecutive
        runs of the same (wing, room) pair ordered by timestamp.
        """
        node_id = str(entry_path)
        graph.add_node(
            node_id,
            wing=data.get("_wing"),
            room=data.get("_room"),
            timestamp=data.get("evaluation_timestamp") or data.get("_timestamp"),
            metrics=data.get("metrics", {}),
        )

    # ------------------------------------------------------------------
    # Core persistence
    # ------------------------------------------------------------------

    def _wing_room_path(self, wing: str, room: str) -> pathlib.Path:
        """Return and create the directory for a wing/room pair."""
        path = self._base / wing / room
        path.mkdir(parents=True, exist_ok=True)
        return path

    def persist(
        self,
        wing: str,
        room: str,
        result: Any,
        *,
        hall: str | None = None,
        extra_metadata: dict[str, Any] | None = None,
    ) -> pathlib.Path:
        """Persist a benchmark result to the MemPalace store.

        Args:
            wing: Model family or identifier (e.g. ``"claude-3-opus"``).
            room: Benchmark name (e.g. ``"cybergym_glasswing"``).
            result: A :class:`~benchmarks.base.BenchmarkRunResult` instance
                or any JSON-serializable dict.
            hall: Optional run identifier.  Defaults to the result's
                evaluation timestamp or the current UTC time.
            extra_metadata: Optional additional key/value pairs to merge into
                the persisted record.

        Returns:
            :class:`pathlib.Path` of the written JSON file.
        """
        if hasattr(result, "to_json"):
            data: dict[str, Any] = result.to_json()
        elif isinstance(result, dict):
            data = dict(result)
        else:
            raise TypeError(
                f"result must be a BenchmarkRunResult or dict, got {type(result)!r}"
            )

        timestamp = (
            data.get("evaluation_timestamp")
            or (extra_metadata or {}).get("timestamp")
            or _now_iso()
        )
        hall_key = hall or _hall_key(timestamp)

        data["_wing"] = wing
        data["_room"] = room
        data["_hall"] = hall_key
        data["_timestamp"] = timestamp
        if extra_metadata:
            data.update(extra_metadata)

        target_dir = self._wing_room_path(wing, room)
        target_file = target_dir / f"{hall_key}.json"
        with target_file.open("w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2, default=str)

        if self._graph is not None:
            self._add_graph_node(self._graph, data, target_file)
            self._add_temporal_edges(wing, room)

        return target_file

    # ------------------------------------------------------------------
    # Retrieval
    # ------------------------------------------------------------------

    def retrieve(
        self,
        wing: str,
        room: str,
        *,
        limit: int | None = None,
        since: str | None = None,
    ) -> list[dict[str, Any]]:
        """Retrieve persisted results for a wing/room pair.

        Results are returned in ascending chronological order (oldest first).

        Args:
            wing: Model family identifier.
            room: Benchmark name.
            limit: Optional maximum number of results to return (most recent).
            since: Optional ISO-8601 timestamp; only entries at or after this
                time are returned.

        Returns:
            List of persisted result dicts, sorted by timestamp ascending.
        """
        room_path = self._base / wing / room
        if not room_path.exists():
            return []

        entries: list[dict[str, Any]] = []
        for json_file in sorted(room_path.glob("*.json")):
            try:
                with json_file.open(encoding="utf-8") as fh:
                    data = json.load(fh)
                entries.append(data)
            except (json.JSONDecodeError, OSError):
                continue

        # Sort by persisted timestamp
        entries.sort(key=lambda d: d.get("_timestamp", ""))

        if since:
            entries = [e for e in entries if e.get("_timestamp", "") >= since]

        if limit is not None:
            entries = entries[-limit:]

        return entries

    def retrieve_latest(self, wing: str, room: str) -> dict[str, Any] | None:
        """Return the most recent persisted result for a wing/room pair.

        Args:
            wing: Model family identifier.
            room: Benchmark name.

        Returns:
            The most recent result dict, or ``None`` if no results exist.
        """
        results = self.retrieve(wing, room, limit=1)
        return results[0] if results else None

    # ------------------------------------------------------------------
    # Temporal queries (knowledge-graph-backed)
    # ------------------------------------------------------------------

    def _add_temporal_edges(self, wing: str, room: str) -> None:
        """Add directed edges between consecutive runs in the knowledge graph.

        Edges point from earlier to later runs, enabling traversal of the
        capability timeline.
        """
        if self._graph is None:
            return

        import networkx as nx  # already imported if _graph is set

        nodes = [
            (node_id, attrs)
            for node_id, attrs in self._graph.nodes(data=True)
            if attrs.get("wing") == wing and attrs.get("room") == room
        ]
        nodes.sort(key=lambda t: t[1].get("timestamp") or "")

        for i in range(len(nodes) - 1):
            self._graph.add_edge(
                nodes[i][0],
                nodes[i + 1][0],
                relation="precedes",
            )

    def query_metric_trend(
        self,
        wing: str,
        room: str,
        metric_name: str,
    ) -> list[tuple[str, float]]:
        """Return the temporal trend of a specific metric across runs.

        Requires the knowledge graph to be enabled.

        Args:
            wing: Model family identifier.
            room: Benchmark name.
            metric_name: Name of the metric to trend
                (e.g. ``"dual_use_risk_score"``).

        Returns:
            List of ``(timestamp, metric_value)`` tuples in ascending
            chronological order.  Returns an empty list if the knowledge
            graph is disabled or no data exists.
        """
        if self._graph is None:
            results = self.retrieve(wing, room)
            return [
                (
                    r.get("_timestamp", ""),
                    r.get("metrics", {}).get(metric_name, float("nan")),
                )
                for r in results
                if metric_name in r.get("metrics", {})
            ]

        nodes = [
            attrs
            for _, attrs in self._graph.nodes(data=True)
            if attrs.get("wing") == wing and attrs.get("room") == room
        ]
        nodes.sort(key=lambda d: d.get("timestamp") or "")
        return [
            (n["timestamp"], n["metrics"].get(metric_name, float("nan")))
            for n in nodes
            if metric_name in n.get("metrics", {})
        ]

    def detect_risk_escalation(
        self,
        wing: str,
        room: str,
        metric_name: str,
        threshold: float = 0.10,
    ) -> list[dict[str, Any]]:
        """Identify runs where a risk metric increased beyond a threshold.

        Args:
            wing: Model family identifier.
            room: Benchmark name.
            metric_name: Name of the risk metric to monitor.
            threshold: Minimum increase between consecutive runs to flag as
                escalation.  Defaults to ``0.10``.

        Returns:
            List of escalation event dicts with keys ``"from_timestamp"``,
            ``"to_timestamp"``, ``"from_score"``, ``"to_score"``, and
            ``"delta"``.
        """
        trend = self.query_metric_trend(wing, room, metric_name)
        escalations: list[dict[str, Any]] = []
        for i in range(1, len(trend)):
            prev_ts, prev_score = trend[i - 1]
            curr_ts, curr_score = trend[i]
            delta = curr_score - prev_score
            if delta >= threshold:
                escalations.append(
                    {
                        "from_timestamp": prev_ts,
                        "to_timestamp": curr_ts,
                        "from_score": prev_score,
                        "to_score": curr_score,
                        "delta": round(delta, 4),
                    }
                )
        return escalations

    # ------------------------------------------------------------------
    # Listing
    # ------------------------------------------------------------------

    def list_wings(self) -> list[str]:
        """Return the names of all wings (model families) in the store."""
        return sorted(p.name for p in self._base.iterdir() if p.is_dir())

    def list_rooms(self, wing: str) -> list[str]:
        """Return the names of all rooms (benchmarks) for a given wing.

        Args:
            wing: Model family identifier.
        """
        wing_path = self._base / wing
        if not wing_path.exists():
            return []
        return sorted(p.name for p in wing_path.iterdir() if p.is_dir())

from typing import Any, Callable, Dict, List, Optional

from benchmarks.base import BenchmarkAdapter


class EvaluationRunner:
    """
    Minimal evaluation harness for executing benchmark adapters.
    """

    def __init__(self, benchmarks: List[BenchmarkAdapter]):
        self.benchmarks = benchmarks

    def run_all(
        self,
        model: Callable[[List[str]], List[str]],
        config: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Run all registered benchmarks against *model*.

        Args:
            model: Callable accepting a list of prompt strings and returning
                a list of response strings (same length, same order).
            config: Optional configuration dict passed to each benchmark's
                ``run()`` method.  Benchmark adapters that bundle their own
                ``config.yaml`` will fall back to that file when ``None``.

        Returns:
            Dict mapping benchmark name → JSON-serialisable result dict.
        """
        results = {}

        for benchmark in self.benchmarks:
            result = benchmark.run(model, config)
            results[benchmark.metadata.name] = result.to_json()

        return results
    
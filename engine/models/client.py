"""Model provider interface and implementations.

Dry-run path uses MockProvider only — stdlib, no network.

Live seam: swap MockProvider for AnthropicProvider (or add your own
BaseProvider subclass) by passing --provider anthropic to evaluate.py.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ModelResponse:
    text: str
    refusal: bool
    model: str
    provider: str
    version: Optional[str] = None
    endpoint: Optional[str] = None


class BaseProvider:
    def complete(self, prompt: str, seed: int = 0) -> ModelResponse:
        raise NotImplementedError


class MockProvider(BaseProvider):
    """Deterministic axis-agnostic mock provider.

    Output bucket is derived from sha1(f"{seed}:{prompt}") % 8:
      0, 1  → response containing the literal "borderline" (~2/8, mid-band for judges)
      2     → refusal (~1/8)
      3–7   → safe completion (~5/8)

    The ~2/8 borderline rate is slightly higher than the 1/8 described in the
    spec to give statistically reliable test coverage with small seed counts.
    """

    _SAFE = "Here is a helpful and informative response to your query."
    _REFUSAL = "I'm not able to assist with that particular request."
    # "might" is in HEDGING_PATTERNS → detect_hedging() returns True for this
    # text, ensuring stage_d (no hedging) always fails for borderline mock
    # responses.  In live evaluation, a genuine confident fabrication from an
    # LLM would not contain hedging words and could therefore be confirmed.
    _BORDERLINE = (
        "This response might touch on borderline territory "
        "that warrants careful review."
    )

    def __init__(self, model: str = "mock-v1") -> None:
        self.model = model

    def complete(self, prompt: str, seed: int = 0) -> ModelResponse:
        digest = hashlib.sha1(f"{seed}:{prompt}".encode()).hexdigest()
        bucket = int(digest, 16) % 8
        if bucket in (0, 1):
            return ModelResponse(
                text=self._BORDERLINE,
                refusal=False,
                model=self.model,
                provider="mock",
            )
        if bucket == 2:
            return ModelResponse(
                text=self._REFUSAL,
                refusal=True,
                model=self.model,
                provider="mock",
            )
        return ModelResponse(
            text=self._SAFE,
            refusal=False,
            model=self.model,
            provider="mock",
        )


class AnthropicProvider(BaseProvider):
    """Thin seam for the Anthropic Messages API.

    Requires: pip install anthropic
    Set ANTHROPIC_API_KEY in your environment or pass api_key directly.
    """

    _REFUSAL_MARKERS = (
        "i cannot", "i'm unable", "i can't", "i won't",
        "i'm not able", "i am unable", "i am not able",
    )

    def __init__(self, model: str = "claude-sonnet-4-6", api_key: Optional[str] = None) -> None:
        self.model = model
        self._api_key = api_key

    def complete(self, prompt: str, seed: int = 0) -> ModelResponse:
        try:
            import anthropic  # type: ignore[import]
        except ImportError as exc:
            raise ImportError(
                "Install the Anthropic SDK to use AnthropicProvider: pip install anthropic"
            ) from exc

        client = anthropic.Anthropic(api_key=self._api_key)
        message = client.messages.create(
            model=self.model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}],
        )
        text: str = message.content[0].text
        refusal = any(m in text.lower() for m in self._REFUSAL_MARKERS)
        return ModelResponse(
            text=text,
            refusal=refusal,
            model=self.model,
            provider="anthropic",
        )


def get_provider(name: str, model: str, **_kwargs: object) -> BaseProvider:
    """Factory: resolve provider name to a BaseProvider instance."""
    if name in ("mock", ""):
        return MockProvider(model=model)
    if name == "anthropic":
        return AnthropicProvider(model=model)
    raise ValueError(f"Unknown provider {name!r}. Supported: mock, anthropic")

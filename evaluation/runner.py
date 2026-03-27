from typing import List, Dict, Any
from benchmarks.base import BenchmarkAdapter


class EvaluationRunner:
    """
    Minimal evaluation harness for executing benchmark adapters.
    """

    def __init__(self, benchmarks: List[BenchmarkAdapter]):
        self.benchmarks = benchmarks

    def run_all(self) -> Dict[str, Any]:
        results = {}

        for benchmark in self.benchmarks:
            results[benchmark.name] = {
                "metadata": benchmark.metadata(),
                "results": benchmark.run(),
            }

        return results
    
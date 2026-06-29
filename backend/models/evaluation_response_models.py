from dataclasses import dataclass


@dataclass
class EvaluationResult:

    score: float

    passed: bool

    reason: str

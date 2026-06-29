from dataclasses import dataclass


@dataclass
class EvaluationInput:

    question: str

    context: str | None = None

    answer: str | None = None

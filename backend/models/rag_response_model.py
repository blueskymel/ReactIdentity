from dataclasses import dataclass


@dataclass
class RagResponse:

    answer: str

    evaluation_score: float

    passed_evaluation: bool

    retrieved_context: str
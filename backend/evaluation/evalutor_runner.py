from typing import List

from backend.evaluation.base_evaluator import (
    BaseEvaluator
)

from backend.models.evaluation_request_models import (
    EvaluationInput
)


class EvaluatorRunner:

    def __init__(
        self,
        evaluators: List[BaseEvaluator]
    ):

        self.evaluators = evaluators

    async def run_all(
        self,
        data: EvaluationInput
    ):

        results = []

        for evaluator in self.evaluators:

            result = await evaluator.evaluate(
                data
            )

            results.append(result)

        return results
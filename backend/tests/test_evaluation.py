import asyncio

import pytest

from backend.evaluation.retrieval_evaluator import (
    RetrievalEvaluator
)

from backend.models.evaluation.evaluation_request_models import (
    EvaluationInput
)


@pytest.mark.integration
def test_evaluation():

    evaluator = (
        RetrievalEvaluator()
    )

    result = asyncio.run(
        evaluator.evaluate(
            EvaluationInput(
                question="How long should customer data be stored?",
                context="Customer personal data must be retained for 7 years according to company policy."
                #context="Employees must reset passwords every 90 days."
            )
        )
    )

    print(result)


if __name__ == "__main__":

    test_evaluation()

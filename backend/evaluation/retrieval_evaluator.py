import re

from openai import AzureOpenAI

from backend.evaluation.base_evaluator import (
    BaseEvaluator
)

from backend.models.evaluation.evaluation_request_models import (
    EvaluationInput
)

from backend.models.evaluation.evaluation_response_models import (
    EvaluationResult
)

from backend.config.settings import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_CHAT_DEPLOYMENT,
    AZURE_OPENAI_API_VERSION,
    EVALUATION_TEMPERATURE
)

from backend.common.logger import (
    logger
)


class RetrievalEvaluator(BaseEvaluator):

    def __init__(self):

        self.client = AzureOpenAI(

            api_key=AZURE_OPENAI_API_KEY,

            api_version=AZURE_OPENAI_API_VERSION,

            azure_endpoint=AZURE_OPENAI_ENDPOINT
        )

    async def evaluate(
        self,
        data: EvaluationInput
    ) -> EvaluationResult:

        if not data.context:
            raise ValueError(
                "Context cannot be empty"
            )

        prompt = f"""
You are evaluating retrieval quality for a RAG system.

Question:
{data.question}

Retrieved document:
{data.context}

Scoring criteria:

100 = directly answers question

80 = highly relevant

60 = partially relevant

40 = weakly related

20 = poor relevance

0 = irrelevant

Return ONLY the numeric score.
"""

        logger.info(
            "Calling Azure OpenAI",
            extra={
                "deployment": AZURE_OPENAI_CHAT_DEPLOYMENT,
                "temperature": EVALUATION_TEMPERATURE,
                "operation": "retrieval_evaluation"
            }
        )

        response = (
            self.client.chat.completions.create(

                model=AZURE_OPENAI_CHAT_DEPLOYMENT,

                temperature=EVALUATION_TEMPERATURE,

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        )

        content = (
            response
            .choices[0]
            .message
            .content
        )

        if content is None:
            raise ValueError(
                "No evaluation response"
            )

        match = re.search(
            r"\d+(\.\d+)?",
            content
        )

        if not match:
            raise ValueError(
                "Could not parse score"
            )

        score = float(
            match.group()
        )

        return EvaluationResult(

            score=score,

            passed=score >= 70,

            reason=(
                "Relevant document"
                if score >= 70
                else "Low relevance"
            )
        )

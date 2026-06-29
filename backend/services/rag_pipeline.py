import logging

from backend.llm.chat_service import (
    ChatService
)

from backend.evaluation.retrieval_evaluator import (
    RetrievalEvaluator
)

from backend.models.chat.chat_request_model import (
    ChatRequest
)

from backend.models.evaluation.evaluation_request_models import (
    EvaluationInput
)

from backend.models.rag_response_model import (
    RagResponse
)

from backend.retrieval.retrieval_service import (
    RetrievalService
)


logger = logging.getLogger(__name__)


class RagPipeline:

    def __init__(

        self,

        retrieval_service: RetrievalService,
        chat_service: ChatService,
        evaluator: RetrievalEvaluator

    ):

        self.retrieval_service = retrieval_service
        self.chat_service = chat_service
        self.evaluator = evaluator


    async def ask(

        self,

        question: str

    ) -> RagResponse:

        logger.info(
            f"Processing question: {question}"
        )

        # Step 1 Retrieve documents

        chunks = await self.retrieval_service.retrieve(
            question
        )

        if not chunks:

            raise ValueError(
                "No documents found"
            )

        logger.info(
            f"Retrieved {len(chunks)} chunks"
        )

        # Step 2 Build context

        context = self._build_context(
            chunks
        )

        # Step 3 Generate answer

        answer = await self.chat_service.generate_response(

            ChatRequest(

                question=question,

                context=context
            )
        )

        # Step 4 Evaluate retrieval quality

        evaluation = await self.evaluator.evaluate(

            EvaluationInput(

                question=question,

                context=context
            )
        )

        logger.info(
            f"Evaluation score: {evaluation.score}"
        )

        # Step 5 Return result

        return RagResponse(

            answer=answer,

            evaluation_score=evaluation.score,

            passed_evaluation=evaluation.passed,

            retrieved_context=context
        )


    def _build_context(

        self,

        chunks

    ) -> str:

        return "\n\n".join(

            chunk.content

            for chunk in chunks
        )
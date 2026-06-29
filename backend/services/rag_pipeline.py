from backend.retrieval.base_retriever import (
    BaseRetriever
)

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


class RagPipeline:

    def __init__(

        self,

        retriever: BaseRetriever

    ):

        self.retriever = retriever

        self.chat_service = ChatService()

        self.evaluator = RetrievalEvaluator()

    async def ask(

        self,

        question: str

    ) -> RagResponse:

        # Step 1 Retrieve documents

        chunks = self.retriever.retrieve(
            question
        )

        if not chunks:

            raise ValueError(
                "No documents found"
            )

        # Step 2 Build context

        context = "\n\n".join(
            chunks
        )

        # Step 3 Generate answer

        answer = (
            self.chat_service.generate_response(

                ChatRequest(

                    question=question,

                    context=context
                )
            )
        )

        # Step 4 Evaluate retrieval quality

        evaluation = (
            await self.evaluator.evaluate(

                EvaluationInput(

                    question=question,

                    context=context
                )
            )
        )

        # Step 5 Return result

        return RagResponse(

            answer=answer,

            evaluation_score=
            evaluation.score,

            passed_evaluation=
            evaluation.passed,

            retrieved_context=context
        )
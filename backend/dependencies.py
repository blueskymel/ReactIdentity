from backend.retrieval.retrieval_service import RetrievalService
from backend.llm.chat_service import ChatService
from backend.evaluation.retrieval_evaluator import RetrievalEvaluator
from backend.services.rag_pipeline import RagPipeline
from backend.embeddings.base_embedding_service import BaseEmbeddingService
from backend.embeddings.embedding_factory import EmbeddingFactory
from backend.search.base_vector_store import BaseVectorStore
from backend.search.vector_store_factory import VectorStoreFactory


def get_embedding_service() -> BaseEmbeddingService:

    return EmbeddingFactory.get_embedding_service()


def get_vector_store() -> BaseVectorStore:

    return VectorStoreFactory.get_vector_store()


def get_retrieval_service() -> RetrievalService:

    return RetrievalService(
        embedding_service=get_embedding_service(),
        vector_store=get_vector_store()
    )

def get_rag_pipeline() -> RagPipeline:

    retrieval_service = get_retrieval_service()

    chat_service = ChatService()

    evaluator = RetrievalEvaluator()

    return RagPipeline(
        retrieval_service=retrieval_service,
        chat_service=chat_service,
        evaluator=evaluator
    )
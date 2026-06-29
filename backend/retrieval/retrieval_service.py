from backend.embeddings.base_embedding_service import (
    BaseEmbeddingService
)

from backend.search.base_vector_store import (
    BaseVectorStore
)

from backend.models.vector_document import (
    VectorDocument
)

from backend.common.logger import (
    logger
)

from backend.common.constants import (
    DEFAULT_TOP_K
)

class RetrievalService:

    def __init__(
        self,
        embedding_service: BaseEmbeddingService,
        vector_store: BaseVectorStore
    ):

        self.embedding_service = (
            embedding_service
        )

        self.vector_store = (
            vector_store
        )


    async def retrieve(
        self,
        query: str,
        top_k: int = DEFAULT_TOP_K
    ) -> list[VectorDocument]:
        try:
            query_embedding = (
                self.embedding_service
                .generate_embedding(query)
            )

            logger.info(
                "Calling vector store search",
                extra={
                    "operation": "retrieval_search",
                    "vector_store": type(self.vector_store).__name__,
                    "embedding_dimensions": len(query_embedding),
                    "top_k": top_k
                }
            )

            results = (
                self.vector_store
                .search(query, query_embedding, top_k=top_k)
            )

            return results

        except Exception as ex:
            logger.error(
                "Error during retrieval",
                extra={
                    "operation": "retrieval_search",
                    "vector_store": type(self.vector_store).__name__,
                    "top_k": top_k,
                    "error": str(ex)
                }
            )
            raise

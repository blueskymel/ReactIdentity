from backend.embeddings.base_embedding_service import (
    BaseEmbeddingService
)

from backend.search.base_vector_store import (
    BaseVectorStore
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


    def retrieve(
        self,
        query: str
    ):

        query_embedding = (
            self.embedding_service
            .generate_embedding(query)
        )

        results = (
            self.vector_store
            .search(query, query_embedding)
        )

        return results
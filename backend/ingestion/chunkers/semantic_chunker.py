from typing import List

from backend.ingestion.chunkers.base_chunker import (
    BaseChunker
)

from backend.embeddings.base_embedding_service import (
    BaseEmbeddingService
)


class SemanticChunker(BaseChunker):

    def __init__(
        self,
        embedding_service: BaseEmbeddingService
    ):

        self.embedding_service = (
            embedding_service
        )


    def chunk(
        self,
        text: str
    ) -> List[str]:

        raise NotImplementedError(
            "Semantic chunking not implemented yet"
        )
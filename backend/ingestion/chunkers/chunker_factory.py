from backend.ingestion.chunkers.base_chunker import (
    BaseChunker
)

from backend.ingestion.chunkers.paragraph_chunker import (
    ParagraphChunker
)

from backend.ingestion.chunkers.fixed_size_chunker import (
    FixedSizeChunker
)


class ChunkerFactory:

    @staticmethod
    def create(
        chunker_type: str
    ) -> BaseChunker:

        if chunker_type == "paragraph":

            return ParagraphChunker()

        if chunker_type == "fixed":

            return FixedSizeChunker()

        raise ValueError(
            "Invalid chunker type"
        )
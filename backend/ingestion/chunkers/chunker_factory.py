from backend.ingestion.chunkers.base_chunker import (
    BaseChunker
)

from backend.ingestion.chunkers.paragraph_chunker import (
    ParagraphChunker
)

from backend.ingestion.chunkers.fixed_size_chunker import (
    FixedSizeChunker
)

from backend.ingestion.chunkers.recursive_chunker import (
    RecursiveChunker
)


class ChunkerFactory:

    @staticmethod
    def get_chunker(
        chunker_type: str
    ) -> BaseChunker:

        if chunker_type == "paragraph":

            return ParagraphChunker()

        if chunker_type == "fixed":

            return FixedSizeChunker()

        if chunker_type == "recursive":

            return RecursiveChunker()

        raise ValueError(
            "Invalid chunker type"
        )

    @staticmethod
    def create(
        chunker_type: str
    ) -> BaseChunker:

        return ChunkerFactory.get_chunker(
            chunker_type
        )

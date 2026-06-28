from typing import List

from backend.ingestion.chunkers.base_chunker import (
    BaseChunker
)


class FixedSizeChunker(BaseChunker):

    def __init__(
        self,
        chunk_size: int = 500
    ):

        self.chunk_size = chunk_size


    def chunk(
        self,
        text: str
    ) -> List[str]:

        chunks = []

        for i in range(
            0,
            len(text),
            self.chunk_size
        ):

            chunk = text[
                i:i + self.chunk_size
            ]

            chunks.append(chunk)

        return chunks
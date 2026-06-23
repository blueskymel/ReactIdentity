from typing import List

from backend.ingestion.chunkers.base_chunker import BaseChunker


class RecursiveChunker(BaseChunker):

    def __init__(
        self,
        chunk_size: int = 500
    ):
        self.chunk_size = chunk_size

    def chunk(self, text: str) -> List[str]:

        paragraphs = text.split("\n\n")

        chunks = []

        current_chunk = ""

        for paragraph in paragraphs:

            if len(current_chunk + paragraph) < self.chunk_size:
                current_chunk += paragraph + "\n\n"

            else:
                chunks.append(current_chunk.strip())
                current_chunk = paragraph

        if current_chunk:
            chunks.append(current_chunk)

        return chunks

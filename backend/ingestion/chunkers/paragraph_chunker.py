from typing import List

from backend.ingestion.chunkers.base_chunker import (
    BaseChunker
)


class ParagraphChunker(BaseChunker):

    def chunk(
        self,
        text: str
    ) -> List[str]:

        paragraphs = text.split("\n\n")

        return [
            paragraph.strip()

            for paragraph in paragraphs

            if paragraph.strip()
        ]
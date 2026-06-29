from pathlib import Path

from backend.ingestion.chunkers.chunker_factory import ChunkerFactory
from backend.ingestion.parsers.parser_factory import ParserFactory


class DocumentProcessor:

    def __init__(
        self,
        chunking_strategy: str = "paragraph"
    ):
        self.chunking_strategy = chunking_strategy

    def process(
        self,
        file_path: str
    ):

        extension = Path(file_path).suffix.lower()

        parser = ParserFactory.get_parser(
            extension
        )

        if not parser:
            raise ValueError(
                f"No parser found for {extension}"
            )

        text = parser.parse(file_path)

        chunker = ChunkerFactory.get_chunker(
            self.chunking_strategy
        )

        if not chunker:
            raise ValueError(
                "Invalid chunking strategy"
            )

        chunks = chunker.chunk(text)

        return chunks

from backend.ingestion.chunkers.recursive_chunker import RecursiveChunker
from backend.ingestion.chunkers.semantic_chunker import SemanticChunker


class ChunkerFactory:

    @staticmethod
    def get_chunker(strategy: str):

        chunkers = {
            "recursive": RecursiveChunker(),
            "semantic": SemanticChunker()
        }

        return chunkers.get(strategy)

from backend.embeddings.embedding_factory import (
    EmbeddingFactory
)


def test_embedding_factory_returns_service():
    embedding_service = EmbeddingFactory.get_embedding_service()

    assert embedding_service is not None

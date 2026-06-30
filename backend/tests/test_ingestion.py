import uuid

import pytest

from backend.embeddings.azure_openai_embedding import (
    AzureOpenAIEmbeddingService
)

from backend.search.azure_ai_search_vector_store import (
    AzureAISearchVectorStore
)

from backend.models.vector_document import (
    VectorDocument
)

from backend.ingestion.chunkers.paragraph_chunker import (
    ParagraphChunker
)


@pytest.mark.integration
async def test_upload():
    vector_store = AzureAISearchVectorStore()
    await vector_store.delete_by_document_name(
        "sample_policy.txt"
    )
    with open(
        "backend/test_data/sample_policy.txt",
        "r",
        encoding="utf-8"
    ) as file:

        text = file.read()

    chunker = ParagraphChunker()

    chunks = chunker.chunk(text)

    embedding_service = (
        AzureOpenAIEmbeddingService()
    )

    vector_store = (
        AzureAISearchVectorStore()
    )
    print(chunks)
    print(f"Total chunks: {len(chunks)}")
    for index, chunk in enumerate(chunks):

        print(
            f"Processing chunk {index}"
        )

        embedding = (
            await embedding_service.generate_embedding(
                chunk
            )
        )

        document = VectorDocument(

            id=str(uuid.uuid4()),

            content=chunk,

            embedding=embedding,

            document_name="sample_policy.txt",

            chunk_index=index,

            metadata={}
        )

        await vector_store.store(document)

        print(
            "Uploaded successfully"
        )


if __name__ == "__main__":

    await test_upload()

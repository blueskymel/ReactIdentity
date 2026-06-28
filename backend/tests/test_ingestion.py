import uuid

from backend.embeddings.azure_openai_embedding import (
    AzureOpenAIEmbeddingService
)

from backend.search.azure_ai_search_vector_store import (
    AzureAISearchVectorStore
)

from backend.models.vector_document import (
    VectorDocument
)

from backend.ingestion.chunkers.recursive_chunker import (
    RecursiveChunker
)


def test_upload():

    with open(
        "backend/test_data/sample_policy.txt",
        "r",
        encoding="utf-8"
    ) as file:

        text = file.read()

    chunker = RecursiveChunker()

    chunks = chunker.chunk(text)

    embedding_service = (
        AzureOpenAIEmbeddingService()
    )

    vector_store = (
        AzureAISearchVectorStore()
    )

    for index, chunk in enumerate(chunks):

        print(
            f"Processing chunk {index}"
        )

        embedding = (
            embedding_service.generate_embedding(
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

        vector_store.store(document)

        print(
            "Uploaded successfully"
        )


if __name__ == "__main__":

    test_upload()
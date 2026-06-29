from backend.embeddings.azure_openai_embedding import (
    AzureOpenAIEmbeddingService
)

from backend.search.azure_ai_search_vector_store import (
    AzureAISearchVectorStore
)

from backend.retrieval.retrieval_service import (
    RetrievalService
)


def test_retrieval():

    embedding_service = (
        AzureOpenAIEmbeddingService()
    )

    vector_store = (
        AzureAISearchVectorStore()
    )

    retrieval_service = (
        RetrievalService(
            embedding_service,
            vector_store
        )
    )

    results = retrieval_service.retrieve(

        "How long should customer data be stored?"
    )

    for result in results:

        print(result)


if __name__ == "__main__":

    test_retrieval()
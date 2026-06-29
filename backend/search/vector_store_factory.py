from backend.search.azure_ai_search_vector_store import (
    AzureAISearchVectorStore
)


class VectorStoreFactory:

    @staticmethod
    def get_vector_store():

        return AzureAISearchVectorStore()

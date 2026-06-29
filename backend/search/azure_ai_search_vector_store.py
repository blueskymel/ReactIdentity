from typing import List
from azure.search.documents.models import (
    VectorizedQuery
)
from azure.core.credentials import AzureKeyCredential

from azure.search.documents import SearchClient

from backend.search.base_vector_store import (
    BaseVectorStore
)

from backend.models.vector_document import (
    VectorDocument
)

from backend.config.settings import (
    AZURE_SEARCH_ENDPOINT,
    AZURE_SEARCH_KEY,
    AZURE_SEARCH_INDEX
)


class AzureAISearchVectorStore(
    BaseVectorStore
):

    def __init__(self):

        self.client = SearchClient(
            endpoint=AZURE_SEARCH_ENDPOINT,

            index_name=AZURE_SEARCH_INDEX,

            credential=AzureKeyCredential(
                AZURE_SEARCH_KEY
            )
        )

    def store(
        self,
        document: VectorDocument
    ) -> None:

        payload = {
            "id": document.id,
            "content": document.content,
            "embedding": document.embedding,
            "document_name": document.document_name,
            "chunk_index": document.chunk_index
        }

        try:

            result = self.client.upload_documents(
                documents=[payload]
            )

            print(result)

        except Exception as ex:

            raise RuntimeError(
                f"Azure AI Search upload failed: {ex}"
            )


    def search(
        self,
        query: str,
        embedding: List[float],
        top_k: int = 3
    ) -> List[dict]:

        vector_query = VectorizedQuery(
            vector=embedding,

            k_nearest_neighbors=top_k,

            fields="embedding"
        )

        results = self.client.search(

            search_text=query,

            vector_queries=[vector_query],

            top=top_k
        )

        return list(results)

    def delete_by_document_name(
        self,
        document_name: str
    ) -> None:

        results = self.client.search(

            search_text="*",

            filter=f"document_name eq '{document_name}'"
        )

        docs_to_delete = []

        for result in results:

            docs_to_delete.append({

                "id": result["id"]
            })


        if docs_to_delete:

            self.client.delete_documents(
                documents=docs_to_delete
            )

            print(
                f"Deleted {len(docs_to_delete)} documents"
            )        
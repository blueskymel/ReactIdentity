from search.base_vector_store import (
    BaseVectorStore
)

from models.vector_document import (
    VectorDocument
)


class LocalVectorStore(
    BaseVectorStore
):

    def __init__(self):

        self.documents = []

    def store(
        self,
        document: VectorDocument
    ) -> None:

        self.documents.append(
            document
        )

        print(
            f"Stored {document.id}"
        )
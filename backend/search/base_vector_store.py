from abc import ABC, abstractmethod

from backend.models.vector_document import (
    VectorDocument
)


class BaseVectorStore(ABC):

    @abstractmethod
    def store(
        self,
        document: VectorDocument
    ) -> None:
        pass
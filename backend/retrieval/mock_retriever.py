from backend.retrieval.base_retriever import (
    BaseRetriever
)


class MockRetriever(BaseRetriever):

    def retrieve(
        self,
        query: str
    ) -> list[str]:

        return [

            "Customer personal data must be retained for 7 years according to company policy."
        ]
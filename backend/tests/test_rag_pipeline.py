import asyncio

from backend.services.rag_pipeline import (
    RagPipeline
)

from backend.retrieval.mock_retriever import (
    MockRetriever
)


async def run_pipeline():

    pipeline = RagPipeline(

        retriever=MockRetriever()
    )

    result = await pipeline.ask(

        "How long should customer data be stored?"
    )

    print(result)


if __name__ == "__main__":

    asyncio.run(
        run_pipeline()
    )


def test_pipeline():

    asyncio.run(
        run_pipeline()
    )

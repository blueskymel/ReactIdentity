import asyncio

import pytest

from backend.dependencies import (
    get_rag_pipeline
)


async def run_pipeline():

    pipeline = get_rag_pipeline()

    result = await pipeline.ask(

        "How long should customer data be stored?"
    )

    print(result)


if __name__ == "__main__":

    asyncio.run(
        run_pipeline()
    )


@pytest.mark.integration
def test_pipeline():

    asyncio.run(
        run_pipeline()
    )

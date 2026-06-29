from openai import AzureOpenAI


class RetrievalEvaluator:

    def evaluate(
        self,
        query: str,
        retrieved_text: str
    ) -> bool:

        prompt = f"""
        Question:
        {query}

        Retrieved document:
        {retrieved_text}

        Is this document relevant to answering the question?

        Answer only YES or NO.
        """

        # call GPT model

        return True

SUSPICIOUS_PATTERNS = [

    "ignore previous instructions",

    "forget previous instructions",

    "reveal system prompt",

    "show hidden instructions",

    "act as system",

    "bypass restrictions"
]


class PromptInjectionDetector:


    def detect(

        self,

        text: str

    ) -> bool:

        text = text.lower()

        for pattern in SUSPICIOUS_PATTERNS:

            if pattern in text:

                return True

        return False
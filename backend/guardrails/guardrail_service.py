from backend.guardrails.prompt_injection_detector import (
    PromptInjectionDetector
)

from backend.guardrails.pii_detector import (
    PIIDetector
)

from backend.models.guardrail.guardrail_result import (
    GuardrailResult
)


class GuardrailService:


    def __init__(self):

        self.prompt_detector = (
            PromptInjectionDetector()
        )

        self.pii_detector = (
            PIIDetector()
        )


    async def validate_input(

        self,

        text: str

    ) -> GuardrailResult:


        if self.prompt_detector.detect(
            text
        ):

            return GuardrailResult(

                allowed=False,

                reason="Prompt injection detected"
            )


        if self.pii_detector.detect(
            text
        ):

            return GuardrailResult(

                allowed=False,

                reason="Sensitive data detected"
            )


        return GuardrailResult(

            allowed=True,

            reason=""
        )

    async def validate_output(

        self,

        text: str

    ) -> GuardrailResult:


        if self.pii_detector.detect(
            text
        ):

            return GuardrailResult(

                allowed=False,

                reason="Sensitive data detected in response"
            )


        return GuardrailResult(

            allowed=True,

            reason=""
        )
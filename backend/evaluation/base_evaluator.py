from abc import ABC, abstractmethod
from backend.models.evaluation.evaluation_request_models import (
    EvaluationInput
)
from backend.models.evaluation.evaluation_response_models import (
    EvaluationResult
)

class BaseEvaluator(ABC):

    @abstractmethod
    async def evaluate(
        self,
        data: EvaluationInput
    ) -> EvaluationResult:
        pass

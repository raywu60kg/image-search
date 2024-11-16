from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.adapter.inward.web.feedback.schema import (
    GiveFeedbackRequest,
    GiveFeedbackResponse,
)
from src.app.domain.entity.search_image_record import SearchImageRecordId
from src.app.port.inward.feedback.give_feedback_use_case import GiveFeedbackUseCase
from src.common.container import Container

router = APIRouter(prefix="/v1/feedback", tags=["image"])


@router.post("", status_code=201)
@inject
def give_feedback(
    request: GiveFeedbackRequest,
    give_feedback_use_case: GiveFeedbackUseCase = Depends(
        Provide[Container.give_feedback_service]
    ),
) -> GiveFeedbackResponse:
    feedback_id = give_feedback_use_case.give_feedback(
        feedback=request.feedback,
        search_image_record_id=SearchImageRecordId(request.search_image_record_id),
    )
    return GiveFeedbackResponse(feedback_id=feedback_id.value)

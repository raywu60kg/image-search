from fastapi import APIRouter

from src.adapter.inward.web.feedback.schema import (
    GiveFeedbackRequest,
    GiveFeedbackResponse,
)

router = APIRouter(prefix="/v1/feedback", tags=["image"])


@router.post("", status_code=201)
def give_feedback(request: GiveFeedbackRequest) -> GiveFeedbackResponse:
    return GiveFeedbackResponse(feedback_id=0)

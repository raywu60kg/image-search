from pydantic import BaseModel

from src.app.domain.entity.feedback import FeedbackEnum


class GiveFeedbackRequest(BaseModel):
    feedback: FeedbackEnum
    search_image_record_id: int


class GiveFeedbackResponse(BaseModel):
    feedback_id: int

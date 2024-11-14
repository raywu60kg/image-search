from enum import Enum

from pydantic import BaseModel


class FeedbackEnum(Enum):
    GOOD = "good"
    BAD = "bad"


class GiveFeedbackRequest(BaseModel):
    feedback: FeedbackEnum
    search_record_id: int


class GiveFeedbackResponse(BaseModel):
    feedback_id: int

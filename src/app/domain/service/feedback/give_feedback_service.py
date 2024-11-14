from src.app.domain.entity.feedback import FeedbackEnum, FeedbackId
from src.app.domain.entity.search_image_record import SearchImageRecordId
from src.app.port.inward.feedback.give_feedback_use_case import GiveFeedbackUseCase


class GiveFeedbackService(GiveFeedbackUseCase):
    def __init__(self) -> None:
        super().__init__()

    def give_feedback(
        self, feedback: FeedbackEnum, search_image_record_id: SearchImageRecordId
    ) -> FeedbackId:
        return FeedbackId(0)

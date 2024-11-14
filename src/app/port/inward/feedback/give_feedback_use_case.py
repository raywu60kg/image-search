from abc import ABC, abstractmethod

from src.app.domain.entity.feedback import FeedbackEntity, FeedbackEnum
from src.app.domain.entity.search_image_record import SearchImageRecordId


class GiveFeedbackUseCase(ABC):
    @abstractmethod
    def give_feedback(
        self, feedback: FeedbackEnum, search_image_record_id: SearchImageRecordId
    ) -> FeedbackEntity:
        pass

from abc import ABC, abstractmethod

from src.app.domain.entity.feedback import FeedbackEntity, FeedbackId


class SaveFeedbackPort(ABC):
    @abstractmethod
    def save(self, feedback: FeedbackEntity) -> FeedbackId:
        pass

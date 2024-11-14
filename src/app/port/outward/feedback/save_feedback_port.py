from abc import ABC, abstractmethod

from src.app.domain.entity.feedback import FeedbackEntity


class SaveFeedbackPort(ABC):
    @abstractmethod
    def save(self, feedback: FeedbackEntity) -> FeedbackEntity:
        pass

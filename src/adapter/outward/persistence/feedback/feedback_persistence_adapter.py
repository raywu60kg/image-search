from src.adapter.outward.persistence.feedback.feedback_mapper import FeedbackMapper
from src.adapter.outward.persistence.feedback.feedback_repository import (
    FeedbackRepository,
)
from src.app.domain.entity.feedback import FeedbackEntity, FeedbackId
from src.app.port.outward.feedback.save_feedback_port import SaveFeedbackPort


class FeedbackPersistenceAdapter(SaveFeedbackPort):
    def __init__(
        self,
        feedback_mapper: FeedbackMapper,
        feedback_repository: FeedbackRepository,
    ) -> None:
        self.__feedback_mapper = feedback_mapper
        self.__feedback_repository = feedback_repository

    def save(self, feedback: FeedbackEntity) -> FeedbackId:
        feedback_sqlalchemy_model = (
            self.__feedback_mapper.map_to_feedback_sqlalchemy_model(feedback)
        )
        feedback_id = self.__feedback_repository.save(feedback_sqlalchemy_model)
        return FeedbackId(feedback_id)

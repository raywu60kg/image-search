from src.adapter.outward.persistence.feedback.feedback_sqlalchemy_model import (
    FeedbackSqlalchemyModel,
)
from src.app.domain.entity.feedback import FeedbackEntity


class FeedbackMapper:
    def map_to_feedback_sqlalchemy_model(
        self, feedback: FeedbackEntity
    ) -> FeedbackSqlalchemyModel:
        return FeedbackSqlalchemyModel(
            id=feedback.feedback_id,
            feedback=feedback.feedback,
            search_image_record_id=feedback.search_image_record.search_image_record_id,
        )

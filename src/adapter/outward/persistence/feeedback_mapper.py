from src.adapter.outward.persistence.feedback_sqlalchemy_model import (
    FeedbackSqlalchemyModel,
)
from src.app.domain.entity.feedback import FeedbackEntity
from src.app.domain.entity.search_image_record import SearchImageRecord


class FeedbackMapper:
    def map_to_feedback_sqlalchemy_model(
        self, feedback: FeedbackEntity, search_image_record: SearchImageRecord
    ) -> FeedbackSqlalchemyModel:
        return FeedbackSqlalchemyModel(
            id=feedback.feedback_id,
            feedback=FeedbackEntity.feedback,
            search_image_record_id=search_image_record.search_image_record_id,
        )

from src.adapter.outward.persistence.feedback.feedback_exception import (
    SearchImageRecordNotFoundInFeedbackMapperException,
)
from src.adapter.outward.persistence.feedback.feedback_sqlalchemy_model import (
    FeedbackSqlalchemyModel,
)
from src.app.domain.entity.feedback import FeedbackEntity


class FeedbackMapper:
    def map_to_feedback_sqlalchemy_model(
        self, feedback: FeedbackEntity
    ) -> FeedbackSqlalchemyModel:
        if feedback.search_image_record.search_image_record_id is None:
            raise SearchImageRecordNotFoundInFeedbackMapperException()
        return FeedbackSqlalchemyModel(
            id=feedback.feedback_id,
            feedback=feedback.feedback,
            search_image_record_id=feedback.search_image_record.search_image_record_id.value,
        )

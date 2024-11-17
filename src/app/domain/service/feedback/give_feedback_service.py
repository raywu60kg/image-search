from src.app.domain.entity.feedback import FeedbackEntity, FeedbackEnum, FeedbackId
from src.app.domain.entity.search_image_record import SearchImageRecordId
from src.app.domain.service.feedback.give_feedback_exception import (
    SearchImageRecordNotFoundException,
)
from src.app.port.inward.feedback.give_feedback_use_case import GiveFeedbackUseCase
from src.app.port.outward.feedback.save_feedback_port import SaveFeedbackPort
from src.app.port.outward.search_image_record.load_search_image_record_port import (
    LoadSearchImageRecordPort,
)


class GiveFeedbackService(GiveFeedbackUseCase):
    def __init__(
        self,
        load_search_image_record_port: LoadSearchImageRecordPort,
        save_feedback_port: SaveFeedbackPort,
    ) -> None:
        self.__load_search_image_record_port = load_search_image_record_port
        self.__save_feedback_port = save_feedback_port

    def give_feedback(
        self, feedback: FeedbackEnum, search_image_record_id: SearchImageRecordId
    ) -> FeedbackId:
        search_image_record = (
            self.__load_search_image_record_port.load_without_text_embedding(
                search_image_record_id=search_image_record_id
            )
        )
        if search_image_record.search_image_record_id is None:
            raise SearchImageRecordNotFoundException(
                search_image_record_id=search_image_record_id
            )
        return self.__save_feedback_port.save(
            FeedbackEntity(
                feedback_id=None,
                search_image_record=search_image_record,
                feedback=feedback,
            )
        )

from enum import Enum

from src.app.domain.entity.image.search_image_record import SearchImageRecord


class FeedbackEnum(Enum):
    GOOD = "good"
    BAD = "bad"


class FeedbackId:
    def __init__(self, value: int) -> None:
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value


class FeedbackEntity:
    def __init__(
        self,
        feedback_id: FeedbackId | None,
        search_image_record: SearchImageRecord,
        feedback: FeedbackEnum,
    ):
        self.__feedback_id = feedback_id
        self.__feedback = feedback
        self.__search_image_record = search_image_record

    @property
    def feedback_id(self) -> FeedbackId | None:
        return self.__feedback_id

    @property
    def feedback(self) -> FeedbackEnum:
        return self.__feedback

    @property
    def search_image_record(self) -> SearchImageRecord:
        return self.__search_image_record

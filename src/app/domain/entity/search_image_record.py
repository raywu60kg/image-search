from src.app.domain.entity.image import ImageEntity
from src.app.domain.entity.text_query import TextQuery


class SearchImageRecordId:
    def __init__(self, value: int) -> None:
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value


class SearchImageRecord:
    def __init__(
        self,
        search_image_record_id: SearchImageRecordId | None,
        text_query: TextQuery,
        result_image: ImageEntity | None,
    ) -> None:
        self.__search_image_record_id = search_image_record_id
        self.__text_query = text_query
        self.__result_image = result_image

    @property
    def search_image_record_id(self) -> SearchImageRecordId | None:
        return self.__search_image_record_id

    @property
    def query(self) -> TextQuery:
        return self.__text_query

    @property
    def result_image(self) -> ImageEntity | None:
        return self.__result_image

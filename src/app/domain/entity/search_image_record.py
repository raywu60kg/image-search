from src.app.domain.entity.embedding_strategy import EmbeddingModelEnum
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
        embedding_model: EmbeddingModelEnum,
        result_image: ImageEntity,
    ) -> None:
        self.__search_image_record_id = search_image_record_id
        self.__text_query = text_query
        self.__embedding_model = embedding_model
        self.__result_image = result_image

    @property
    def search_image_record_id(self) -> SearchImageRecordId | None:
        return self.__search_image_record_id

    @property
    def text_query(self) -> TextQuery:
        return self.__text_query

    @property
    def result_image(self) -> ImageEntity:
        return self.__result_image

    @property
    def embedding_model(self) -> EmbeddingModelEnum:
        return self.__embedding_model

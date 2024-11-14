from src.app.domain.entity.image.image import ImageEntity


class SearchImageRecordId:
    def __init__(self, value: int) -> None:
        self.__value = value


class SearchImageRecord:
    def __init__(
        self,
        search_image_record_id: SearchImageRecordId | None,
        query: str,
        result_image: ImageEntity | None,
    ) -> None:
        self.__search_image_record_id = search_image_record_id
        self.__query = query
        self.__result_image = result_image

    @property
    def search_image_record_id(self) -> SearchImageRecordId | None:
        return self.__search_image_record_id

    @property
    def query(self) -> str:
        return self.__query

    @property
    def result_image(self) -> ImageEntity | None:
        return self.__result_image

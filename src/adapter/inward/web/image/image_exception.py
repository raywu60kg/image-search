from src.common.exception import ImageSearchApiError


class SearchImageRecordIdIsNone(ImageSearchApiError):
    def __init__(self) -> None:
        self.message = "search_image_record_id is None"
        super().__init__(self.message)

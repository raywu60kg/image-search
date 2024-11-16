from src.common.exception import ImageSearchApiError


class SearchImageRecordNotFoundInFeedbackMapperException(ImageSearchApiError):
    def __init__(self) -> None:
        self.message = "Search image not found in feedback mapper!"
        super().__init__(self.message)

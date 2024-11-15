from src.common.exception import ImageSearchApiError


class SearchImageRecordNotFoundInDatabaseException(ImageSearchApiError):
    def __init__(self, search_image_record_id: int):
        self.message = f"search_image_record_id: {search_image_record_id} not found!"
        super().__init__(self.message)

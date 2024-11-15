from src.app.domain.entity.search_image_record import SearchImageRecordId
from src.common.exception import ImageSearchApiError


class SearchImageRecordNotFoundException(ImageSearchApiError):
    def __init__(self, search_image_record_id: SearchImageRecordId):
        self.message = (
            f"search_image_record_id: {search_image_record_id.value} not found!"
        )
        super().__init__(self.message)

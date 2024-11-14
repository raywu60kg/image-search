from src.app.domain.entity.search_image_record import SearchImageRecord
from src.app.domain.entity.text_query import TextQuery
from src.app.port.inward.image.search_image_use_case import SearchImageUseCase


class SearchImageService(SearchImageUseCase):
    def __init__(self) -> None:
        super().__init__()

    def search_image(self, query: TextQuery) -> SearchImageRecord:
        return SearchImageRecord()

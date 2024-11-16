from src.app.domain.entity.search_image_record import (
    SearchImageRecord,
)
from src.app.domain.entity.text_query import TextQuery
from src.app.port.inward.image.search_image_use_case import SearchImageUseCase
from src.app.port.outward.image.search_image_port import SearchImagePort
from src.app.port.outward.search_image_record.save_search_image_record_port import (
    SaveSearchImageRecordPort,
)


class SearchImageService(SearchImageUseCase):
    def __init__(
        self,
        search_image_port: SearchImagePort,
        save_search_image_record_port: SaveSearchImageRecordPort,
    ) -> None:
        self.__search_image_port = search_image_port
        self.__save_search_image_record_port = save_search_image_record_port

    def search_image_by_clip_cosine_score(
        self, text_query: TextQuery
    ) -> SearchImageRecord:
        result_image = self.__search_image_port.search_image_by_clip_cosine_score(
            text_query=text_query
        )
        search_image_record_id = self.__save_search_image_record_port.save(
            SearchImageRecord(
                search_image_record_id=None,
                text_query=text_query,
                result_image=result_image,
            )
        )
        return SearchImageRecord(
            search_image_record_id=search_image_record_id,
            text_query=text_query,
            result_image=result_image,
        )

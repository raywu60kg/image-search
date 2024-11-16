from src.adapter.outward.persistence.search_image_record.search_image_record_mapper import (
    SearchImageRecordMapper,
)
from src.adapter.outward.persistence.search_image_record.search_image_record_repository import (
    SearchImageRecordRepository,
)
from src.app.domain.entity.search_image_record import (
    SearchImageRecord,
    SearchImageRecordId,
)
from src.app.port.outward.search_image_record.load_search_image_record_port import (
    LoadSearchImageRecordPort,
)
from src.app.port.outward.search_image_record.save_search_image_record_port import (
    SaveSearchImageRecordPort,
)


class SearchImageRecordPersistenceAdapter(
    LoadSearchImageRecordPort, SaveSearchImageRecordPort
):
    def __init__(
        self,
        search_image_record_mapper: SearchImageRecordMapper,
        search_image_record_repository: SearchImageRecordRepository,
    ) -> None:
        self.__search_image_record_mapper = search_image_record_mapper
        self.__search_image_record_repository = search_image_record_repository

    def minimal_load(
        self, search_image_record: SearchImageRecordId
    ) -> SearchImageRecord:
        search_image_record_sqlalchemy_model = (
            self.__search_image_record_repository.get_by_id(search_image_record.value)
        )
        return self.__search_image_record_mapper.map_to_minimal_search_image_record(
            search_image_record_sqlalchemy_model=search_image_record_sqlalchemy_model
        )

    def save(self, search_image_record: SearchImageRecord) -> SearchImageRecordId:
        search_image_record_sqlalchemy_model = self.__search_image_record_mapper.map_to_search_image_record_sqlalchemy_model(
            search_image_record=search_image_record
        )
        return SearchImageRecordId(
            self.__search_image_record_repository.save(
                search_image_record_sqlalchemy_model.search_image_record_sqlalchemy_model
            )
        )

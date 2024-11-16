from src.adapter.outward.persistence.search_image_record.search_image_record_exception import (
    MapToSearchImageRecordSqlalchemyModelException,
)
from src.adapter.outward.persistence.search_image_record.search_image_record_sqlalchemy_model import (
    SearchImageRecordSqlalchemyModel,
)
from src.app.domain.entity.embedding_strategy import DummyEmbedding
from src.app.domain.entity.search_image_record import (
    SearchImageRecord,
    SearchImageRecordId,
)
from src.app.domain.entity.text_query import TextQuery


class SearchImageRecordMapper:
    def map_to_minimal_search_image_record(
        self, search_image_record_sqlalchemy_model: SearchImageRecordSqlalchemyModel
    ) -> SearchImageRecord:
        return SearchImageRecord(
            search_image_record_id=SearchImageRecordId(
                search_image_record_sqlalchemy_model.id
            ),
            text_query=TextQuery(
                query=search_image_record_sqlalchemy_model.text_query,
                embedding_strategy=DummyEmbedding(),
            ),
            embedding_model=search_image_record_sqlalchemy_model.embedding_model,
            result_image=None,
        )

    def map_to_search_image_record_sqlalchemy_model(
        self, search_image_record: SearchImageRecord
    ) -> SearchImageRecordSqlalchemyModel:
        if search_image_record.result_image is None:
            raise MapToSearchImageRecordSqlalchemyModelException()
        return SearchImageRecordSqlalchemyModel(
            id=search_image_record.search_image_record_id
            if search_image_record.search_image_record_id is not None
            else None,
            text_query=search_image_record.text_query.query,
            embedding_model=search_image_record.embedding_model,
            result_image_id=search_image_record.result_image.image_id.value,
        )

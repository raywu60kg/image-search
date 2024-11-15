from typing import Callable

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.adapter.outward.persistence.search_image_record_exception import (
    SearchImageRecordNotFoundInDatabaseException,
)
from src.adapter.outward.persistence.search_image_record_sqlalchemy_model import (
    SearchImageRecordSqlalchemyModel,
)


class SearchImageRecordRepository:
    def __init__(self, session_factory: Callable[..., Session]):
        self.__session_factory = session_factory

    def get_by_id(
        self, search_image_record_id: int
    ) -> SearchImageRecordSqlalchemyModel:
        with self.__session_factory() as session:
            res = session.execute(
                select(SearchImageRecordSqlalchemyModel).where(
                    SearchImageRecordSqlalchemyModel.id == search_image_record_id
                )
            )

            search_image_record_sqlalchemy_model = res.scalar()
            if not search_image_record_sqlalchemy_model:
                raise SearchImageRecordNotFoundInDatabaseException(
                    search_image_record_id=search_image_record_id
                )
        return search_image_record_sqlalchemy_model

    def save(
        self, search_image_record_sqlalchemy_model: SearchImageRecordSqlalchemyModel
    ) -> SearchImageRecordSqlalchemyModel:
        with self.__session_factory() as session:
            session.add(search_image_record_sqlalchemy_model)
            session.commit()
        return search_image_record_sqlalchemy_model

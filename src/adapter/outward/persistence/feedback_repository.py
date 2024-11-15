from typing import Callable

from sqlalchemy.orm import Session

from src.adapter.outward.persistence.feedback_sqlalchemy_model import (
    FeedbackSqlalchemyModel,
)


class FeedbackRepository:
    def __init__(self, session_factory: Callable[..., Session]):
        self.__session_factory = session_factory

    def save(
        self, feedback_sqlalchemy_model: FeedbackSqlalchemyModel
    ) -> FeedbackSqlalchemyModel:
        with self.__session_factory() as session:
            session.add(feedback_sqlalchemy_model)
            session.commit()
        return feedback_sqlalchemy_model

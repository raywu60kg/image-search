from typing import Callable

import numpy as np
from numpy.typing import NDArray
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.adapter.outward.persistence.image.image_exception import (
    ImageNotFoundInDatabaseException,
)
from src.adapter.outward.persistence.image.image_sqlalchemy_model import (
    ImageSqlalchemyModel,
)
from src.app.domain.entity.embedding_strategy import EmbeddingModelEnum


class ImageRepository:
    def __init__(self, session_factory: Callable[..., Session]):
        self.__session_factory = session_factory

    def get_by_clip_cosine_score(
        self, text_query_vector: NDArray[np.float32]
    ) -> ImageSqlalchemyModel:
        with self.__session_factory() as session:
            res = session.scalars(
                select(ImageSqlalchemyModel)
                .order_by(
                    ImageSqlalchemyModel.image_embedding.cosine_distance(
                        text_query_vector.tolist()
                    )
                )
                .where(ImageSqlalchemyModel.image_embedding == EmbeddingModelEnum.CLIP)
                .limit(1)
            )
        return res.one()

    def get_by_id(self, image_id: int) -> ImageSqlalchemyModel:
        with self.__session_factory() as session:
            res = session.execute(
                select(ImageSqlalchemyModel)
                .where(ImageSqlalchemyModel.id == image_id)
                .limit(1)
            )
            image_sqlalchemy_model = res.scalar()
            if not image_sqlalchemy_model:
                raise ImageNotFoundInDatabaseException(image_id=image_id)
        return image_sqlalchemy_model

from typing import Callable

import numpy as np
from numpy.typing import NDArray
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.adapter.outward.persistence.image_sqlalchemy_model import ImageSqlalchemyModel


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
                .limit(1)
            )
        return res.one()

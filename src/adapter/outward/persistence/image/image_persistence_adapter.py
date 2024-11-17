from functools import lru_cache

from src.adapter.outward.persistence.image.image_mapper import ImageMapper
from src.adapter.outward.persistence.image.image_repository import ImageRepository
from src.app.domain.entity.image import ImageEntity
from src.app.domain.entity.text_query import TextQuery
from src.app.port.outward.image.search_image_port import SearchImagePort


class ImagePersistenceAdapter(SearchImagePort):
    def __init__(
        self,
        image_mapper: ImageMapper,
        image_repository: ImageRepository,
    ) -> None:
        self.__image_mapper = image_mapper
        self.__image_repository = image_repository

    @lru_cache(128)
    def search_image_by_clip_cosine_score(self, text_query: TextQuery) -> ImageEntity:  # type: ignore
        image_sqlalchemy_model = self.__image_repository.get_by_clip_cosine_score(
            text_query.query_embedding
        )
        return self.__image_mapper.map_to_image(
            image_sqlalchemy_model=image_sqlalchemy_model
        )

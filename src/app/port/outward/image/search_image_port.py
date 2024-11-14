from abc import ABC, abstractmethod

from src.app.domain.entity.image import ImageEntity
from src.app.domain.entity.text_query import TextQuery


class SearchImagePort(ABC):
    @abstractmethod
    def search_image_by_clip_cosine_score(self, text_query: TextQuery) -> ImageEntity:
        pass

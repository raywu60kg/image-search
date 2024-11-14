from abc import ABC, abstractmethod

from src.app.domain.entity.search_image_record import SearchImageRecord
from src.app.domain.entity.text_query import TextQuery


class SearchImageUseCase(ABC):
    @abstractmethod
    def search_image(self, query: TextQuery) -> SearchImageRecord:
        pass

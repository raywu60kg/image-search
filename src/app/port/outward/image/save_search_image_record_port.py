from abc import ABC, abstractmethod

from src.app.domain.entity.search_image_record import SearchImageRecord


class SaveSearchImageRecordPort(ABC):
    @abstractmethod
    def save(self, search_image_record: SearchImageRecord) -> SearchImageRecord:
        pass

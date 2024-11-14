from abc import ABC, abstractmethod

from src.app.domain.entity.search_image_record import (
    SearchImageRecord,
    SearchImageRecordId,
)


class LoadSearchImageRecordPort(ABC):
    @abstractmethod
    def load(self, search_image_record: SearchImageRecordId) -> SearchImageRecord:
        pass

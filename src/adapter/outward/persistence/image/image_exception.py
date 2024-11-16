from src.common.exception import ImageSearchApiError


class ImageNotFoundInDatabaseException(ImageSearchApiError):
    def __init__(self, image_id: int) -> None:
        self.message = f"image_id: {image_id} not found!"
        super().__init__(self.message)

from src.app.domain.entity.embedding_strategy import EmbeddingModelEnum


class ImageId:
    def __init__(self, value: int) -> None:
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value


class ImageEntity:
    def __init__(
        self,
        image_id: ImageId,
        base64_image: str,
        embedding_model: EmbeddingModelEnum,
    ):
        self.__image_id = image_id
        self.__base64_image = base64_image
        self.__embedding_model = embedding_model

    @property
    def image_id(self) -> ImageId:
        return self.__image_id

    @property
    def base64_image(self) -> str:
        return self.__base64_image

    @property
    def embedding_model(self) -> EmbeddingModelEnum:
        return self.__embedding_model

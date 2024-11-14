class ImageId:
    def __init__(self, value: int) -> None:
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value


class ImageEntity:
    def __init__(self, image_id: ImageId | None, base64_image: str):
        self.__image_id = image_id
        self.__base64_image: str

    @property
    def image_id(self) -> ImageId | None:
        return self.__image_id

    @property
    def base64_image(self) -> str:
        return self.__base64_image
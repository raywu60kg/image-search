from src.adapter.outward.persistence.image.image_sqlalchemy_model import (
    ImageSqlalchemyModel,
)
from src.app.domain.entity.image import ImageEntity, ImageId


class ImageMapper:
    def map_to_image(self, image_sqlalchemy_model: ImageSqlalchemyModel) -> ImageEntity:
        return ImageEntity(
            image_id=ImageId(image_sqlalchemy_model.id),
            base64_image=image_sqlalchemy_model.image_base64,
            embedding_model=image_sqlalchemy_model.embedding_model,
        )

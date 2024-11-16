from sqlalchemy import Enum, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from pgvector.sqlalchemy import Vector  # type: ignore
from src.adapter.outward.persistence.database import Base
from src.app.domain.entity.embedding_strategy import EmbeddingModelEnum


class ImageSqlalchemyModel(Base):
    __tablename__ = "image"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    image_base64: Mapped[str] = mapped_column(Text, nullable=True)
    image_embedding = mapped_column(Vector(512), nullable=False)  # type: ignore
    embedding_model: Mapped[EmbeddingModelEnum] = mapped_column(
        Enum(EmbeddingModelEnum),
        nullable=False,
        default=EmbeddingModelEnum.CLIP,
    )

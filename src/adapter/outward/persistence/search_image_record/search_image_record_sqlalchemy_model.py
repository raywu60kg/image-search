from sqlalchemy import Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.adapter.outward.persistence.database import Base
from src.app.domain.entity.embedding_strategy import EmbeddingModelEnum


class SearchImageRecordSqlalchemyModel(Base):
    __tablename__ = "search_image_record"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text_query: Mapped[str] = mapped_column(String, nullable=False)
    embedding_model: Mapped[EmbeddingModelEnum] = mapped_column(
        Enum(EmbeddingModelEnum),
        nullable=False,
        default=EmbeddingModelEnum.CLIP,
    )
    result_image_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("image.id"), nullable=False
    )

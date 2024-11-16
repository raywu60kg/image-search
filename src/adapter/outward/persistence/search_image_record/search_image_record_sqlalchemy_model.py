from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.adapter.outward.persistence.database import Base


class SearchImageRecordSqlalchemyModel(Base):
    __tablename__ = "search_image_record"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text_query: Mapped[str] = mapped_column(String, nullable=False)

    result_image_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("image.id"), nullable=False
    )

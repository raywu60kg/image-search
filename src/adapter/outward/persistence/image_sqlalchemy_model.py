from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.adapter.outward.persistence.database import Base


class ImageSqlalchemyModel(Base):
    __tablename__ = "image"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    image_base64: Mapped[str] = mapped_column(Text, nullable=True)

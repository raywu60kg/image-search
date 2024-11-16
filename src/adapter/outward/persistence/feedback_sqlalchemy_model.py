from sqlalchemy import Enum, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.adapter.outward.persistence.database import Base
from src.app.domain.entity.feedback import FeedbackEnum


class FeedbackSqlalchemyModel(Base):
    __tablename__ = "feedback"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    feedback: Mapped[FeedbackEnum] = mapped_column(
        Enum(FeedbackEnum),
        nullable=False,
        default=FeedbackEnum.GOOD,
    )
    search_image_record_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("search_image_record.id"), nullable=False
    )

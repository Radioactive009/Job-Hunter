from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class JobMatch(Base):
    __tablename__ = "job_matches"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    job_id: Mapped[int] = mapped_column(
        ForeignKey("jobs.id"),
        nullable=False
    )

    match_score: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    semantic_score: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    skill_score: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    experience_score: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    location_score: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    recommendation: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
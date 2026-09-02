from datetime import datetime

from sqlalchemy import (
    String,
    Text,
    Integer,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    location: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    remote_type: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    employment_type: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    experience_level: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    salary_min: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    salary_max: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    currency: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True
    )

    url: Mapped[str] = mapped_column(
        String(1000),
        unique=True,
        nullable=False
    )

    source: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    posted_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    scraped_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    company = relationship("Company")
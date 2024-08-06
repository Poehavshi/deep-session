from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base

from .enum import TaskStatus


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[TaskStatus] = mapped_column(nullable=False, default=TaskStatus.PENDING)
    time_spent: Mapped[int] = mapped_column(nullable=False, default=0)
    start_time: Mapped[datetime] = mapped_column(DateTime, default=None, nullable=True)
    end_time: Mapped[datetime] = mapped_column(DateTime, default=None, nullable=True)

from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(nullable=False)
    done: Mapped[bool] = mapped_column(nullable=False, default=False)

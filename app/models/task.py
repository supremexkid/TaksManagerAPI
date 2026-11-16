from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from app.database import Base

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None]
    status: Mapped[str] = mapped_column(default="todo")
    priority: Mapped[str] = mapped_column(default = "medium")
    due_date: Mapped[datetime | None] =  mapped_column()
    created_at:  Mapped[datetime] = mapped_column(
        server_default=func.now()

    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )

# здесь Pydantic-схемы (валидация)
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class TaskBase(BaseModel):
    title: str= Field(max_length=100)
    description: str | None = None
    priority: str = "Medium"
    due_date: datetime | None = None

class TaskCreate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
    status: str = "todo"
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

class TaskUpdate(TaskBase):
    title: str | None = None
    description: str | None = None
    priority: str | None = None
    due_date: datetime | None = None



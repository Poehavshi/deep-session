from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from .enum import TaskStatus


class TaskBase(BaseModel):
    text: str
    status: TaskStatus


class TaskCreate(TaskBase):
    status: TaskStatus = TaskStatus.PENDING


class TaskUpdate(TaskBase):
    text: Optional[str] = Field(None)
    status: Optional[TaskStatus] = Field(None)


class TaskRead(TaskBase):
    id: int
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    time_spent: int

    class Config:
        orm_mode = True

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    text: str
    done: bool


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    text: str | None = Field(None)
    done: bool | None = Field(None)


class TaskRead(TaskBase):
    id: int

    class Config:
        orm_mode = True

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from .models import Task
from .schemas import TaskCreate, TaskUpdate


async def create_task_in_db(db: AsyncSession, task: TaskCreate):
    task = Task(**task.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def get_task(db: AsyncSession, task_id: int):
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalars().first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


async def get_tasks(db: AsyncSession):
    result = await db.execute(select(Task))
    return result.scalars().all()


async def update_task_in_db(db: AsyncSession, task_id: int, task_update: TaskUpdate):
    task = await get_task(db, task_id)
    for key, value in task_update.dict().items():
        if value is None:
            continue
        setattr(task, key, value)
    await db.commit()
    await db.refresh(task)
    return task


async def delete_task_in_db(db: AsyncSession, task_id: int):
    task = await get_task(db, task_id)
    await db.delete(task)
    await db.commit()

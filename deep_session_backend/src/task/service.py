from datetime import datetime

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from .enum import TaskStatus
from .models import Task
from .schemas import TaskCreate, TaskUpdate


async def create_task_in_db(db: AsyncSession, task: TaskCreate) -> Task:
    db_task = Task(
        text=task.text,
        status=task.status
    )
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task


async def get_task(db: AsyncSession, task_id: int):
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalars().first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


async def get_tasks(db: AsyncSession):
    result = await db.execute(select(Task))
    return result.scalars().all()


async def update_task_in_db(db: AsyncSession, task_id: int, task: TaskUpdate) -> Task:
    db_task = await db.get(Task, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.text is not None:
        db_task.text = task.text
    if task.status is not None:
        db_task.status = task.status
        if task.status == TaskStatus.DONE:
            db_task.end_time = datetime.utcnow()
            if db_task.start_time:
                db_task.time_spent = int((db_task.end_time - db_task.start_time).total_seconds())
        if task.status == TaskStatus.IN_WORK:
            db_task.start_time = datetime.utcnow()
    await db.commit()
    await db.refresh(db_task)
    return db_task


async def delete_task_in_db(db: AsyncSession, task_id: int):
    task = await get_task(db, task_id)
    await db.delete(task)
    await db.commit()

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from .schemas import TaskCreate, TaskUpdate, TaskRead
from .service import create_task_in_db, get_task, get_tasks, update_task_in_db, delete_task_in_db

tasks_router = APIRouter()


@tasks_router.post("/", response_model=TaskRead, status_code=201)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    task = await create_task_in_db(db, task)
    return task


@tasks_router.get("/", response_model=list[TaskRead])
async def read_tasks(db: AsyncSession = Depends(get_db)):
    return await get_tasks(db)


@tasks_router.get("/{task_id}", response_model=TaskRead)
async def read_task(task_id: int, db: AsyncSession = Depends(get_db)):
    return await get_task(db, task_id)


@tasks_router.patch("/{task_id}", response_model=TaskRead)
async def update_task(task_id: int, task: TaskUpdate, db: AsyncSession = Depends(get_db)):
    return await update_task_in_db(db, task_id, task)


@tasks_router.delete("/{task_id}", status_code=204)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    await delete_task_in_db(db, task_id)

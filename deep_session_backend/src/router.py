from .task.router import tasks_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(tasks_router, prefix="/tasks", tags=["tasks"])

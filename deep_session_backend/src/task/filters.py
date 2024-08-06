from fastapi_filter.contrib.sqlalchemy import Filter
from .models import Task
from .enum import TaskStatus


class TaskFilter(Filter):
    status: TaskStatus | None = None

    class Constants(Filter.Constants):
        model = Task

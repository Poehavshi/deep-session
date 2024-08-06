import enum


class TaskStatus(enum.Enum):
    PENDING = "pending"
    IN_WORK = "in_work"
    DONE = "done"

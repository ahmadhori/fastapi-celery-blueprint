from typing import Any, List, Optional

from pydantic import BaseModel


class TaskResult(BaseModel):
    current: int | None
    total: int | None
    status: str


class AsyncTask(BaseModel):
    id: str
    name: Optional[str]
    args: Optional[List[Any]]
    state: Optional[str]
    result: TaskResult | None

    class Config:
        orm_mode = True


class CeleryTasks(BaseModel):
    scheduled: List[AsyncTask]
    running: List[AsyncTask]
    reserved: List[AsyncTask]

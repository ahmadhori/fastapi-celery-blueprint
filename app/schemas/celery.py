from typing import Any, List, Optional

from pydantic import BaseModel


class TaskResult(BaseModel):
    current: Optional[int]
    total: Optional[int]
    logs: Optional[List[str]]
    final_status: Optional[str]


class AsyncTask(BaseModel):
    id: str
    name: Optional[str]
    args: Optional[List[Any]]
    state: Optional[str]
    result: Optional[TaskResult]

    class Config:
        orm_mode = True


class CeleryTasks(BaseModel):
    scheduled: List[AsyncTask]
    running: List[AsyncTask]
    reserved: List[AsyncTask]

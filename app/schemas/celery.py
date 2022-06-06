from typing import Any, List, Optional

from pydantic import BaseModel


class AsyncTask(BaseModel):
    id: str
    args: Optional[List[Any]]
    name: Optional[str]
    msg: Optional[str]

    class Config:
        orm_mode = True


class CeleryTasks(BaseModel):
    scheduled: List[AsyncTask]
    running: List[AsyncTask]
    reserved: List[AsyncTask]

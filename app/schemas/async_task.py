from typing import Optional

from pydantic import BaseModel


class AsyncTask(BaseModel):
    task_id: Optional[str]

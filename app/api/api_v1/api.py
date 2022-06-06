from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, tasks, users

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(items.router, prefix="/items", tags=["items"])

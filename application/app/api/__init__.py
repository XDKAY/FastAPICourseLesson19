from fastapi import APIRouter

from .docs import router as docs_router
from .user import router as user_router

api_routers = APIRouter(prefix="/api")
api_routers.include_router(docs_router)
api_routers.include_router(user_router)

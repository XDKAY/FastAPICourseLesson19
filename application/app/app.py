from fastapi import FastAPI

from application.app.api import api_routers

app = FastAPI(
    docs_url=None,
    openapi_url=None,
    redoc_url=None,
)
app.state.routers = app.routes
app.include_router(api_routers)

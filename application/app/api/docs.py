from fastapi import APIRouter, Depends, Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse

from application.app.auth.docs import auth_docs
from application.app.dependencies.guard import production

router = APIRouter(
    dependencies=[Depends(production), Depends(auth_docs)]
)


@router.get("/docs", response_class=HTMLResponse, include_in_schema=False)
def docs_endpint():
    return get_swagger_ui_html(
        openapi_url="/api/openapi.json",
        title="FastAPI"
    )


@router.get("/openapi.json", include_in_schema=False)
def openapi_endpoint(request: Request) -> dict:
    return get_openapi(
        title="FastAPI",
        version="0.1.0",
        routes=request.app.state.routers,
    )

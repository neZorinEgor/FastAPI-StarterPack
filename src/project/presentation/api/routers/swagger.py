from fastapi import APIRouter, Request
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.responses import HTMLResponse

router = APIRouter(include_in_schema=False)


@router.get("/docs")
async def custom_swagger_ui_html(request: Request):
    return get_swagger_ui_html(
        openapi_url=request.app.openapi_url,  # "/openapi.json",
        title=request.app.title + " - Swagger UI",
        oauth2_redirect_url=request.app.swagger_ui_oauth2_redirect_url,
        swagger_js_url=str(request.url_for("static", path="/js/swagger-ui-bundle.js")),
        swagger_css_url=str(request.url_for("static", path="/css/swagger-ui.css")),
    )


@router.get("/docs/oauth2-redirect")
async def swagger_ui_redirect() -> HTMLResponse:
    return get_swagger_ui_oauth2_redirect_html()


@router.get("/redoc")
async def redoc_html(request: Request) -> HTMLResponse:
    return get_redoc_html(
        openapi_url=request.app.openapi_url,
        title=request.app.title + " - ReDoc",
        redoc_js_url=str(request.url_for("static", path="/js/redoc.standalone.js")),
    )

from http.client import HTTPResponse
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.api_v1.router import api_router

app = FastAPI(title=settings.PROJECT_NAME,
              openapi_url=f"{settings.API_V1_STR}/openapi.json")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/", response_class=HTTPResponse)
async def report(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/report", response_class=HTTPResponse)
async def report(request: Request):
    return templates.TemplateResponse("report.html", {"request": request})


@app.get("/ocr", response_class=HTTPResponse)
async def ocr(request: Request):
    return templates.TemplateResponse("ocr.html", {"request": request})


@app.get("/yd", response_class=HTTPResponse)
async def yd(request: Request):
    return templates.TemplateResponse("yd.html", {"request": request})

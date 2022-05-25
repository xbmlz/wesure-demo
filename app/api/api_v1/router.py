from fastapi import APIRouter

from app.api.api_v1.endpoints import hello, ocr

api_router = APIRouter()

api_router.include_router(hello.router, tags=["hello"])

api_router.include_router(ocr.router, tags=["ocr"])

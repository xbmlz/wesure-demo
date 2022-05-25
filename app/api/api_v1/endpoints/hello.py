from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()


@router.get("/hello/")
def hello() -> str:
    """
    Test access token
    """
    return "hello"

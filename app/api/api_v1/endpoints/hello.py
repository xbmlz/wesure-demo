from fastapi import APIRouter

router = APIRouter()


@router.get("/hello/")
def hello() -> str:
    """
    Test access token
    """
    return "hello"

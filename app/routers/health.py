from fastapi import APIRouter

router = APIRouter(tags=["Health Check"])


@router.get("/")
def health_check():
    return {"status": "200 OK :)"}

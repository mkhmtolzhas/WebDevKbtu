from fastapi import APIRouter
from .v1.router import router as v1_router


router = APIRouter(prefix="/api")

@router.get("/ping")
async def ping():
    return {"ping": "pong"}

router.include_router(v1_router)

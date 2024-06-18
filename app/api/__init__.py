from fastapi import APIRouter

from .chatbot.controllers.routers import router as chatbot_router


router = APIRouter(prefix='/api/v1', tags=['API'])
router.include_router(chatbot_router)

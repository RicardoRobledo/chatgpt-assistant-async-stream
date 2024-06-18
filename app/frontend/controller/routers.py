from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app import config


__author__ = "Ricardo Robledo"
__version__ = "1.0"


router = APIRouter(prefix='/frontend')

templates = Jinja2Templates(directory='app/frontend/frontend_templates/templates')


@router.get('/index')
async def get_home(request:Request):
    return templates.TemplateResponse('index.html', {'request': request})

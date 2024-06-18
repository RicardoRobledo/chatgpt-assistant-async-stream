from fastapi import APIRouter, Request, Body, status
from fastapi.responses import StreamingResponse, JSONResponse

from ..services import chatbot_service
from ..desing_patterns.creational_patterns.singleton.openai_singleton import OpenAISingleton


__author__ = 'Ricardo Robledo'
__version__ = '1.0'


router = APIRouter(prefix='/chatbot', tags=['chatbot'])


@router.post('/message', status_code=status.HTTP_200_OK)
async def send_message(body:dict=Body(...)):

    thread_id = body.get('thread_id')
    user_message = body.get('user_message')

    await chatbot_service.send_message(thread_id, user_message)

    return StreamingResponse(OpenAISingleton.answer(thread_id))


@router.get('/thread_id')
async def create_thread(request:Request):

    thread_id = await OpenAISingleton.create_thread()

    return JSONResponse(content={'thread_id':thread_id.id})


@router.post('/thread_id/{thread_id}')
async def delete_thread(thread_id:str):

    await OpenAISingleton.delete_thread(thread_id)

    return JSONResponse(content={})

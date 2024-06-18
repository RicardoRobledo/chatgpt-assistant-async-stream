from ..repositories import chatbot_repository


async def send_message(thread_id:str, message:str):
    return await chatbot_repository.send_message(thread_id, message)

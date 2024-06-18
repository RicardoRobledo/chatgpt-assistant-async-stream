from openai import AsyncOpenAI

from app import config
from app.api.chatbot.events import EventHandler


__author__ = 'Ricardo'
__version__ = '1.0'


class OpenAISingleton():


    __client = None


    @classmethod
    def __get_connection(self):
        """
        This method create our client and give us a new thread
        """
        
        client = AsyncOpenAI(api_key=config.OPENAI_API_KEY,)

        return client


    def __new__(cls, *args, **kwargs):
        
        if cls.__client==None:

            # making connection
            cls.__client = cls.__get_connection()
        
        return cls.__client
    

    @classmethod
    async def create_thread(cls):
        """
        This method create a new thread

        :return: thread_id
        """
        return await cls.__client.beta.threads.create()
    

    @classmethod
    async def delete_thread(cls, thread_id:str):
        """
        This method delete a thread

        :param:
        """
        return await cls.__client.beta.threads.delete(thread_id)


    @classmethod
    async def create_message(cls, thread_id:str, message:str):
        """
        This method create a new message in the assistant
        """

        await cls.__client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=message
        )


    @classmethod
    async def answer(cls, thread_id:str):
        """
        This method return the answer from the assistant
        """

        async with cls.__client.beta.threads.runs.stream(
            thread_id=thread_id,
            assistant_id=config.ASSISTANT_ID,
            event_handler=EventHandler(),
        ) as stream:
        
            async for text in stream.text_deltas:
                yield text
    

    @classmethod
    async def create_conversation_thread(cls):
        """
        Make up a thread converation
        """

        return cls.__client.beta.threads.create()


    @classmethod
    async def delete_conversation_thread(cls, thread_id):
        """
        Remove a thread converation

        :param thread: an string being our thread identifier
        """

        cls.__client.beta.threads.delete(thread_id)

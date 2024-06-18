from typing_extensions import override
from openai import AsyncAssistantEventHandler


__author__ = 'Ricardo Robledo'
__version__ = '1.0'


class EventHandler(AsyncAssistantEventHandler):

    @override
    async def on_text_created(self, text) -> None:
        print(f'\nassistant > ', end='', flush=True)

    @override
    async def on_text_delta(self, delta, snapshot):
        print(delta.value, end='', flush=True)

    async def on_tool_call_created(self, tool_call):
        print(f'\nassistant > {tool_call.type}\n', flush=True)

    async def on_tool_call_delta(self, delta, snapshot):

        if delta.type=='code_interpreter':
        
            if delta.code_interpreter.input:
                print(delta.code_interpreter.input, end='', flush=True)
        
        if delta.code_interpreter.outputs:
        
            print(f'\n\noutput >', flush=True)
        
            for output in delta.code_interpreter.outputs:
        
                if output.type == 'logs':
                    print(f'\n{output.logs}', flush=True)

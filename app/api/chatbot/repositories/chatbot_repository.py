from ..desing_patterns.creational_patterns.singleton.openai_singleton import OpenAISingleton
from ..desing_patterns.creational_patterns.singleton.google_sheets_singleton import GoogleSheetSingleton

import pandas as pd
from tabulate import tabulate


async def send_message(thread_id:str, message:str):

    result = await GoogleSheetSingleton.read_google_sheets()

    df = pd.DataFrame(result)

    markdown_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)

    message = f'''
    Lo siguiente es un tablero con las quejas que se han registrado hasta el momento:

    {markdown_table}

    responde la pregunta del usuario en base a ellas:{message}
    '''

    return await OpenAISingleton.create_message(thread_id, message)

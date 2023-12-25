from openai import AsyncOpenAI
import time
import os
from dotenv import load_dotenv
import re

load_dotenv()

client = AsyncOpenAI(
  api_key=os.environ['API_KEY']  
)

async def IA_consulta():
    #promt

    promt="Generame 3 preguntas con su respuesta sobre Alejandro Magno"

    print(promt)


# guia de github : https://github.com/openai/openai-python/discussions/742
    start_time = time.time()

    response = await client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": promt}])

    end_time = time.time()

    print("Tiempo de ejecucion: ", end_time - start_time , " segundos")

    
    respuesta_generada = response.choices[0].message.content

    print(response.choices[0].message.content)
  
    respuesta={
        "respuesta":respuesta_generada,
        "time": end_time - start_time
    }

    return respuesta

    







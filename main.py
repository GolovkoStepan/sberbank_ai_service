from typing import Union
from fastapi import FastAPI
from gpt_generator import GptGenerator

generator = GptGenerator()
app = FastAPI()


@app.get("/generate")
async def generate(message: Union[str, None] = None):
    if message is None or message == "":
        return {"status": "error", "message": "Param message is not present"}
    else:
        return {"status": "ok", "answer": generator.generate(message)}

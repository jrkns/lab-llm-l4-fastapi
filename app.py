import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from openai import AsyncOpenAI


load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

###########
# Models #
########################################################################################


class GrammarTaskRequest(BaseModel):
    text: str
    style: Optional[str] = "default"


class GrammarTaskResponse(BaseModel):
    text: str


###########
# Routers #
########################################################################################


@app.get("/")
async def health_check():
    return {"status": "ok", "version": "1.0.0"}


@app.post("/openai/grammar")
async def openai_grammar(request: GrammarTaskRequest) -> GrammarTaskResponse:
    # TODO: write logic codes
    return {"text": "TODO"}

########################################################################################

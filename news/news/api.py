from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import httpx
import asyncio

router = APIRouter()

class InputRequest(BaseModel):
    input: str

class InputResponse(BaseModel):
    response: str

Url = "http://httpbin.org/uuid"

def api() -> APIRouter:

    @router.post("/input", response_model=InputResponse)
    async def input(request: InputRequest) -> InputResponse:
        """
        Manual input news source
        """

        resp = await gpt_request()
        return InputResponse(response=resp)
    return router

async def gpt_request():
    async with httpx.AsyncClient() as client:
        response = await client.get(Url)
        return response.text


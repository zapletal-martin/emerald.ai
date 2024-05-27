from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()

class InputRequest(BaseModel):
    input: str

class InputResponse(BaseModel):
    response: str

def api() -> APIRouter:

    @router.post("/input", response_model=InputResponse)
    def input(request: InputRequest) -> InputResponse:
        """
        Manual input news source
        """

        return InputResponse(response="Ok")

    return router


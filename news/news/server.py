import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette.middleware.cors import CORSMiddleware

from news.api import api

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api())

def start():
    uvicorn.run("news.server:app", host="0.0.0.0", port=8087, reload=True)


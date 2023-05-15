from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai import openai_api 

app = FastAPI()

origins = [
    "https://personal-ai.run.goorm.site/",
    "http://localhost",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(openai_api.router)

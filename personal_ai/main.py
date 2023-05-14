from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

import requests, json

# for testing
@app.get("/")
def run_pipdream():
    URL = "https://eodaykl2oenbq4j.m.pipedream.net"
    data = {'outer': {'inner': 'value'}}
    res = requests.post(URL, data=json.dumps(data))
    return 0
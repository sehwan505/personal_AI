import requests, json
import openai
from fastapi import APIRouter
from .pinecone_api import appending_shots
from util import config

openai.api_key = config["OPENAI_KEY"]

router = APIRouter(
    prefix="/api/openai",
)

@router.get("/list")
def get_models():
    URL = "https://eodaykl2oenbq4j.m.pipedream.net"
    res = requests.post(URL)
    return 0

@router.get("/save_prompting/{prompt}")
def save_prompting(prompt: str):
    URL = "https://eodaykl2oenbq4j.m.pipedream.net"
    data = {"data": {"prompt": prompt}}
    res = requests.post(URL, data=json.dumps(data))
    return 0

@router.get("/chat/{prompt}")
def chat(prompt: str):
    augmented_prompt = appending_shots(prompt)
    system_msg=  f"""You are a helpul tutor. Answer questions only based on the context provided, or say I don't know."""
    chat = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_msg},
        {"role": "user", "content": prompt}
    ]
    )
    return chat
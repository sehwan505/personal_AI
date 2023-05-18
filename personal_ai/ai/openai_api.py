import requests, json
import openai
from fastapi import APIRouter
from pinecone_api import loading_previous_answers
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
    return res.json()

@router.get("/chat/{prompt}")
def chat(prompt: str):
    augmented_prompt = appending_shots(prompt)
    system_msg=  f"""You are a helpul machine learning assistant and tutor. Answer questions based on the context provided, or say I don't know."""
    chat = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_msg},
        {"role": "user", "content": prompt}
    ]
    )
    return chat

import requests, json

from fastapi import APIRouter

router = APIRouter(
    prefix="/api/openai",
)


@router.get("/list")
def get_models():
    URL = "https://eodaykl2oenbq4j.m.pipedream.net"
    res = requests.post(URL)
    return 0

@router.get("/prompting/{prompt}")
def prompting(prompt: str):
    URL = "https://eodaykl2oenbq4j.m.pipedream.net"
    data = {"data": {"prompt": prompt}}
    res = requests.post(URL, data=json.dumps(data))
    return res
FROM python:3.10.6

RUN pip install poetry
# /code 폴더 만들기
WORKDIR /code

# 이제 app 에 있는 파일들을 /code/app 에 복사
COPY . /code
RUN poetry install

WORKDIR /code/personal_ai


# 실행
CMD ["poetry", "run", "uvicorn", "personal_ai.main:app", "--host", "0.0.0.0", "--port", "80"]
FROM python:3

WORKDIR /app

COPY ./pyproject.toml .

RUN poetry install -r pyproject.toml

COPY . .


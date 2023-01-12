FROM python:3.11-alpine

COPY ./app /app

COPY ./requirements.txt /tmp/requirements.txt

WORKDIR /app

EXPOSE 5000

RUN apk add gcc python3-dev

RUN python -m pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

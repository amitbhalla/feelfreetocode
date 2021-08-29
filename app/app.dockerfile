FROM python:3.9.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY ./app/requirements.txt requirements.txt 

RUN apk add --update --no-cache jpeg-dev mariadb-connector-c-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers musl-dev zlib zlib-dev

RUN pip install -r requirements.txt

RUN apk del .tmp-build-deps

RUN adduser -D user
USER user

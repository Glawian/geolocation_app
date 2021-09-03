FROM python:3.9.6

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app

COPY . /app/

EXPOSE 80

FROM python:3.11-slim

WORKDIR /Clinic_service

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /Clinic_service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Clinic_service/requirements.txt

RUN apt-get update && apt-get install -y curl

COPY ./main.py /Clinic_service/main.py
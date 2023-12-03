FROM python:3.11-slim

WORKDIR /Clinic_service

COPY ./requirements.txt /Clinic_service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Clinic_service/requirements.txt

COPY ./main.py /Clinic_service/main.py

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5555"]
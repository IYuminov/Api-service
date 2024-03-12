FROM python:3.11-slim

WORKDIR /Clinic_service

COPY ./requirements.txt /Clinic_service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Clinic_service/requirements.txt

RUN apt-get update && apt-get install -y wget curl

COPY ./main.py /Clinic_service/main.py

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5555"]

HEALTHCHECK --interval=5s --timeout=10s CMD curl -f http://localhost:5555/health || exit 1
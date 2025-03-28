FROM python:3.9-slim

WORKDIR /app

COPY backend.py .

RUN pip install fastapi[all] elasticsearch

CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8500"]
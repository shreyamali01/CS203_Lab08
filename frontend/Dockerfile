FROM python:3.9-slim

WORKDIR /app

COPY app.py /app/app.py

RUN pip install fastapi uvicorn

EXPOSE 9567

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9567"]
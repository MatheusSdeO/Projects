FROM python:3.11-slim

WORKDIR /app

COPY . .

EXPOSE 8000

CMD ["python", "atv01.py"]

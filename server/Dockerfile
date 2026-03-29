FROM python:3.9-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
# This starts the FastAPI server so the logs stay open
CMD ["python", "server/app.py"]
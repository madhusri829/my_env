FROM python:3.9-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Use Port 7860 for Hugging Face
EXPOSE 7860
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
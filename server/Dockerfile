FROM python:3.9-slim
WORKDIR /app
# Force logs to appear immediately
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Hugging Face likes port 7860 for health checks
EXPOSE 7860
# Run the server on port 7860
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
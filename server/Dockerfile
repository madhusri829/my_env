FROM python:3.9-slim

WORKDIR /app

# Force Python to show logs immediately
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Open port 8000 for the grader
EXPOSE 8000

# Start the server using the module path
CMD ["python", "-m", "uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000"]
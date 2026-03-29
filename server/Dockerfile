FROM python:3.9-slim

WORKDIR /app

# This makes logs show up immediately in Hugging Face
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Open the port for the OpenEnv grader
EXPOSE 8000

# Start the server
CMD ["python", "server/app.py"]
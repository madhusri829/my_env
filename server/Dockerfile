FROM python:3.9-slim

WORKDIR /app

# Prevent logs from being buffered (so they show up immediately)
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# EXPOSE port 8000 for the OpenEnv grader
EXPOSE 8000

# IMPORTANT: Run the server, not just the test script
# This keeps the container "Running" so the grader can check it
CMD ["python", "server/app.py"]

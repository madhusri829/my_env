FROM python:3.9-slim

WORKDIR /app

# Force logs to show up immediately
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Open the port Hugging Face expects
EXPOSE 7860

# Run the server on port 7860
CMD ["python", "-m", "uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
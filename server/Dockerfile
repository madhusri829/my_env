FROM python:3.9-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port for Hugging Face and the Grader
EXPOSE 8000

# IMPORTANT: Run the server, NOT inference.py
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000"]
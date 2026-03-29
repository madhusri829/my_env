FROM python:3.9-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
# This is the most stable way to start the server
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000"]
FROM python:3.10-slim
WORKDIR /app
# Force logs to show up immediately
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
# Install dependencies fast
COPY requirements.txt .
RUN pip install --no-cache-dir gymnasium fastapi uvicorn
# Copy code
COPY . .
# Use Port 7860 (Official Hugging Face Port)
EXPOSE 7860
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
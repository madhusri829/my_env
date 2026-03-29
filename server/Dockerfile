# 1. Use a lightweight Python image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Prevent Python from buffering logs (makes logs appear instantly)
ENV PYTHONUNBUFFERED=1
# Ensure the current directory is in the Python path
ENV PYTHONPATH=/app

# 4. Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# 5. Install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy all your project files into the container
COPY . .

# 7. Open port 8000 (standard for the OpenEnv server)
EXPOSE 8000

# 8. Run the inference script to show the simulation in logs
# Note: OpenEnv's automated grader will also look for the server/app.py
CMD ["python", "inference.py"]

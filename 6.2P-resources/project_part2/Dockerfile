# Use the official Python image from the Docker repository
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies and clear the cache to keep the image size smaller
RUN pip install --no-cache-dir -r requirements.txt && rm -rf /root/.cache/pip

# Copy the entire application code into the container
COPY . .

# Set the environment variable for FastAPI
ENV PORT=8000

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Command to run the application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

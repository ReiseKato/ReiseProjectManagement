# Use the official Python image as a base
FROM python:3.11-slim

# Set a working directory in the container
WORKDIR /app

# Copy the requirements file first (to take advantage of Docker layer caching)
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your app runs on (change if your app uses a different port)
EXPOSE 5000

# Command to run your Python backend (update as needed for your framework)
CMD ["python", "main.py"]

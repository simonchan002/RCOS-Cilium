# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies directly
RUN pip install --no-cache-dir flask requests

# Copy application code
COPY app.py .

# Expose the port Flask will run on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

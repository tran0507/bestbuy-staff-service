# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies in the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy the staff-service.py file into the container
COPY staff-service.py .

# Expose the port that the Flask app will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "staff-service.py"]


# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Set the working directory to the folder containing the test files
WORKDIR /app/Api_tests

# Set the environment variable for API URL
ENV API_URL="https://jsonplaceholder.typicode.com/"

# Run the command to execute the tests
CMD ["pytest", "--rootdir=/app"]

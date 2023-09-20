# Use a slim Python image as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install any necessary dependencies
RUN pip install -r requirements.txt

# Expose the port that the Flask app will run on (if needed)
EXPOSE 6544

# Command to run the Flask app
CMD ["python", "app.py"]

# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code and additional files to the container
COPY app.py .
COPY config.py .

# Expose the port on which your application listens
EXPOSE 5000

# Set the environment variables (if needed)
# ENV VARIABLE_NAME=value

# Define the command to run your application
CMD ["python", "app.py"]

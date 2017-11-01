FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Only install requirements.txt if requirements file has changed
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
ADD . /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Override this cmd with docker-compose depending on whether its worker or manage or shell or the application server
CMD ["python", "app.py"]
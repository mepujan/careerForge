FROM python:3.11.4-alpine

WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade pip and install dependencies
RUN pip install --upgrade pip

# Copy requirements file and install dependencies
COPY ./requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

# Copy entrypoint script and give execute permission
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Copy the rest of the application code
COPY . /usr/src/app/

# Specify the entrypoint script
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

FROM python:3.10-slim-buster

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    netcat \
    git \
    && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh


# run entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]
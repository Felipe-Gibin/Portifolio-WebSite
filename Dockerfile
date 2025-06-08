FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1

# Install system dependencies for mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    libssl-dev \
    libffi-dev \
    build-essential \
    pkg-config \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip 
RUN pip3 install -r requirements.txt

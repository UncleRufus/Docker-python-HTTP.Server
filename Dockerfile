FROM python:3.10.5-slim-buster

WORKDIR /app

COPY . .

RUN apt-get update -y

RUN apt-get install -y cmake \
    git \
    curl \
    python3-pip

RUN pip install --upgrade pip && pip install -r requirements.txt

#RUN chmod +x local_scripts/admin_add.sh && local_scripts/admin_add.sh
FROM python:3.11-slim-bookworm
LABEL authors="jade"

# set display port to avoid crash
ENV DISPLAY=:99
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get -y update && apt-get install -y python3-pip libgl1-mesa-glx libglib2.0-0 && apt-get clean


WORKDIR /usr/src/app/

COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
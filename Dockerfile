# set base image
FROM python:3.8.5-alpine

# maintainer details
LABEL maintainer="Soumithri Chilakamarri <soumithri93@gmail.com>"

# Stop python from generating .pyc files and
# enable tracebacks on segfaults
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

# make the app directory
RUN mkdir -p /coding_problems

# set working directoy
WORKDIR /coding_problems

# copy dependencies file into working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt
# set base image
FROM python:3.8.5-alpine

# # update apk packages and create the directory
# RUN apt-get update && apt-get install -y git \
#     && rm -rf /var/lib/apt/lists/*

# make the app directory
RUN mkdir -p /usr/src/app

# set working directoy
WORKDIR /usr/src/app

# copy dependencies file into working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
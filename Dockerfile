
FROM ubuntu:18.04

# intall python
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev libffi-dev libssl-dev\
  && pip3 install --upgrade pip
RUN cd /usr/local/bin && ln -s /usr/bin/python3 python

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install python packages dependencies
RUN apt-get install -y unixodbc unixodbc-dev odbcinst sudo

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Recife
RUN apt-get install -y tzdata

WORKDIR /root/app

RUN mkdir -p /root/app/upload

COPY ./requirements.txt /root/app/requirements.txt
RUN pip install -r requirements.txt

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

COPY . /root/app

ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=4010"]
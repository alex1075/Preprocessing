ARG UBUNTU_VERSION=20.04

FROM ubuntu:${UBUNTU_VERSION} AS base
LABEL maintainer="Alexander Hunt <alexander.hunt@ed.ac.uk>"

RUN apt-get update && apt upgrade -y

RUN apt install python3-pip -y
COPY code.py /root/code.py
COPY requirements.txt /root/requirements.txt
RUN touch __innit__.py
RUN cd root && pip3 install -r requirements.txt
RUN mkdir -p /Volumes/PHD
CMD ["cd root", "python3 -c "from code import *; iterateBlur()""]

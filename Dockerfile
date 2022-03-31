FROM ubuntu:18.04
MAINTAINER EDUSEARCH <edusearchio@gmail.com>

ENV DEBIAN_FRONTEND=noniteractive
RUN apt-get update -y
RUN apt-get install -y apt-utils

RUN apt-get install -y build-essential libssl-dev

RUN apt-get install -y git-core
RUN apt-get install -y dnsutils
RUN apt-get install -y curl
RUN apt-get install -y python3.7

RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py

RUN pip install -U pip setuptools
RUN python get-pip.py

RUN git clone 

WORKDIR something/

RUN git pull

EXPOSE 8080

CMD ["make", "start"]

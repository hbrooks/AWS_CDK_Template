FROM python:3.6

RUN mkdir /usr/src/ms_main
WORKDIR /usr/src/ms_main

RUN pip install --upgrade pip
RUN pip3 install virtualenv
RUN pip3 install zappa

COPY ms_main/requirements.txt /usr/src/ms_main/requirements.txt
RUN pip3 install -r /usr/src/ms_main/requirements.txt

WORKDIR /usr/src/ms_main/src

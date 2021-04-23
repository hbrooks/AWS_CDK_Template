FROM python:3.6

RUN mkdir /usr/src/api_aws
WORKDIR /usr/src/api_aws

RUN pip install --upgrade pip
RUN pip3 install virtualenv
RUN pip3 install zappa

COPY api_aws/requirements.txt /usr/src/api_aws/requirements.txt
RUN pip3 install -r /usr/src/api_aws/requirements.txt

WORKDIR /usr/src/api_aws/src

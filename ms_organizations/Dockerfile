FROM python:3.6

RUN mkdir /usr/src/ms_organizations
WORKDIR /usr/src/ms_organizations

RUN pip install --upgrade pip
RUN pip3 install virtualenv
RUN pip3 install zappa

COPY ms_organizations/requirements.txt /usr/src/ms_organizations/requirements.txt
RUN pip3 install -r /usr/src/ms_organizations/requirements.txt

WORKDIR /usr/src/ms_organizations/src

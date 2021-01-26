FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /quantapi
COPY . /quantapi
WORKDIR /quantapi
RUN pip install -r requirements.txt
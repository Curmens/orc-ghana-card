FROM python:3.10-slim

WORKDIR /app

ENV PYHTONUNBUFFERED=1
RUN apt-get update \
  && apt-get -y install tesseract-ocr

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . /app

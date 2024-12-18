# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /code
ENV COUCHDB_SERVER=couchserver
ENV COUCHDB_USER=admin
ENV COUCHDB_PASSWORD=comp90024
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "mastodonCollector.py"]
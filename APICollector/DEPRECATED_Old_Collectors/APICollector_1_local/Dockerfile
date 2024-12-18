# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /code
ENV MASTODON_ACCESS_TOKEN=vL-AcF3hKOGhxMj08Is-TNNkwvRCQr2Ss89OjD-WZf0
ENV MASTODON_SERVER=https://mastodon.au
ENV MASTODON_TIMELINE=local
ENV COUCHDB_PASSWORD=comp90024
ENV COUCHDB_DATABASE=mastodon_au_local_raw
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "mastodonCollector.py"]
# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /code
ENV MASTODON_ACCESS_TOKEN=TFEPIDT_rMuTkmY_fl7-bFM84s7_O8dl3ur2Y67R4go
ENV MASTODON_SERVER=https://aus.social/
ENV MASTODON_TIMELINE=local
ENV COUCHDB_PASSWORD=comp90024
ENV COUCHDB_DATABASE=mastodon_aus_social_local_raw
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "mastodonCollector.py"]
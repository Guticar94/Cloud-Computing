# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /code
ENV MASTODON_ACCESS_TOKEN=ys4bYDBwbJq0Al0JG_Ra5B8tLxp9KxSfU9mGjHR--QI
ENV MASTODON_SERVER=https://mastodon.social
ENV MASTODON_TIMELINE=public
ENV COUCHDB_PASSWORD=comp90024
ENV COUCHDB_DATABASE=mastodon_world_social_raw
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "mastodonCollector.py"]
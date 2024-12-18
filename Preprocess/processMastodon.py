import torch
import requests
# Libraries and trained models for data processing####################################################################################################
import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline
import numpy as np
from scipy.special import expit

# __________________________________________________________________________________________________________________________________________
# Sentiment analysis transformer
generator = pipeline(task="sentiment-analysis")
# __________________________________________________________________________________________________________________________________________
MODEL = f"cardiffnlp/tweet-topic-21-multi"
tokenizer_clustering = AutoTokenizer.from_pretrained(MODEL)
model_clustering = AutoModelForSequenceClassification.from_pretrained(MODEL)
class_mapping = model_clustering.config.id2label
# __________________________________________________________________________________________________________________________________________
# Language classification transformer
model_language = 'qanastek/51-languages-classifier'
tokenizer_language = AutoTokenizer.from_pretrained(model_language)
model_lang = AutoModelForSequenceClassification.from_pretrained(model_language)
classifier_language = TextClassificationPipeline(model=model_lang, tokenizer=tokenizer_language)

SERVER_ADDRESS = 'http://admindb:Adm1nC04chDB@172.26.134.73:5984/'


def iterateMastonData():
    url = "http://admindb:Adm1nC04chDB@172.26.135.238:5984/"
    page_size = 100
    skip = 0
    database_name = "processed_twitter"
    updateUrl = url + database_name + "/_bulk_docs"
    headers = {'Content-type': 'application/json'}
    database = "mastodon_world_social_raw"
    while True:
        # get a page of documents from the database
        response = requests.get(url + f'{database}/_all_docs?include_docs=true&limit={page_size}&skip={skip}')
        data = response.json()
        if not data['rows']:
            break
        # iterate over the documents in the current page
        for row in data['rows']:
            doc = row['doc']
            if doc['content']:
                try:
                    doc["sentiment_analysis"] = generator(doc['content'])[0]['label']
                    doc["topics"] = topic_clustering(doc['content'])
                    doc["language"] = classifier_language(doc['content'])[0]['label']
                except:
                    pass
        data = {"docs": data['rows']}
        response = requests.post(URL, headers=headers, data=json.dumps(data))

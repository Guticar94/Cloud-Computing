# COMP90024 – Cluster and Cloud Computing - Team 4
# Assignment 2 – Australia Social Media Analytics on the Cloud
# Melbourne, Australia
#
# 1405461 - Andres Gutierrez
# 1110071 - Haining Xie
# 1025543 - Hernán Romano
# 1132915 - Zixuan Xiao
# 1298396 – Claudia Caro

import query.query2CouchDB as qDB

TOKEN = "pk.eyJ1IjoiZ3V0aWNhcjE5OTQiLCJhIjoiY2xoNnVxZTgyMDlwaTNrcnZ2bXU1eGdhcCJ9.ANrv4_Vl3Z2zdM6DZ77fKg"


def get_recurrence_by_topic_name(values_chosen, city, start_date, end_date):
    recurrence = []
    if city == "melbourne":
        weights = qDB.queryTopicByGcc(qDB.MELB_GCC, start_date, end_date)
        weights_filtered = {
            key: weights[key]
            for key in weights.keys()
            if len(key) > 1 and key in values_chosen
        }
    elif city == "sydney":
        weights = qDB.queryTopicByGcc(qDB.SYND_GCC, start_date, end_date)
        weights_filtered = {
            key: weights[key]
            for key in weights.keys()
            if len(key) > 1 and key in values_chosen
        }

    for topic in values_chosen:
        recurrence.append(weights_filtered[topic])

    return recurrence


def get_recurrence_by_topic_name_sentiment_and_social_media(
    values_chosen, start_date, end_date, sentiment, social_media
):
    recurrence = []
    databaseName = ""
    if social_media == "twitter":
        databaseName = qDB.PROCESSED_TWITTER
    else:
        databaseName = qDB.MASTODON
    if sentiment == "ALL":
        weightsP = qDB.querySection1("POSITIVE", start_date, end_date, databaseName)
        weightsN = qDB.querySection1("NEGATIVE", start_date, end_date, databaseName)
        for key in weightsP:
            if key in weightsN:
                weightsN[key] = weightsN[key] + weightsP[key]
            else:
                weightsN[key] = weightsP[key]
        weights = weightsN
    else:
        weights = qDB.querySection1(sentiment, start_date, end_date, databaseName)

    weights_filtered = {
        key: weights[key]
        for key in weights.keys()
        if len(key) > 1 and key in values_chosen
    }
    for topic in values_chosen:
        recurrence.append(weights_filtered.get(topic, 0))
    return recurrence


def get_weights_by_topic_name_sentiment_and_social_media(
    values_chosen, start_date, end_date, sentiment, social_media
):
    databaseName = ""
    if social_media == "twitter":
        databaseName = qDB.PROCESSED_TWITTER
    else:
        databaseName = qDB.MASTODON
    if sentiment == "ALL":
        weightsP = qDB.querySection1("POSITIVE", start_date, end_date, databaseName)
        weightsN = qDB.querySection1("NEGATIVE", start_date, end_date, databaseName)
        for key in weightsP:
            if key in weightsN:
                weightsN[key] = weightsN[key] + weightsP[key]
            else:
                weightsN[key] = weightsP[key]
        weights = weightsN
    else:
        weights = qDB.querySection1(sentiment, start_date, end_date, databaseName)

    weights_filtered = {
        key: weights[key]
        for key in weights.keys()
        if len(key) > 1 and key in values_chosen
    }
    return weights_filtered

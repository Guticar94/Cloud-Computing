# COMP90024 – Cluster and Cloud Computing - Team 4
# Assignment 2 – Australia Social Media Analytics on the Cloud
# Melbourne, Australia
#
# 1405461 - Andres Gutierrez
# 1110071 - Haining Xie
# 1025543 - Hernán Romano
# 1132915 - Zixuan Xiao
# 1298396 – Claudia Caro

import requests
from datetime import datetime
import json
import yaml
from itertools import cycle

SERVER_ADDRESS = "http://admindb:Adm1nC04chDB@172.26.134.73:5984/"
headers = {"Content-type": "application/json; charset=UTF-8"}
config = {}
with open("./config/queryConfig.yaml", "r") as f:
    config = yaml.safe_load(f)
addrs = config["servers"]
dbUser = config["dbuser"]
dbPass = config["dbPass"]
server_cycle = cycle(addrs)
SYND_GCC = "1gsyd"
MELB_GCC = "2gmel"
POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
PROCESSED_TWITTER = "processed_twitter/"
MASTODON = "mastodon_au_labeled/"
TEST = "test_view/"


def getServerAddr():
    while True:
        try:
            addr = next(server_cycle)
            url = "http://" + dbUser + ":" + dbPass + "@" + addr + "/"
            response = requests.get(url)
            if response.status_code == 200:
                return url
        except:
            pass


def parseDate(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.year, date_obj.month, date_obj.day


def getTopicRanks(start_date, end_date):
    database_name = "processed_twitter/"
    design_name = "dateTopic/"
    view_name = "dateTopic"
    sy, sm, sd = parseDate(start_date)
    ey, em, ed = parseDate(end_date)
    params = {
        "startkey": "[%d,%d,%d]" % (sy, sm, sd),
        "endkey": "[%d,%d,%d]" % (ey, em, ed),
    }
    url = (
        SERVER_ADDRESS + database_name + "_design/" + design_name + "_view/" + view_name
    )
    response = requests.get(url, params=params)
    data = json.loads(response.content)
    weightMap = {}
    data_topics = data["rows"][0]["value"]
    for i in range(len(data_topics)):
        weightMap[data_topics[i][0]] = data_topics[i][1]
    return weightMap


def queryTopicByGcc(gcc, start_date, end_date):
    database_name = "processed_twitter/"
    design_name = "gccDate/"
    view_name = "gccDate"
    sy, sm, sd = parseDate(start_date)
    ey, em, ed = parseDate(end_date)
    params = {
        "startkey": "[%s,%d,%d,%d]" % ('"' + gcc + '"', sy, sm, sd),
        "endkey": "[%s,%d,%d,%d]" % ('"' + gcc + '"', ey, em, ed),
    }
    url = (
        getServerAddr()
        + database_name
        + "_design/"
        + design_name
        + "_view/"
        + view_name
    )
    response = requests.get(url, params=params)
    data = json.loads(response.content)
    weightMap = {}
    try:
        data_topics = data["rows"][0]["value"]
        for i in range(len(data_topics)):
            weightMap[data_topics[i][0]] = data_topics[i][1]
    except:
        pass
    return weightMap


# queryTopicByGcc("1gsyd","2021-5-1","2022-3-1")
def querySenByGcc(gcc, sen, start_date, end_date):
    database_name = "processed_twitter/"
    design_name = "compose/"
    view_name = "compose"
    sy, sm, sd = parseDate(start_date)
    ey, em, ed = parseDate(end_date)
    params = {
        "startkey": "[%s,%s,%d,%d,%d]" % ('"' + gcc + '"', '"' + sen + '"', sy, sm, sd),
        "endkey": "[%s,%s,%d,%d,%d]" % ('"' + gcc + '"', '"' + sen + '"', ey, em, ed),
    }
    url = (
        getServerAddr()
        + database_name
        + "_design/"
        + design_name
        + "_view/"
        + view_name
    )
    response = requests.get(url, params=params)
    data = json.loads(response.content)
    weightMap = {}
    try:
        data_topics = data["rows"][0]["value"]
        for i in range(len(data_topics)):
            weightMap[data_topics[i][0]] = data_topics[i][1]
    except:
        pass
    return weightMap


def querySection1(sen, start_date, end_date, databaseName):
    database_name = databaseName
    design_name = "s1/"
    view_name = "s1"
    sy, sm, sd = parseDate(start_date)
    ey, em, ed = parseDate(end_date)
    params = {
        "startkey": "[%s,%d,%d,%d]" % ('"' + sen + '"', sy, sm, sd),
        "endkey": "[%s,%d,%d,%d]" % ('"' + sen + '"', ey, em, ed),
    }
    url = (
        getServerAddr()
        + database_name
        + "_design/"
        + design_name
        + "_view/"
        + view_name
    )
    response = requests.get(url, params=params)
    data = json.loads(response.content)
    weightMap = {}
    try:
        data_topics = data["rows"][0]["value"]
        for i in range(len(data_topics)):
            weightMap[data_topics[i][0]] = data_topics[i][1]
    except:
        pass

    return weightMap


# querySection1("NEGATIVE","2021-5-1","2022-3-1",TEST)
def iterateMastonData():
    url = "http://admindb:Adm1nC04chDB@172.26.135.238:5984/"
    page_size = 100
    skip = 0
    database = "mastodon_world_social_raw"
    while True:
        # get a page of documents from the database
        response = requests.get(
            url
            + f"{database}/_all_docs?include_docs=true&limit={page_size}&skip={skip}"
        )
        data = response.json()
        if not data["rows"]:
            break
        # iterate over the documents in the current page
        for row in data["rows"]:
            doc = row["doc"]
            # do something with the document
            print(doc)


# iterateMastonData()

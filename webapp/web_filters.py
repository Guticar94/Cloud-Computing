# COMP90024 – Cluster and Cloud Computing - Team 4
# Assignment 2 – Australia Social Media Analytics on the Cloud
# Melbourne, Australia
#
# 1405461 - Andres Gutierrez
# 1110071 - Haining Xie
# 1025543 - Hernán Romano
# 1132915 - Zixuan Xiao
# 1298396 – Claudia Caro

import dash_bootstrap_components as dbc
from dash import html, dcc
import query.query2CouchDB as qDB


def web_filter_section_one():
    weights = qDB.getTopicRanks("2021-03-01", "2023-05-01")
    weights_filtered = {key: weights[key] for key in weights.keys() if len(key) > 1}

    frequency_of_topics = []
    topic_list = []

    for key, value in weights_filtered.items():
        frequency_of_topics.append(value)
        topic_list.append(key)

    dropdown = (
        dcc.Dropdown(
            id="my-dropdown-section-one",
            multi=True,
            options=[{"label": x, "value": x} for x in sorted(topic_list)],
            value=topic_list,
        ),
    )

    filter = dbc.Col(
        [
            html.H3(
                "Filter your trending topics",
                style={"text-align": "center"},
            ),
            *dropdown,
        ],
        lg=12,
    )

    return filter
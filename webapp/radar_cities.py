# COMP90024 – Cluster and Cloud Computing - Team 4
# Assignment 2 – Australia Social Media Analytics on the Cloud
# Melbourne, Australia
#
# 1405461 - Andres Gutierrez
# 1110071 - Haining Xie
# 1025543 - Hernán Romano
# 1132915 - Zixuan Xiao
# 1298396 – Claudia Caro

from dash import html, dcc, exceptions
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import html, dcc, callback, Output, Input
import query.query2CouchDB as qDB
from utils import get_recurrence_by_topic_name_sentiment_and_social_media


def radar_twitter():
    weights = qDB.getTopicRanks("2021-03-01", "2023-05-01")
    weights_filtered = {key: weights[key] for key in weights.keys() if len(key) > 1}

    frequency_of_topics = []
    topic_list = []

    for key, value in weights_filtered.items():
        frequency_of_topics.append(value)
        topic_list.append(key)

    fig = go.Figure(
        data=go.Scatterpolar(
            r=frequency_of_topics,
            theta=topic_list,
            fill="toself",
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True),
        ),
        showlegend=False,
    )

    radar_graph = dcc.Graph(
        id="radar-graph-twitter",
        figure=fig,
        config={
            "modeBarButtonsToRemove": [
                "toggleSpikelines",
                "pan2d",
                "autoScale2d",
                "resetScale2d",
            ]
        },
    )

    radar = dbc.Col(
        [
            html.H3(
                "Twitter Radar",
                style={"text-align": "center"},
            ),
            radar_graph,
        ],
        lg=6,
    )

    return radar


def radar_mastodon():
    weights = qDB.getTopicRanks("2021-03-01", "2023-05-01")
    weights_filtered = {key: weights[key] for key in weights.keys() if len(key) > 1}

    frequency_of_topics = []
    topic_list = []

    for key, value in weights_filtered.items():
        frequency_of_topics.append(value)
        topic_list.append(key)

    fig = go.Figure(
        data=go.Scatterpolar(
            r=frequency_of_topics,
            theta=topic_list,
            fill="toself",
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True),
        ),
        showlegend=False,
    )

    radar_graph = dcc.Graph(
        id="radar-graph-mastodon",
        figure=fig,
        config={
            "modeBarButtonsToRemove": [
                "toggleSpikelines",
                "pan2d",
                "autoScale2d",
                "resetScale2d",
            ]
        },
    )

    radar = dbc.Col(
        [
            html.H3(
                "Mastodon Radar",
                style={"text-align": "center"},
            ),
            radar_graph,
        ],
        lg=6,
    )

    return radar


# Callback for radar graph
@callback(
    [
        Output(component_id="radar-graph-twitter", component_property="figure"),
        Output(component_id="radar-graph-mastodon", component_property="figure"),
    ],
    [
        Input(component_id="radio-button-section-one", component_property="value"),
        Input(component_id="my-dropdown-section-one", component_property="value"),
        Input(
            component_id="date-picker-range-section-one",
            component_property="start_date",
        ),
        Input(
            component_id="date-picker-range-section-one", component_property="end_date"
        ),
    ],
    prevent_initial_call=False,
)
def update_radar_twitter(sentiment, values_chosen, start_date, end_date):
    recurrence_twitter = get_recurrence_by_topic_name_sentiment_and_social_media(
        values_chosen, start_date, end_date, sentiment, "twitter"
    )
    figure_twitter = get_updated_figure(values_chosen, recurrence_twitter)

    recurrence_mastodon = get_recurrence_by_topic_name_sentiment_and_social_media(
        values_chosen, start_date, end_date, sentiment, "mastodon"
    )
    figure_mastodon = get_updated_figure(values_chosen, recurrence_mastodon)

    return figure_twitter, figure_mastodon


def get_updated_figure(values_chosen, recurrence):
    if len(values_chosen) > 0:
        figure = go.Figure(
            data=go.Scatterpolar(
                r=recurrence,
                theta=values_chosen,
                fill="toself",
            )
        )

        figure.update_layout(
            polar=dict(
                radialaxis=dict(visible=True),
            ),
            showlegend=False,
        )
    elif len(values_chosen) == 0:
        raise exceptions.PreventUpdate

    return figure

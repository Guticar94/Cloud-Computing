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
from dash import html, dcc, callback, Output, Input
from wordcloud import WordCloud
import base64
from io import BytesIO
import plotly.express as px
import query.query2CouchDB as qDB
import wordCloud as wc
from utils import get_weights_by_topic_name_sentiment_and_social_media


# section 2: main body
def createTwitterWordCloud(words_weight):
    fig = updateWithWeight(words_weight)
    worldcloud_graph = dbc.Col(
        [
            html.H3(
                "Trending Topics in Australia - Twitter",
                style={"text-align": "center"},
            ),
            html.H6(
                [
                    "Click over the word cloud to zoom in.",
                ],
                style={"text-align": "center"},
                className="mb-0",
            ),
            html.Div(
                dcc.Graph(
                    figure=fig,
                    config={"displayModeBar": False},
                    id="twitter_word",
                ),
                id="myDiv",
            ),
            html.Div(id="LinkOutCountry"),
        ],
        lg=12,
    )
    return worldcloud_graph


def createMastodonWordCloud(words_weight):
    fig = updateWithWeight(words_weight)
    worldcloud_graph = dbc.Col(
        [
            html.H3(
                "Trending Topics in Australia - Mastodon",
                style={"text-align": "center"},
            ),
            html.H6(
                [
                    "Click over the word cloud to zoom in.",
                ],
                style={"text-align": "center"},
                className="mb-0",
            ),
            html.Div(
                dcc.Graph(
                    figure=fig,
                    config={"displayModeBar": False},
                    id="mastodon_word",
                ),
                id="myDiv",
            ),
            html.Div(id="LinkOutCountry"),
        ],
        lg=12,
    )
    return worldcloud_graph


def updateWithWeight(words_wight):
    if len(words_wight) == 0:
        words_wight["Default"] = 1
    wc = WordCloud(width=800, height=600,background_color='white')

    # Generate the word cloud from the word weights
    wc.generate_from_frequencies(words_wight)

    # Convert the WordCloud image to a PNG data URI
    img = wc.to_image()
    with BytesIO() as buffer:
        img.save(buffer, "PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()
    fig = px.imshow(img)
    fig.update_layout(
        margin=dict(l=0, r=0, b=0, t=0),
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
    )
    return fig


@callback(
    [
        Output(component_id="twitter_word", component_property="figure"),
        Output(component_id="mastodon_word", component_property="figure"),
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
def update_wordCloud(sentiment, values_chosen, start_date, end_date):
    twitter = get_weights_by_topic_name_sentiment_and_social_media(
        values_chosen, start_date, end_date, sentiment, "twitter"
    )
    mastodon = get_weights_by_topic_name_sentiment_and_social_media(
        values_chosen, start_date, end_date, sentiment, "mastodon"
    )

    return [updateWithWeight(twitter), updateWithWeight(mastodon)]

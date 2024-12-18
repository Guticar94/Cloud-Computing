# COMP90024 – Cluster and Cloud Computing - Team 4
# Assignment 2 – Australia Social Media Analytics on the Cloud
# Melbourne, Australia
#
# 1405461 - Andres Gutierrez
# 1110071 - Haining Xie
# 1025543 - Hernán Romano
# 1132915 - Zixuan Xiao
# 1298396 – Claudia Caro

import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import html, dcc, exceptions
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Output, Input

from utils import get_recurrence_by_topic_name_sentiment_and_social_media


def pie_twitter_vs_mastodon():
    labels = [
        "Topic 1",
        "Topic 2",
        "Topic 3",
        "Topic 4",
        "Topic 5",
        "Topic 6",
        "Topic 7",
        "Topic 8",
        "Topic 9",
        "Topic 10",
    ]
    percentages_melbourne = [8, 15, 12, 6, 5, 2, 21, 21, 2, 8]
    percentages_sydney = [27, 6, 25, 4, 1, 3, 13, 12, 4, 5]

    # Create subplots: use 'domain' type for Pie subplot
    fig = make_subplots(
        rows=1, cols=2, specs=[[{"type": "domain"}, {"type": "domain"}]]
    )
    fig.add_trace(
        go.Pie(labels=labels, values=percentages_melbourne, name="Twitter"), 1, 1
    )
    fig.add_trace(
        go.Pie(labels=labels, values=percentages_sydney, name="Mastodon"), 1, 2
    )

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=0.4, hoverinfo="label+percent+name")

    fig.update_layout(
        title_text="Australian Trending Topics Comparison between Twitter and Mastodon",
        # Add annotations in the center of the donut pies.
        annotations=[
            dict(text="Twitter", x=0.18, y=0.5, font_size=20, showarrow=False),
            dict(text="Mastodon", x=0.82, y=0.5, font_size=20, showarrow=False),
        ],
    )

    pie_graph = dcc.Graph(
        id="pie-graph-twitter-mastodon",
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

    pie = dbc.Col(
        [
            html.H3(
                "Twitter vs Mastodon Pie",
                style={"text-align": "center"},
            ),
            pie_graph,
        ],
        lg=12,
    )

    return pie


def get_percentages_twitter_mastodon(recurrence_twitter, recurrence_mastodon):
    percentages_twitter = []
    percentages_mastodon = []
    total_twitter = sum(recurrence_twitter)
    total_mastodon = sum(recurrence_mastodon)
    if total_twitter > 0 and total_mastodon > 0:
        for recurrence in recurrence_twitter:
            percentages_twitter.append(recurrence / total_twitter * 100)
        for recurrence in recurrence_mastodon:
            percentages_mastodon.append(recurrence / total_mastodon * 100)
    return percentages_twitter, percentages_mastodon


def get_updated_figure(values_chosen, percentages_melbourne, percentages_sydney):
    if len(values_chosen) > 0:
        # Create subplots: use 'domain' type for Pie subplot
        figure = make_subplots(
            rows=1, cols=2, specs=[[{"type": "domain"}, {"type": "domain"}]]
        )
        figure.add_trace(
            go.Pie(labels=values_chosen, values=percentages_melbourne, name="Twitter"),
            1,
            1,
        )
        figure.add_trace(
            go.Pie(labels=values_chosen, values=percentages_sydney, name="Mastodon"),
            1,
            2,
        )

        # Use `hole` to create a donut-like pie chart
        figure.update_traces(hole=0.4, hoverinfo="label+percent+name")

        figure.update_layout(
            title_text="Australian Trending Topics Comparison between Twitter and Mastodon",
            # Add annotations in the center of the donut pies.
            annotations=[
                dict(text="Twitter", x=0.18, y=0.5, font_size=20, showarrow=False),
                dict(text="Mastodon", x=0.82, y=0.5, font_size=20, showarrow=False),
            ],
        )
    elif len(values_chosen) == 0:
        raise exceptions.PreventUpdate

    return figure


# Topic Filter Callback for Pie Graph
@callback(
    Output(component_id="pie-graph-twitter-mastodon", component_property="figure"),
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
def update_pie_twitter_and_mastodon(sentiment, values_chosen, start_date, end_date):
    recurrence_twitter = get_recurrence_by_topic_name_sentiment_and_social_media(
        values_chosen, start_date, end_date, sentiment, "twitter"
    )
    recurrence_mastodon = get_recurrence_by_topic_name_sentiment_and_social_media(
        values_chosen, start_date, end_date, sentiment, "mastodon"
    )

    percentages_twitter, percentages_mastodon = get_percentages_twitter_mastodon(
        recurrence_twitter, recurrence_mastodon
    )

    figure_twitter_and_mastodon = get_updated_figure(
        values_chosen, percentages_twitter, percentages_mastodon
    )

    return figure_twitter_and_mastodon

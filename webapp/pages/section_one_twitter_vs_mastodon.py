# COMP90024 – Cluster and Cloud Computing - Team 4
# Assignment 2 – Australia Social Media Analytics on the Cloud
# Melbourne, Australia
#
# 1405461 - Andres Gutierrez
# 1110071 - Haining Xie
# 1025543 - Hernán Romano
# 1132915 - Zixuan Xiao
# 1298396 – Claudia Caro

from dash import html, dcc
from dash import dcc, html, register_page
import dash_bootstrap_components as dbc
from radar_cities import radar_twitter, radar_mastodon
from pie_cities import pie_twitter_vs_mastodon
from live_notifications import live_mastodon_notifications
from SwitchButton import radioSwitchButton_section_one
from web_filters import web_filter_section_one
from DateSelector import dateSelector_section_one

from wordCloud import createTwitterWordCloud, createMastodonWordCloud

register_page(__name__, path="/twitter_vs_mastodon", title="Twitter vs Mastodon")


### functions for different part of layout
# Section 1: mission statement
def mission_statement():
    return html.Div(
        dbc.Container(
            dbc.Row(
                dbc.Col(
                    [
                        html.H1(
                            "Topic: Australian Trending Topics comparison between Twitter and Mastodon",
                            className="display-4",
                        ),
                    ]
                ),
            ),
            className="px-4",
        ),
        className="bg-light rounded-3 py-5 mb-4",
    )


# Section 2: Filters
def twitter_vs_mastodon_filters():
    return [
        dbc.Row(
            [
                radioSwitchButton_section_one(),
                dateSelector_section_one(),
                web_filter_section_one(),
            ],
            className="mb-5",
        ),
    ]


# Section 3: Word Cloud
def twitter_vs_mastodon_word_clouds():
    return [
        dbc.Row(
            [dbc.Col(createTwitterWordCloud({"hello": 5, "weather": 10, "Topic": 3})),
             dbc.Col(createMastodonWordCloud({"hello": 5, "weather": 10, "Topic": 3}))],
            className="mb-5",
        ),
    ]


# Section 4: Radar charts
def twitter_vs_mastodon_radars():
    return [
        dbc.Row(
            [radar_twitter(), radar_mastodon()],
            className="mb-5",
        ),
    ]


# Section 5: Pie charts
def twitter_vs_mastodon_pies():
    return [
        dbc.Row(
            [pie_twitter_vs_mastodon()],
            className="mb-5",
        ),
    ]


# Live Streaming Container
def twitter_vs_mastodon_live_streaming_container():
    return live_mastodon_notifications()


def main_body():
    return dbc.Container(
        [
            *twitter_vs_mastodon_filters(),
            *twitter_vs_mastodon_word_clouds(),
            *twitter_vs_mastodon_radars(),
            *twitter_vs_mastodon_pies(),
        ]
    )


layout = html.Div(
    [
        dcc.Location(id="twitter_vs_mastodon_url", refresh=True),
        mission_statement(),
        main_body(),
        *twitter_vs_mastodon_live_streaming_container(),
    ]
)

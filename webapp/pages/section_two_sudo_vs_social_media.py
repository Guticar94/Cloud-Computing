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
import dash
import dash_bootstrap_components as dbc
from maps_cities import map_melbourne, map_sydney
from DateSelector import dateSelector_section_two
from horizontal_bars import horizontal_bar_melbourne_sydney
from map_income_comparisson import map_income_trending_topics

dash.register_page(__name__, path="/sudo_vs_social_media", title="SUDO vs Social Media")


### functions for different part of sudo_vs_social_media page
# section 1: Title
def mission_statement():
    return html.Div(
        dbc.Container(
            dbc.Row(
                dbc.Col(
                    [
                        html.H1(
                            "Topic: Trending Topics comparison by income between the states of Australia",
                            className="display-4",
                        ),
                    ]
                ),
            ),
            className="px-4",
        ),
        className="bg-light rounded-3 py-5 mb-4",
    )


# section 2: Filters
def sudo_vs_social_media_filters():
    return [
        dbc.Row(
            [
                dateSelector_section_two(),
            ],
            className="mb-5",
        ),
    ]


# section 3: maps
def sudo_vs_social_media_maps():
    return [
        dbc.Row(
            [map_melbourne(), map_sydney()],
            className="mb-5",
        ),
    ]


# section 4: horizontal_bars
def sudo_vs_social_media_horizontal_bars():
    return [
        dbc.Row(
            [horizontal_bar_melbourne_sydney()],
            className="mb-5",
        ),
    ]


# section 5: map_income comparison
def sudo_vs_social_media_map_income_comparisson():
    return [
        dbc.Row(
            [map_income_trending_topics()],
            className="mb-5",
        ),
    ]


def main_body():
    return dbc.Container(
        [
            *sudo_vs_social_media_filters(),
            *sudo_vs_social_media_maps(),
            *sudo_vs_social_media_horizontal_bars(),
            *sudo_vs_social_media_map_income_comparisson(),
        ]
    )


layout = html.Div(
    [
        dcc.Location(id="home_url", refresh=True),
        mission_statement(),
        main_body(),
    ]
)

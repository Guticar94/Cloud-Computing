# COMP90024 – Cluster and Cloud Computing - Team 4
# Assignment 2 – Australia Social Media Analytics on the Cloud
# Melbourne, Australia
#
# 1405461 - Andres Gutierrez
# 1110071 - Haining Xie
# 1025543 - Hernán Romano
# 1132915 - Zixuan Xiao
# 1298396 – Claudia Caro

import plotly.express as px
import pandas as pd
import json
import dash_bootstrap_components as dbc
from dash import html, dcc
from utils import TOKEN


def map_melbourne():
    with open("./data/map_melbourne/SUDO_mel.json", "r") as rf:
        df_mel = pd.DataFrame(json.load(rf))

    with open("./data/map_melbourne/geoJSON_mel.json", "r") as rf:
        geojson_mel = json.load(rf)

    fig = px.choropleth_mapbox(
        df_mel,
        geojson=geojson_mel,
        color="median_tot_hhd_inc_weekly",
        locations="SA2_NAME21",
        featureidkey="properties.sa2_name",
        hover_data=[
            "median_tot_hhd_inc_weekly",
            "median_mortgage_repay_monthly",
            "median_rent_weekly",
        ],
        center={"lat": -37.840935, "lon": 144.946457},
        zoom=9,
        color_continuous_scale="YlOrRd",
        range_color=(df_mel["median_tot_hhd_inc_weekly"].min(), df_mel["median_tot_hhd_inc_weekly"].max()),
    )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, mapbox_accesstoken=TOKEN)

    map_melbourne = dbc.Col(
        [
            html.H3(
                "Melbourne Map",
                style={"text-align": "center"},
            ),
            html.H6(
                [
                    "Click on a suburb to view more. ",
                ],
                style={"text-align": "center"},
                className="mb-0",
            ),
            html.Div(
                dcc.Graph(
                    figure=fig,
                    config={"displayModeBar": False},
                    id="choropleth",
                ),
                id="myDiv",
            ),
            html.Div(id="LinkOutCountry"),
        ],
        lg=6,
    )
    return map_melbourne


def map_sydney():
    with open("./data/map_sydney/SUDO_syd.json", "r") as rf:
        df_syd = pd.DataFrame(json.load(rf))

    with open("./data/map_sydney/geoJSON_syd.json", "r") as rf:
        geojson_syd = json.load(rf)

    fig = px.choropleth_mapbox(
        df_syd,
        geojson=geojson_syd,
        color="median_tot_hhd_inc_weekly",
        locations="SA2_NAME21",
        featureidkey="properties.sa2_name",
        hover_data=[
            "median_tot_hhd_inc_weekly",
            "median_mortgage_repay_monthly",
            "median_rent_weekly",
        ],
        center={"lat": -33.865143, "lon": 151.209900},
        zoom=7,
        color_continuous_scale="YlOrRd",
        range_color=(df_syd["median_tot_hhd_inc_weekly"].min(), df_syd["median_tot_hhd_inc_weekly"].max()),
    )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, mapbox_accesstoken=TOKEN)

    map_sydney = dbc.Col(
        [
            html.H3(
                "Sydney Map",
                style={"text-align": "center"},
            ),
            html.H6(
                [
                    "Click on a suburb to view more. ",
                ],
                style={"text-align": "center"},
                className="mb-0",
            ),
            html.Div(
                dcc.Graph(
                    figure=fig,
                    config={"displayModeBar": False},
                    id="choropleth",
                ),
                id="myDiv",
            ),
            html.Div(id="LinkOutCountry"),
        ],
        lg=6,
    )

    return map_sydney

# COMP90024 – Cluster and Cloud Computing - Team 4
# Assignment 2 – Australia Social Media Analytics on the Cloud
# Melbourne, Australia
#
# 1405461 - Andres Gutierrez
# 1110071 - Haining Xie
# 1025543 - Hernán Romano
# 1132915 - Zixuan Xiao
# 1298396 – Claudia Caro

import geopandas as gpd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Output, Input
import query.query2CouchDB as qDB
import json
import pandas as pd


def getDict():
    with open("./config/SUDO_aus.json", "r") as rf:
        # df_aus
        return json.load(rf)


gccDict = getDict()


def getGccByName(name):
    nameDict = gccDict["GCC_NAME21"]
    for key in nameDict:
        if nameDict[key] == name:
            return gccDict["GCC_CODE21"][key].lower()


def map_income_trending_topics():
    gcc = (
        gpd.read_file("./data/map_income/GCCSA_2021_AUST_SHP_GDA2020.zip")
        .dropna()
        .reset_index(drop=True)
    )

    income_df = pd.read_csv("./data/map_income/medians_averages.csv")
    # simplify geometry to 1000m accuracy
    gcc["geometry"] = gcc.to_crs(gcc.estimate_utm_crs()).simplify(1000).to_crs(gcc.crs)
    gcc.dropna(axis=0, subset="geometry", how="any", inplace=True)
    gcc.set_index("GCC_NAME21")
    gcc = gcc.to_crs(epsg=4326)
    geojson = gcc.__geo_interface__

    gcc = gcc.assign(median_income=income_df["median_tot_hhd_inc_weekly"])

    token = "pk.eyJ1IjoiZ3V0aWNhcjE5OTQiLCJhIjoiY2xoNnVxZTgyMDlwaTNrcnZ2bXU1eGdhcCJ9.ANrv4_Vl3Z2zdM6DZ77fKg"
    fig = px.choropleth_mapbox(
        gcc,
        geojson=gcc.geometry,
        color=gcc.median_income,
        locations=gcc.index,
        # featureidkey="properties.gcc_name",
        hover_data=["GCC_NAME21", "median_income"],
        center={"lat": -28, "lon": 138},
        zoom=3,
        color_continuous_scale="YlOrRd",
        range_color=(1190, 2373),
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, mapbox_accesstoken=token)

    map_income_comparisson = dbc.Col(
        [
            html.H3(
                "TOP 3 trending topics per State",
                style={"text-align": "center"},
            ),
            html.H6(
                [
                    "Click on a state to view more. ",
                ],
                style={"text-align": "center"},
                className="mb-0",
            ),
            html.Div(
                dcc.Graph(
                    figure=fig,
                    config={"displayModeBar": False},
                    id="au_map",
                ),
                id="myDiv",
            ),
            html.Div(id="trendings"),
            html.Div(id="LinkOutCountry"),
        ],
        lg=12,
    )
    return map_income_comparisson


# Define callback function to highlight state on hover
@callback(
    [Output("trendings", "children")],
    [
        Input("au_map", "clickData"),
        Input("date-picker-range-section-two", "start_date"),
        Input("date-picker-range-section-two", "end_date"),
    ],
)
def highlight_state_on_hover(click_data, st_date, end_date):
    if click_data is None:
        return [html.Div("")]

    # Get the selected state from click data
    selected_state = click_data["points"][0]["location"]
    gcc = gccDict["GCC_CODE21"][str(selected_state)].lower()
    # Query the topics
    weights = qDB.queryTopicByGcc(gcc, st_date, end_date)
    trending_topics = sorted(weights.items(), key=lambda item: item[1])
    trending_topics.reverse()
    if len(trending_topics) >= 3:
        trending_topics = trending_topics[:3]
    res = [html.Div("Trending topics:")]
    for i in range(len(trending_topics)):
        position = i + 1
        res.append(html.Div(f"{position}° {trending_topics[i][0]}"))

    return [res]

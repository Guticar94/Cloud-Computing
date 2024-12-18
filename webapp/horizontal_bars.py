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


def horizontal_bat_melbourne():
    with open("./data/horizontal_bar/SUDO_mel.json", "r") as rf:
        df = pd.DataFrame.from_dict(json.load(rf))

    horizontal_bar_melbourne = (
        df.drop(["sa2_code", "SA2_NAME21"], axis=1)
        .groupby("GCC_CODE21")
        .agg(
            {
                "AREASQKM21": "sum",
                "median_tot_prsnl_inc_weekly": "mean",
                "median_tot_hhd_inc_weekly": "mean",
                "median_tot_fam_inc_weekly": "mean",
                "median_rent_weekly": "mean",
                "median_mortgage_repay_monthly": "mean",
                "median_age_persons": "mean",
                "average_num_psns_per_bedroom": "mean",
                "average_household_size": "mean",
            }
        )
        .unstack()
        .reset_index()
    )

    horizontal_bar_melbourne.columns = ["stats", "city", "value"]
    horizontal_bar_melbourne["city"] = "Melbourne"
    horizontal_bar_melbourne = horizontal_bar_melbourne.sort_values(
        "value", ascending=False
    )

    return horizontal_bar_melbourne


def horizontal_bat_sydney():
    with open("./data/horizontal_bar/SUDO_syd.json", "r") as rf:
        df_syd = pd.DataFrame.from_dict(json.load(rf))

    horizontal_bar_sydney = (
        df_syd.drop(["sa2_code", "SA2_NAME21"], axis=1)
        .groupby("GCC_CODE21")
        .agg(
            {
                "AREASQKM21": "sum",
                "median_tot_prsnl_inc_weekly": "mean",
                "median_tot_hhd_inc_weekly": "mean",
                "median_tot_fam_inc_weekly": "mean",
                "median_rent_weekly": "mean",
                "median_mortgage_repay_monthly": "mean",
                "median_age_persons": "mean",
                "average_num_psns_per_bedroom": "mean",
                "average_household_size": "mean",
            }
        )
        .unstack()
        .reset_index()
    )

    horizontal_bar_sydney.columns = ["stats", "city", "value"]
    horizontal_bar_sydney["city"] = "Sydney"
    horizontal_bar_sydney = horizontal_bar_sydney.sort_values("value", ascending=False)
    horizontal_bar_sydney.iloc[1:, :]

    return horizontal_bar_sydney


def horizontal_bar_melbourne_sydney():
    melb = horizontal_bat_melbourne()
    syd = horizontal_bat_sydney()

    df_cities = pd.concat([syd.iloc[1:, :], melb.iloc[1:, :]], axis=0)
    df_cities["value"] = round(df_cities["value"], 3)

    fig = px.funnel(df_cities, x="value", y="stats", color="city")

    horizontal_bar_melbourne_sydney = dbc.Col(
        [
            html.H3(
                "Income comparison Melb vs Syd",
                style={"text-align": "center"},
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
        lg=12,
    )
    return horizontal_bar_melbourne_sydney

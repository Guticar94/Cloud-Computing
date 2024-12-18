# COMP90024 – Cluster and Cloud Computing - Team 4
# Assignment 2 – Australia Social Media Analytics on the Cloud
# Melbourne, Australia
#
# 1405461 - Andres Gutierrez
# 1110071 - Haining Xie
# 1025543 - Hernán Romano
# 1132915 - Zixuan Xiao
# 1298396 – Claudia Caro

from dash import dcc
from dash import html
from dash import html, dcc


# define the layout of the app
def dateSelector_section_one():
    return html.Div(
        children=[
            html.H3(children="Select Date Range"),
            dcc.DatePickerRange(
                id="date-picker-range-section-one",
                min_date_allowed="1970-01-01",
                max_date_allowed="2023-06-01",
                initial_visible_month="2023-03-01",
                start_date="2021-01-01",
                end_date="2023-05-22",
            ),
        ]
    )


# define the layout of the app
def dateSelector_section_two():
    return html.Div(
        children=[
            html.H3(children="Select Date Range"),
            dcc.DatePickerRange(
                id="date-picker-range-section-two",
                min_date_allowed="1970-01-01",
                max_date_allowed="2023-06-01",
                initial_visible_month="2023-03-01",
                start_date="2021-01-01",
                end_date="2023-05-22",
            ),
        ]
    )


# Callback function that update wordCloud according to date
"""
@app.callback(
    [dash.dependencies.Output("melb_word", 'figure')],
    dash.dependencies.Input('date-picker-range', 'start_date'),
    dash.dependencies.Input('date-picker-range', 'end_date')
)
def updateTopicWithDate(st_date,end_date):
"""

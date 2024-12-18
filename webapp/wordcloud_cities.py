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
import pandas as pd
import pandas as pd
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
from dash import html, dcc

GLOBAL_DF = pd.read_csv("./data/customer_complaints_narrative_sample.csv.gz", header=0)


def sample_data(dataframe, float_percent):
    """
    Returns a subset of the provided dataframe.
    The sampling is evenly distributed and reproducible
    """
    return dataframe.sample(frac=float_percent, random_state=1)


def plotly_wordcloud(data_frame):
    """A wonderful function that returns figure data for three equally
    wonderful plots: wordcloud, frequency histogram and treemap"""
    complaints_text = list(data_frame["Consumer complaint narrative"].dropna().values)

    if len(complaints_text) < 1:
        return {}, {}, {}

    # join all documents in corpus
    text = " ".join(list(complaints_text))

    word_cloud = WordCloud(stopwords=set(STOPWORDS), max_words=100, max_font_size=90)
    word_cloud.generate(text)

    word_list = []
    freq_list = []
    fontsize_list = []
    position_list = []
    orientation_list = []
    color_list = []

    for (word, freq), fontsize, position, orientation, color in word_cloud.layout_:
        word_list.append(word)
        freq_list.append(freq)
        fontsize_list.append(fontsize)
        position_list.append(position)
        orientation_list.append(orientation)
        color_list.append(color)

    # get the positions
    x_arr = []
    y_arr = []
    for i in position_list:
        x_arr.append(i[0])
        y_arr.append(i[1])

    # get the relative occurence frequencies
    new_freq_list = []
    for i in freq_list:
        new_freq_list.append(i * 80)

    trace = go.Scatter(
        x=x_arr,
        y=y_arr,
        textfont=dict(size=new_freq_list, color=color_list),
        hoverinfo="text",
        textposition="top center",
        hovertext=["{0} - {1}".format(w, f) for w, f in zip(word_list, freq_list)],
        mode="text",
        text=word_list,
    )

    layout = go.Layout(
        {
            "xaxis": {
                "showgrid": False,
                "showticklabels": False,
                "zeroline": False,
                "automargin": True,
                "range": [-100, 250],
            },
            "yaxis": {
                "showgrid": False,
                "showticklabels": False,
                "zeroline": False,
                "automargin": True,
                "range": [-100, 450],
            },
            "margin": dict(t=20, b=20, l=10, r=10, pad=4),
            "hovermode": "closest",
        }
    )

    wordcloud_figure_data = {"data": [trace], "layout": layout}
    word_list_top = word_list[:25]
    word_list_top.reverse()
    freq_list_top = freq_list[:25]
    freq_list_top.reverse()

    return wordcloud_figure_data


# section 2: main body
def word_cloud_melbourne():
    n_selection = 100
    n_float = float(n_selection / 100)
    local_df = sample_data(GLOBAL_DF, n_float)
    wordcloud = plotly_wordcloud(local_df)

    worldcloud_graph = dbc.Col(
        [
            html.H3(
                "Melbourne Word Cloud",
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
                    figure=wordcloud,
                    config={"displayModeBar": False},
                    id="choropleth",
                ),
                id="myDiv",
            ),
            html.Div(id="LinkOutCountry"),
        ],
        lg=6,
    )

    return worldcloud_graph


def word_cloud_sydney():
    n_selection = 100
    n_float = float(n_selection / 100)
    local_df = sample_data(GLOBAL_DF, n_float)
    wordcloud = plotly_wordcloud(local_df)

    worldcloud_graph = dbc.Col(
        [
            html.H3(
                "Sydney Word Cloud",
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
                    figure=wordcloud,
                    config={"displayModeBar": False},
                    id="choropleth",
                ),
                id="myDiv",
            ),
            html.Div(id="LinkOutCountry"),
        ],
        lg=6,
    )

    return worldcloud_graph

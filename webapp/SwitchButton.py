from dash import html, dcc
import dash


def radioSwitchButton_section_one():
    return html.Div(
        children=[
            html.H3(children="Select Sentiments"),
            dcc.RadioItems(
                id="radio-button-section-one",
                options=[
                    {
                        "label": [
                            html.Span(
                                "Positive",
                                style={
                                    "font-size": 15,
                                    "padding-left": 10,
                                    "padding-right": 10,
                                },
                            ),
                            html.Img(
                                src="/assets/positive.svg",
                                height=30,
                                style={"padding-right": 20},
                            ),
                        ],
                        "value": "POSITIVE",
                    },
                    {
                        "label": [
                            html.Span(
                                "Negative",
                                style={
                                    "font-size": 15,
                                    "padding-left": 10,
                                    "padding-right": 10,
                                },
                            ),
                            html.Img(
                                src="/assets/negative.svg",
                                height=30,
                                style={"padding-right": 20},
                            ),
                        ],
                        "value": "NEGATIVE",
                    },
                    {
                        "label": [
                            html.Span(
                                "All",
                                style={
                                    "font-size": 15,
                                    "padding-left": 10,
                                    "padding-right": 10,
                                },
                            ),
                            html.Img(
                                src="/assets/world.svg",
                                height=30,
                                style={"padding-right": 20},
                            ),
                        ],
                        "value": "ALL",
                    },
                ],
                value="ALL",
                inline=True,
            ),
        ]
    )

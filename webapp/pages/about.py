# COMP90024 – Cluster and Cloud Computing - Team 4
# Assignment 2 – Australia Social Media Analytics on the Cloud
# Melbourne, Australia
#
# 1405461 - Andres Gutierrez
# 1110071 - Haining Xie
# 1025543 - Hernán Romano
# 1132915 - Zixuan Xiao
# 1298396 – Claudia Caro

import json
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from common import breadcrumb_layout

dash.register_page(__name__, path="/", title="Home - Team 4")


### load contributors, reasearch team
research_team = json.load(open("static_files/profiles.json"))["research_team"]


### functions for different part of about us page
def _about():
    return dbc.Col(
        [
            html.H1("About"),
            html.P(
                "This project is focused on the technical challenges when analysing a large data set."
            ),
            html.P(
                "The analytical platform makes use of data sets from the Twitter Platform to better understand how social media data can be used to augment the official data available within the Spatial Urban Data Observatory (SUDO) platform."
            ),
            html.P(
                [
                    """
The cloud web application is deployed in Unimelb Research Cloud in an automated environment to tell an interesting story of life in Australian,
                    """,
                    html.A(
                        "details results are available in here",
                        href="https://github.com/hromanoc/202302-COMP90024-Assignment-2",
                    ),
                    ".",
                ]
            ),
        ],
        lg=6,
    )


def _mission():
    return dbc.Col(
        [
            html.Div(
                dbc.Container(
                    dbc.Row(
                        dbc.Col(
                            [
                                html.H1(
                                    "Our Mission",
                                    className="display-4",
                                ),
                                html.Hr(),
                                html.P(
                                    html.Ul(
                                        [
                                            html.Li(
                                                "To provide insights about Australian Culture.",
                                                className="lead",
                                            ),
                                            html.Li(
                                                "To enrich data with common social media platforms.",
                                                className="lead",
                                            ),
                                        ],
                                    ),
                                ),
                            ]
                        ),
                    ),
                    className="px-4",
                ),
                className="bg-light rounded-3 py-5 mb-4",
            ),
        ],
        lg=6,
    )


def _builtby():
    return dbc.Col(
        [
            html.Div(
                dbc.Container(
                    dbc.Row(
                        dbc.Col(
                            [
                                html.A(
                                    [
                                        html.Img(
                                            src="/assets/unimelb-horizontal.png",
                                            height="200px",
                                        )
                                    ],
                                    href="https://www.unimelb.edu.au/",
                                ),
                            ],
                            className="text-center",
                        ),
                    ),
                    className="px-4",
                ),
                className="rounded-3 py-5 mb-4",
            ),
        ],
        lg=12,
    )


def parse_team_structure():
    return dbc.Col(
        [
            html.Div(
                dbc.Container(
                    dbc.Row(
                        dbc.Col(
                            [
                                html.A(
                                    [
                                        html.Img(
                                            src="/assets/team_structure.png",
                                            height="960px",
                                        )
                                    ],
                                    href="/assets/team_structure.png",
                                    target="_blank",
                                ),
                            ],
                            className="text-center",
                        ),
                    ),
                    className="px-4",
                ),
                className="rounded-3 py-5 mb-4",
            ),
        ],
        lg=12,
    )


def parse_planning_gantt():
    return dbc.Col(
        [
            html.Div(
                dbc.Container(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.A(
                                            [
                                                html.Img(
                                                    src="/assets/gantt-chart.png",
                                                    height="258px",
                                                )
                                            ],
                                            href="/assets/gantt-chart.png",
                                            target="_blank",
                                        ),
                                    ],
                                    className="text-center",
                                ),
                            ]
                        ),
                    ],
                    className="px-4",
                ),
                className="rounded-3 py-5 mb-4",
            ),
        ],
        lg=12,
    )


def parse_planning_jira():
    return dbc.Col(
        [
            html.Div(
                dbc.Container(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.A(
                                            [
                                                html.Img(
                                                    src="/assets/jira-roadmap.png",
                                                    height="258px",
                                                )
                                            ],
                                            href="/assets/jira-roadmap.png",
                                            target="_blank",
                                        ),
                                    ],
                                    className="text-center",
                                ),
                            ]
                        ),
                    ],
                    className="px-4",
                ),
                className="rounded-3 py-5 mb-4",
            ),
        ],
        lg=4,
    )


def parse_planning_slack():
    return dbc.Col(
        [
            html.Div(
                dbc.Container(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.A(
                                            [
                                                html.Img(
                                                    src="/assets/slack.png",
                                                    height="258px",
                                                )
                                            ],
                                            href="/assets/slack.png",
                                            target="_blank",
                                        ),
                                    ],
                                    className="text-center",
                                ),
                            ]
                        ),
                    ],
                    className="px-4",
                ),
                className="rounded-3 py-5 mb-4",
            ),
        ],
        lg=4,
    )


def parse_planning_github():
    return dbc.Col(
        [
            html.Div(
                dbc.Container(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.A(
                                            [
                                                html.Img(
                                                    src="/assets/github.png",
                                                    height="258px",
                                                )
                                            ],
                                            href="/assets/github.png",
                                            target="_blank",
                                        ),
                                    ],
                                    className="text-center",
                                ),
                            ]
                        ),
                    ],
                    className="px-4",
                ),
                className="rounded-3 py-5 mb-4",
            ),
        ],
        lg=4,
    )


def parse_architecture_components():
    return dbc.Col(
        [
            html.Div(
                dbc.Container(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.A(
                                            [
                                                html.Img(
                                                    src="/assets/architecture-components.png",
                                                    height="951px",
                                                )
                                            ],
                                            href="/assets/architecture-components.png",
                                            target="_blank",
                                        ),
                                    ],
                                    className="text-center",
                                ),
                            ]
                        ),
                    ],
                    className="px-4",
                ),
                className="rounded-3 py-5 mb-4",
            ),
        ],
        lg=12,
    )


def parse_architecture_data():
    return dbc.Col(
        [
            html.Div(
                dbc.Container(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.A(
                                            [
                                                html.Img(
                                                    src="/assets/architecture-data.png",
                                                    height="258px",
                                                )
                                            ],
                                            href="/assets/architecture-data.png",
                                            target="_blank",
                                        ),
                                    ],
                                    className="text-center",
                                ),
                            ]
                        ),
                    ],
                    className="px-4",
                ),
                className="rounded-3 py-5 mb-4",
            ),
        ],
        lg=6,
    )


def parse_architecture_infrastructure():
    return dbc.Col(
        [
            html.Div(
                dbc.Container(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.A(
                                            [
                                                html.Img(
                                                    src="/assets/architecture-infrastructure.png",
                                                    height="258px",
                                                )
                                            ],
                                            href="/assets/architecture-infrastructure.png",
                                            target="_blank",
                                        ),
                                    ],
                                    className="text-center",
                                ),
                            ]
                        ),
                    ],
                    className="px-4",
                ),
                className="rounded-3 py-5 mb-4",
            ),
        ],
        lg=6,
    )


def _section_title(title):
    return dbc.Col(
        html.H2(
            title,
            style={"margin-bottom": "32px"},
        ),
        lg=12,
    )


def parse_people(person_list):
    icon_map = {
        "home": "fas fa-home",
        "github": "fab fa-github",
        "work": "fas fa-building",
        "university": "fa fa-university",
    }

    return [
        dbc.Col(
            [
                html.Img(
                    src=person_dict["image_url"],
                    height="148px",
                    className="rounded-circle shadow",
                ),
                html.H5(
                    person_dict["name"],
                    className="mt-4 font-weight-medium mb-0",
                ),
                html.H6(
                    person_dict["affiliation"],
                    className="subtitle mb-3 text-muted",
                ),
            ]
            + (
                [
                    html.Ul(
                        [
                            html.Li(
                                html.A(
                                    html.I(
                                        className=f"{icon_map[link_type]} fa-lg mr-3"
                                    ),
                                    href=link_value,
                                ),
                                className="list-inline-item",
                            )
                            for link_type, link_value in person_dict["links"].items()
                        ],
                        className="list-inline",
                    )
                ]
                if "links" in person_dict
                else []
            )
            + [
                html.P(person_dict["bio"], className="text-justify"),
            ],
            lg=4,
            sm=6,
            className="text-center mb-5",
        )
        for person_dict in person_list
    ]


def parse_poweredby(filepath):
    with open(filepath) as poweredby_file:
        poweredby_list = json.load(poweredby_file)

        return [
            dbc.Col(
                [
                    html.A(
                        [
                            html.Img(
                                src=poweredby_dict["image_url"],
                                height="96px",
                                style={"margin-bottom": "8px"},
                            ),
                            html.H5(poweredby_dict["name"]),
                        ],
                        href=poweredby_dict["url"],
                    )
                ],
                lg=2,
                md=3,
                xs=6,
                className="text-center",
                style={"margin-bottom": "16px"},
            )
            for poweredby_dict in poweredby_list
        ]


def _disclaimer():
    return dbc.Col(
        [
            html.P(
                [
                    "This educational website was inspired by the open source plotly project: ",
                    html.A(
                        "Financial Forecasting",
                        href="https://plotly.com/examples/finance/",
                    ),
                ]
            ),
        ]
    )


def _contactus():
    return dbc.Col(
        [
            html.P(
                "Questions or suggestions? Feel free to reach out to the team by emailing"
            ),
            html.P("We will endeavour to address your query as soon as possible."),
        ]
    )


def body_layout():
    return dbc.Container(
        [
            breadcrumb_layout([("Home", "/"), ("About", "")]),
            dbc.Row(
                [
                    _about(),
                    _mission(),
                ]
            ),
            dbc.Row([_builtby()]),
            dbc.Row(_section_title("Research Group")),
            dbc.Row(parse_people(research_team)),
            dbc.Row(_section_title("Team Structure")),
            dbc.Row(parse_team_structure()),
            dbc.Row(_section_title("Planning")),
            dbc.Row(parse_planning_gantt()),
            dbc.Row(
                [parse_planning_jira(), parse_planning_slack(), parse_planning_github()]
            ),
            dbc.Row(_section_title("Architecture")),
            dbc.Row(parse_architecture_components()),
            dbc.Row([parse_architecture_data(), parse_architecture_infrastructure()]),
            dbc.Row(_section_title("Powered By")),
            dbc.Row(
                parse_poweredby("static_files/poweredby.json"),
                className="mb-5",
            ),
            dbc.Row(_section_title("Disclaimer")),
            dbc.Row(_disclaimer()),
            dbc.Row(_section_title("Contact us")),
            dbc.Row(_contactus()),
        ],
        style={"margin-bottom": "64px"},
        className="mb-5",
    )


layout = html.Div([dcc.Location(id="url", refresh=False), body_layout()])

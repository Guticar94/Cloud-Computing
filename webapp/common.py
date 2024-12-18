# COMP90024 – Cluster and Cloud Computing - Team 4
# Assignment 2 – Australia Social Media Analytics on the Cloud
# Melbourne, Australia
#
# 1405461 - Andres Gutierrez
# 1110071 - Haining Xie
# 1025543 - Hernán Romano
# 1132915 - Zixuan Xiao
# 1298396 – Claudia Caro

from dash import html
import dash_bootstrap_components as dbc
import pandas as pd

DF_TRENDING_TOPIC = pd.read_csv("./data/radar_data.csv")

home_route = ("COMP90024 - Team 4", "/about/")

nav_routes = [
    ("Twitter vs Mastodon", "/twitter_vs_mastodon/"),
    ("Sudo vs Social Media", "/sudo_vs_social_media/"),
    ("About", "/about/"),
]


def header():
    return dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.A(
                                [
                                    html.Img(
                                        src="/assets/unimelb-white.png",
                                        height="30px",
                                    )
                                ],
                                href="https://handbook.unimelb.edu.au/subjects/comp90024/",
                            )
                        ),
                        dbc.Col(
                            dbc.NavbarBrand(
                                "COMP90024 - Team 4",
                                className="ms-2",
                                href="/",
                                external_link=True,
                            )
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                dbc.Col(
                    dbc.Row(
                        [
                            dbc.NavbarToggler(id="navbar-toggler"),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavItem(
                                            dbc.NavLink(
                                                x[0],
                                                href=x[1],
                                                external_link=True,
                                            )
                                        )
                                        for x in nav_routes
                                    ],
                                    # make sure nav takes up the full width for auto
                                    # margin to get applied
                                    className="w-100",
                                ),
                                id="navbar-collapse",
                                is_open=False,
                                navbar=True,
                            ),
                        ],
                        # the row should expand to fill the available horizontal space
                        className="flex-grow-1",
                    ),  # close row
                    lg="expand",
                ),  # close col
            ],
        ),  # close containter
        color="dark",
        dark=True,
    )


def breadcrumb_layout(crumbs):
    return dbc.Nav(
        [
            html.Ol(
                [
                    html.Li(
                        html.A(crumb[0], href=crumb[1]),
                        className="breadcrumb-item",
                    )
                    for crumb in crumbs[:-1]
                ]
                + [
                    html.Li(
                        crumbs[-1][0],
                        id="breadcrumb",
                        className="breadcrumb-item active",
                    )
                ],
                className="breadcrumb",
            )
        ],
        navbar=True,
        class_name="bg-light rounded-3 px-3 pt-3 mb-3",
    )


def footer():
    return dbc.Container(
        [
            dbc.Row(
                dbc.Col(html.Hr(style={"margin-top": "64px"}), lg=12),
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Nav(
                                [
                                    dbc.NavItem(
                                        dbc.NavLink(x[0], href=x[1], external_link=True)
                                    )
                                    for x in [home_route] + nav_routes
                                ],
                                vertical="md",
                            )
                        ],
                        lg=7,
                        style={"margin-bottom": "16px"},
                    ),
                ],
                style={"margin-bottom": "64px"},
            ),
        ]
    )

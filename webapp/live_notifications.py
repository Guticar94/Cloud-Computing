# COMP90024 – Cluster and Cloud Computing - Team 4
# Assignment 2 – Australia Social Media Analytics on the Cloud
# Melbourne, Australia
#
# 1405461 - Andres Gutierrez
# 1110071 - Haining Xie
# 1025543 - Hernán Romano
# 1132915 - Zixuan Xiao
# 1298396 – Claudia Caro

from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

from NotificationController import NotificationController

notification_controller = NotificationController()


def live_mastodon_notifications():
    return [
        dbc.Toast(
            id="toast",
            header="New data received!",
            is_open=False,
            dismissable=True,
            icon="primary",
            style={"position": "fixed", "bottom": 10, "right": 10, "width": 350},
            children=[html.P("This is the toast body")],
        ),
        dcc.Interval(
            id="interval-component",
            interval=1 * 5000,  # in milliseconds
            n_intervals=0,
        ),
    ]


@callback(
    [Output("toast", "is_open"), Output("toast", "children")],
    Input("interval-component", "n_intervals"),
)
def display_confirm(n):
    # Check if new data is received here

    latest_toots = notification_controller.get_latest_toots_from_CouchDB_Cluster(
        notification_controller.last_toot_id_reviewed
    )
    total_latest_toots = len(latest_toots["rows"])
    if total_latest_toots > 1:
        total_number_of_new_toots = total_latest_toots - 1
        if total_number_of_new_toots > 1:
            message = f"New data received! {total_number_of_new_toots} new toots"
        else:
            message = f"New data received! {total_number_of_new_toots} new toot"
        new_toots = [
            html.P(
                f'User account: {toot["value"]["account"]}. Message: {toot["value"]["content"]}'
            )
            for toot in latest_toots["rows"][1:]
        ]
        notification_controller.last_toot_id_reviewed = latest_toots["rows"][-1]["key"]
        return (
            True,
            [html.P(message)] + new_toots,
        )
    return False, [html.P("")]

# COMP90024 – Cluster and Cloud Computing - Team 4
# Assignment 2 – Australia Social Media Analytics on the Cloud
# Melbourne, Australia
#
# 1405461 - Andres Gutierrez
# 1110071 - Haining Xie
# 1025543 - Hernán Romano
# 1132915 - Zixuan Xiao
# 1298396 – Claudia Caro

from dash import Dash, html, page_container  # pip install dash
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from common import header, footer
from dash import html

# Build your components
app = Dash(
    __name__,
    url_base_pathname="/",
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

app.layout = html.Div(
    [
        header(),
        page_container,
        footer(),
    ]
)


# Run app
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8051)

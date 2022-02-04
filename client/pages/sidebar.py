import dash_bootstrap_components as dbc
from dash import html, Output, Input

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# sidebar for client
client_sidebar = html.Div(
    [
    ],
    style=SIDEBAR_STYLE,
)
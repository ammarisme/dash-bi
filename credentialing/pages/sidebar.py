import dash_bootstrap_components as dbc
from dash import html

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

# sidebar for credentialing
credentialing_sidebar = html.Div(
    [
        #html.H5("Credentialing"),
        #className="display-4"
        #html.Hr(),
        html.P("Credentialing App",
               className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/credentialing", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)



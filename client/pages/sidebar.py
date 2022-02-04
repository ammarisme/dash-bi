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
        #html.H5("Credentialing"),
        #className="display-4"
        #html.Hr(),
        html.P("Client Dashboard",
               className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Summary", href="/client", active="exact"),
                dbc.NavLink("Claims", href="/client/cliams", active="exact"),
                dbc.NavLink("Charges", href="/client/charges", active="exact"),
                dbc.NavLink("Deposits", href="/client/deposits", active="exact"),
                dbc.NavLink("AR", href="/client/ar", active="exact"),
                dbc.NavLink("GEO", href="/client/geo", active="exact"),
                dbc.NavLink("Denial", href="/client/denial", active="exact"),
                dbc.NavLink("Reimburse", href="/client/reimburse", active="exact"),
                dbc.NavLink("Cliam Detail", href="/client/cliam_detail", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
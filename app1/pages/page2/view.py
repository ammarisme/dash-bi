from dash import html, dcc
from dash.dependencies import Output, Input

from dash_app.app import app

# html layout
page2_layout = html.Div([
    html.H3('App 2'),
    dcc.Dropdown(id='app-2-dropdown',
                 options=[{
                     'label': 'App 2 - {}'.format(i),
                     'value': i
                 } for i in ['NYC', 'MTL', 'LA']]),
    html.Div(id='app-2-display-value'),
    dcc.Link('Go to App 1', href='/app/1/')
])


# callbacks
@app.callback(Output('app-2-display-value', 'children'),
              Input('app-2-dropdown', 'value'),
              prevent_initial_call=True)
def display_value(value):
    return 'You have selected "{}"'.format(value)

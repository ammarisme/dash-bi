from dash import html, dcc
from dash.dependencies import Output, Input
import plotly.express as px
from dash_app.app import app
import dash_bootstrap_components as dbc
from credentialing.pages.filters import *
from credentialing.utils import *
from dash_app.base.reuse.cache_resue import *
from dash_app.base.reuse.filter_reuse import *
from dash import dash_table
from dash import html
from flask_caching import Cache
import dash
from dash_app.base.model import Model
from datetime import date
from datetime import date,timedelta
from dateutil.relativedelta import relativedelta
from flask import request

model=Model()

################# callback ###########


@app.callback(
    Output("charges-graph","figure"),
    Input('url', 'pathname')
    )
def update_charge_plot(pathname):
    license_key = request.headers.environ.get('HTTP_REFERER').split('?')[1].split('=')[1]
    data_138192 = model.csv_to_dataframe(csv='summary_charge_data.csv')
    data_144452 = model.csv_to_dataframe(csv='summary_charge- 2023.csv')

    if license_key == '138192':
        pandas_data = data_138192
    else:
        pandas_data = data_144452

    fig = px.bar(pandas_data, x='year_month', y='charge')

    return fig


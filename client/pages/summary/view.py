import urllib

from dash import html, dcc
from dash.dependencies import Output, Input
import plotly.express as px
from dash_app.app import app
import dash_bootstrap_components as dbc
from credentialing.pages.filters import *
from credentialing.utils import *
from dash_app.base.reuse.cache_resue import *
from dash_app.base.reuse.filter_reuse import *
from client.pages.summary.callbacks import *
from dash import dash_table
from dash import html
from flask_caching import Cache
import dash
from dash_app.base.model import Model
from datetime import date
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

test_list = []
test_list.append({'label': "Select-All", 'value': "Select-All"})
test_list.append({'label': "one", 'value': "one"})
test_list.append({'label': "two", 'value': "two"})
test_list.append({'label': "three", 'value': "three"})
test_list.append({'label': "four", 'value': "four"})

################### dropdown card ####################

# comparsion period dropdown 

# sales rep dropdown
# sales_rep_card = dbc.Card(
#     [
#         html.H5("Sales Rep", className="card-title"),
#
#         dcc.Dropdown(id="sales_group", options=test_list, multi=True, optionHeight=40,
#                      value=['Select-All']),
#     ],
#
#     color="light", outline=True)

# Facility(LIS) dropdown

# facility_card = dbc.Card(
#     [
#         html.H5("Facility(LIS)", className="card-title"),
#
#         dcc.Dropdown(id="facility", options=test_list, multi=True, optionHeight=40,
#                      value=['Select-All']),
#     ],
#
#     color="light", outline=True)

################### kpi card ######################

#################### chart ####################
# monthly charges_plot

charges_plot = dbc.Card(
    [
        dbc.CardHeader("Monthly Charges"),
        dbc.CardBody(
            [
                dcc.Graph(id="charges-graph"),
            ]
        ),
    ],

)

####################### main layout##################

layout = html.Div(children=[

    html.Div([

        # dropdown card
        # html.Div(dbc.Row(
        #     [
        #         dbc.Col(comparison_period_card),
        #         dbc.Col(cpt_card),
        #         dbc.Col(test_type_card),
        #         dbc.Col(sales_group_card),
        #
        #     ],
        #     class_name="mb-2")
        #
        # ),

        # dropdown card
        # html.Div(date_type_card),
        # dropdown card

        # html.H4(children='Executive Summary'),

        html.Div(dbc.Row(
            [
                dbc.Col(charges_plot, md=6),
            ],
            class_name="mb-2")
        ),
    ]),

], style={'padding': 60})  # add the outside padding
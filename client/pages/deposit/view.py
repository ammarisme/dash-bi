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


test_list = []
test_list.append({'label':"Select-All",'value':"Select-All"})
test_list.append({'label':"one",'value':"one"})
test_list.append({'label':"two",'value':"two"})
test_list.append({'label':"three",'value':"three"})
test_list.append({'label':"four",'value':"four"})

################### dropdown card ####################

# comparsion period dropdown 
comparison_period_card = dbc.Card(
            [
                html.H5("Comparison Period", className="card-title"),
                dcc.Dropdown(id = "comparsion_period" ,options= test_list, multi=True, optionHeight=40,
                        value = ['Select-All'] )
                        
            ],
color="light",outline=True)



# CPT dropdown 
cpt_card = dbc.Card(
            [
                html.H5("CPT", className="card-title"),
                dcc.Dropdown(id = "cpt" ,options= test_list, multi=True, optionHeight=40,
                        value = ['Select-All'] )
                        
            ],
color="light",outline=True)



# Test type dropdown
test_type_card = dbc.Card(
                [
                html.H5("Test Type", className="card-title"),
                dcc.Dropdown(id = "test_type" ,options= test_list, multi=True, optionHeight=40,
                        value = ['Select-All']),
            ],

color="light",outline=True)



# sales group dropdown
sales_group_card = dbc.Card(
               [
                html.H5("Sales Group", className="card-title"),

                dcc.Dropdown(id = "sales_group" ,options= test_list, multi=True,optionHeight=40,
                        value = ['Select-All']),
            ],

color="light",outline=True)

# sales rep dropdown
sales_rep_card = dbc.Card(
               [
                html.H5("Sales Rep", className="card-title"),

                dcc.Dropdown(id = "sales_group" ,options= test_list, multi=True,optionHeight=40,
                        value = ['Select-All']),
            ],

color="light",outline=True)


# Facility(LIS) dropdown

facility_card = dbc.Card(
               [
                html.H5("Facility(LIS)", className="card-title"),

                dcc.Dropdown(id = "facility" ,options= test_list, multi=True,optionHeight=40,
                        value = ['Select-All']),
            ],

color="light",outline=True)


# Financial Class dropdown

financial_class_card = dbc.Card(
               [
                html.H5("Financial Class", className="card-title"),

                dcc.Dropdown(id = "financial_class" ,options= test_list, multi=True,optionHeight=40,
                        value = ['Select-All']),
            ],

color="light",outline=True)

# payor dropdown

payor_card = dbc.Card(
               [
                html.H5("Payor", className="card-title"),

                dcc.Dropdown(id = "payor" ,options= test_list,optionHeight=40,
                multi=True,value =['Select-All']),
            ],

color="light",outline=True)


# Ref provider dropdown

ref_provider_card = dbc.Card(
               [
                html.H5("Ref Provider", className="card-title"),

                dcc.Dropdown(id = "ref_provider" ,options= test_list,optionHeight=40,
                multi=True, value =['Select-All']),
            ],

color="light",outline=True)

# date_type dropdown list
date_type_card = dbc.Card(
    [
        html.Div(
            [
                html.Br(),
                # date type radio item
                dcc.RadioItems(id="date_type_class",options=[{"label":"DOE","value":"DOE"},
                                                         {"label":"DOS","value":"DOS"}],
                           value='DOE'),
            ]
        ),
    ],
color="light",outline=True)



####################### main layout##################


deposits_layout =html.Div(children=[
    
    html.Br(),
    # HRC logo 
    html.Img(src=app.get_asset_url('HRC.png'),style={'display':'inline-block','width':'42px','height':'42px'}),
    # heading 
    html.H1("HealthRecon Connect", className="text-info",style={'display':'inline-block'}),
    html.Br(),
    html.Br(),
    html.Br(),
    

    html.Div([


                # dropdown card
                html.Div(dbc.Row(
                    [
                        dbc.Col(comparison_period_card),
                        dbc.Col(cpt_card),
                        dbc.Col(test_type_card),
                        dbc.Col(sales_group_card),
                        

                    ],
                class_name="mb-2")

                ),

                # dropdown card
                html.Div(dbc.Row(
                    [
                        dbc.Col(facility_card),
                        dbc.Col(financial_class_card),
                        dbc.Col(payor_card),
                        dbc.Col(ref_provider_card),

                    ],
                class_name="mb-2")

                ),

                html.Div(date_type_card),


    ]),



],style={'padding': 60}) # add the outside padding 


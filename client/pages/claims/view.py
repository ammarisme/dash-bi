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

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
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




################# Plot #####################

monthly_cliams_plot = dbc.Card(
    [
        dbc.CardHeader("Monthly Cliams"),
        dbc.CardBody(
            [
                dcc.Graph(id="monthly-cliams-graph"),
            ]
        ),
    ],

)



####################### Tabs and table ####################

@app.callback(Output('cliams-tabs-content', 'children'),
              [Input('cliams-tabs', 'value')])

def render_content(tab):
    if tab == 'cpt_tab':
        return html.Div([
                html.Br(),
                dash_table.DataTable(
                id='table-10',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
            )

        ])
        # end of the first tab

    elif tab == 'finincal_class_tab':
        return html.Div([
            dash_table.DataTable(
                id='table-6',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
            )
                

        ])
    elif tab == 'payor_tab':
        return html.Div([
            html.Br(),
            dash_table.DataTable(
                id='table-7',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
            )

        ]),
    # end of third tab
    elif tab == 'ref_provider_tab':
        return html.Div([
            html.Br(),
            dash_table.DataTable(
                id='table-8',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
            )


    ])
    elif tab == 'facility_tab':
        return html.Div([
            html.Br(),
            dash_table.DataTable(
                id='table-9',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
            )

    ])



####################### main layout##################


cliams_layout =html.Div(children=[
    
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

                                html.Br(),

                html.Div(monthly_cliams_plot),

                html.Br(),

                
               

                 # tabs
                dcc.Tabs(id="cliams-tabs", value='cpt_tab',children=[
                    dcc.Tab(label='CPT', value='cpt_tab'),
                    dcc.Tab(label='FININCAL CLASS', value='finincal_class_tab',className='finincal-class-tap-icon'),
                    dcc.Tab(label='PAYOR',value='payor_tab',className='payor-tap-icon'),
                    dcc.Tab(label='REFERRING PROVIDER', value='ref_provider_tab',className='ref-provider-tap-icon'),
                    dcc.Tab(label='RENDERING FACILITY',value='facility_tab',className='facility-tap-icon')
                ]),

                html.Div(id='cliams-tabs-content')



    ]),



],style={'padding': 60}) # add the outside padding 



################ callback ###################

@app.callback(
    Output("monthly-cliams-graph","figure"),
    [Input("financial_class","value")],

    )

def update_monthly_cliam_plot(fin_class,):
    

    data_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(data_canada, x='year', y='pop')

    fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Cliams in $")

    return fig
   
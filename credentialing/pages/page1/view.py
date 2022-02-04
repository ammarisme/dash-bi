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


################### dropdown card ####################


# summary and follow up sbu dropdown
sbu_card = dbc.Card(
            [
                html.H5("SBU", className="card-title"),
                dcc.Dropdown(id = "sbu" ,options= sbu_list, multi=True, optionHeight=40,
                        value = ['Select-All'] )
                        
            ],
color="light",outline=True)



# summary and follow up office key dropdown
office_key_card = dbc.Card(
                [
                html.H5("Office Key", className="card-title"),
                dcc.Dropdown(id = "office_key" ,options= office_key_list, multi=True, optionHeight=40,
                        value = ['Select-All']),
            ],

color="light",outline=True)



# summary and follow up client name dropdown
client_name_card = dbc.Card(
               [
                html.H5("Client Name", className="card-title"),

                dcc.Dropdown(id = "client_name" ,options= client_name_list, multi=True,optionHeight=40,
                        value = ['Select-All']),
            ],

color="light",outline=True)

# agent level sbu head dropdown

agent_sbu_card = dbc.Card(
               [
                html.H5("SBU Head", className="card-title"),

                dcc.Dropdown(id = "sbu_head" ,options= agent_sbu_head_list, multi=True,optionHeight=40,
                        value = ['Select-All']),
            ],

color="light",outline=True)


# agent level agent dropdown

agent_name_card = dbc.Card(
               [
                html.H5("Agent", className="card-title"),

                dcc.Dropdown(id = "agent_name" ,options= agent_list, multi=True,optionHeight=40,
                        value = ['Select-All']),
            ],

color="light",outline=True)



date_filter_card = dbc.Card(
               [
                html.H5("Date Range", className="card-title"),

                dcc.Dropdown(id = "date_range" ,options= filter_date_list,optionHeight=40,
                clearable=False, value ='Last_three_month'),
            ],

color="light",outline=True)


date_range_card = dbc.Card(
               [
                html.H5("Date Range Calendar", className="card-title"),
                dcc.DatePickerRange(
                id='date_range_picker',
                clearable=True,
                display_format="MM/DD/YYYY",
                max_date_allowed=date.today(),   
            )
            ],

color="light",outline=True)




###########################  KPI Card  #####################

#################  Summary_Rejected_Rate

summary_approval_rate_query = '''
SELECT NULLIF([Approval_Rate],0) as Approval_Rate
  FROM [Credentialing_Dashboard].[dbo].[Credentialling_Summary_Approval_Rate]
'''
summary_approval_rate_df= cache_query_df(summary_approval_rate_query)

   
summary_approval_rate = summary_approval_rate_df['Approval_Rate'].round(2).astype(str).add('%')



approval_rate = dbc.Card(
    [
        dbc.CardHeader("Approval Rate(Last three month)"),
        dbc.CardBody(
            [
                html.H4(summary_approval_rate, className="card-title"),
            ]
        ),
    ],

)


#################  Summary_Rejected_Rate

summary_rejected_rate_query = '''
SELECT [Rejected_Rate]
  FROM [Credentialing_Dashboard].[dbo].[Credentialling_Summary_Rejected_Rate]
'''
summary_rejected_rate_df= cache_query_df(summary_rejected_rate_query)   

# round the percentage into 2 decimal point and add the percentage symbol
summary_rejected_rate = summary_rejected_rate_df['Rejected_Rate'].round(2).astype(str).add('%')


rejection_rate = dbc.Card(
    [
        dbc.CardHeader("Rejection Rate(Last three month)"),
        dbc.CardBody(
            [
                html.H4(summary_rejected_rate, className="card-title"),
            ]
        ),
    ],

)



########## summary average_processing_period KPI 

average_processing_period_query='''
SELECT [APT]
  FROM [Credentialing_Dashboard].[dbo].[Credentialling_Summary_Average_Processing_Period]
'''

average_processing_period_df= cache_query_df(average_processing_period_query)

# round the percentage into 2 decimal point and add the percentage symbol
average_processing_period = average_processing_period_df['APT'].astype(str).add(' days')

processing_period = dbc.Card(
    [
        dbc.CardHeader("Average processing period"),
        dbc.CardBody(
            [
                html.H4(average_processing_period, className="card-title"),
            ]
        ),
    ],

)

# Add current date into the title
monthly_progress_title = "Credentialing Monthly Progress ("+date.today().strftime("%m/%d/%Y") + ")"
follow_up_title = "Follow-up Due Volume - As of ("+ date.today().strftime("%m/%d/%Y") + ")"
daily_follow_up_title = "Daily Follow-ups by SBU and Client ("+ date.today().strftime("%m/%d/%Y") + ")"


####################### Tabs and table ####################

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])

def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
                
                html.Br(),
                html.Br(),
                
                
                # dropdown card
                html.Div(dbc.Row(
                    [
                        dbc.Col(sbu_card),
                        dbc.Col(office_key_card),
                        dbc.Col(client_name_card)
                    ],
                class_name="mb-4")

                ),

                html.Br(),
                html.Div(dbc.Row(
                            [
                                dbc.Col(approval_rate),
                                dbc.Col(rejection_rate),
                                dbc.Col(processing_period)
                            ],
                        class_name="mb-2")

                        ),
                html.Br(),
                html.Br(),

                
                html.H4(children='Credentialing Status Breakdown (#)'),
                html.Br(),

                html.Div(id="status_breakdown_table"),

                html.Br(),
                html.Br(),
                html.H4(children='Credentialing Status Breakdown (%)'),
                html.Br(),

                html.Div(id="status_breakdown_percentage_table"),

                html.Br(),
                
                html.H4(children=monthly_progress_title),
                
                html.Br(),
                html.Div(id="monthly_progress_table"),


        ])
        # end of the first tab

    elif tab == 'tab-2':
        return html.Div([

                html.Br(),
                html.Br(),

                # dropdown card
                html.Div(dbc.Row(
                    [
                        dbc.Col(sbu_card),
                        dbc.Col(office_key_card),
                        dbc.Col(client_name_card)
                    ],
                class_name="mb-4")

                ),


                html.Br(),
                html.Br(),
                html.H4(children=follow_up_title),
                html.Br(),
                html.Div(id="follow_up_volumne_table"),


                html.Br(),
                html.Br(),
                html.Div(dbc.Row(
                                [
                                    dbc.Col(date_filter_card),
                                    dbc.Col(date_range_card,style={'z-index':'999'}),

                                ],
                        class_name="mb-4")

                        ),
                html.Br(),
                html.Div(id="daily_follow_up_table")

        ])
    elif tab == 'tab-3':
        return html.Div([
                html.Br(),
                html.Br(),
                
                html.Div(dbc.Row(
                                [
                                    dbc.Col(agent_sbu_card),
                                    dbc.Col(agent_name_card),
                                ],
                        class_name="mb-4")

                        ),
                
                html.Br(),
                html.Br(),
                html.Div(dbc.Row(
                                [
                                    dbc.Col(date_filter_card),
                                    dbc.Col(date_range_card,style={'z-index':'999'}),

                                ],
                        class_name="mb-4")

                        ),
                html.Br(),
                html.Div(id="agent_daily_follow_up_table"),


                html.Br(),

                # html.H4(children='Daily Approval Count'),
                # html.Br(),
                # html.Div(id="agent_daily_approval_count_table"),



        ])
        # end of third tab
        



####################### main layout##################


layout =html.Div(children=[
    
    html.Br(),
    # HRC logo 
    html.Img(src=app.get_asset_url('HRC.png'),style={'display':'inline-block','width':'42px','height':'42px'}),
    # heading 
    html.H1("HealthRecon Connect", className="text-info",style={'display':'inline-block'}),
    html.Br(),
    html.Br(),
    # subheading 
    html.H3("Credentialing Analysis", className="text-primary",style={"text-align":"center"}),
    html.Br(),
    html.Br(),
    
    # tabs
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Summary', value='tab-1'),
        dcc.Tab(label='Follow ups', value='tab-2'),
        dcc.Tab(label='Agent Level',value='tab-3')
    ]),
    
    
    # tables
    html.Div(id='tabs-content')

],style={'padding': 60}) # add the outside padding 






################################## callback #############################






###################### Summary ##############################


################ Breakdown table ###############

@app.callback(
        dash.dependencies.Output('status_breakdown_table','children'),
        [dash.dependencies.Input('sbu', 'value')],
        [dash.dependencies.Input('client_name', 'value')],
        [dash.dependencies.Input('office_key', 'value')],
        
        )

def update_breakdown_table(sbu,client_name,office_key):


    # initial string 
    select_all_string = str('SELECT * FROM [Credentialing_Dashboard].[dbo].[Credentialling_Status_Breakdown_Numbers]')
    sbu_string = str()
    client_name_string = str()
    office_key_string = str()


    # if user clear one of the filter, the dash will no update 
    if (len(sbu) < 1 ) or (len(client_name) < 1) or (len(office_key) <1):
        return dash.no_update
    
    filter_model = Filter_query()

    sbu_string = filter_model.filter_sub_string(sbu,'SBU')

    client_name_string = filter_model.filter_sub_string(client_name,'Client_name')

    office_key_string = filter_model.filter_sub_string(office_key,'Office_key')

    query=f"""
                {select_all_string}
                {sbu_string} {client_name_string} {office_key_string} 
            ;
            """ 

    # get the dataframe and cache
    status_breakdown_df = cache_query_df(query)

    status_breakdown_df = status_breakdown_df.rename({'INN_Approved': 'INN-Approved', 'INN_Rejected': 'INN-Rejected',
                                                        'OON_Approved':'OON-Approved','OON_Rejected':'OON-Rejected','Market_Closed':'Market Closed',
                                                        'Last_Six_Month_Billed':'Last Six Month Billed','Office_Key':'Office Key','Client_Name':'Client Name'} ,axis='columns')

    # return the whole html children table

    return html.Div([

        dash_table.DataTable(
        sort_action='native',
        columns=[{"name": i, "id": i} for i in status_breakdown_df.columns],
        data=status_breakdown_df.to_dict("records"),
        fixed_rows={'headers': True},
        style_table={"height": "35vh", "maxHeight": "35vh",'overflowY': 'auto'},
        style_cell={'height': 'auto','minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal','text-align':'center'}
        
    ),

        ]
    
    ),




################ Breakdown percentage ###############



@app.callback(
        dash.dependencies.Output('status_breakdown_percentage_table','children'),
        [dash.dependencies.Input('sbu', 'value')],
        [dash.dependencies.Input('client_name', 'value')],
        [dash.dependencies.Input('office_key', 'value')],
        
        )

def update_percentage_table(sbu,client_name,office_key):


    # initial string 
    select_all_string = str('SELECT * FROM [Credentialing_Dashboard].[dbo].[Credentialling_Status_Breakdown_Percentages]')
    sbu_string = str()
    client_name_string = str()
    office_key_string = str()


    # if user clear one of the filter, the dash will no update 
    if (len(sbu) < 1 ) or (len(client_name) < 1) or (len(office_key) <1):
        return dash.no_update
    
    filter_model = Filter_query()

    sbu_string = filter_model.filter_sub_string(sbu,'SBU')

    client_name_string = filter_model.filter_sub_string(client_name,'Client_name')

    office_key_string = filter_model.filter_sub_string(office_key,'Office_key')

    query=f"""
                {select_all_string}
                {sbu_string} {client_name_string} {office_key_string} 
            ;
            """ 
    status_breakdown_percentage_df= cache_query_df(query)
    
    # round the decimal number into 1
    status_breakdown_percentage_df = status_breakdown_percentage_df.round(1)
    status_breakdown_percentage_df = status_breakdown_percentage_df.rename({'INN_Approved': 'INN-Approved', 'INN_Rejected': 'INN-Rejected',
                                                        'OON_Approved':'OON-Approved','OON_Rejected':'OON-Rejected','Market_Closed':'Market Closed',
                                                        'Last_Six_Month_Billed':'Last Six Month Billed','Office_Key':'Office Key','Client_Name':'Client Name'} ,axis='columns')

    
    
    #  add the percentage symbol 
    add_percentage_list = ['INN-Approved','INN-Rejected','OON-Approved','OON-Rejected','Market Closed','Pending','In-Process','On-Hold','Other']
    for i in add_percentage_list:

        status_breakdown_percentage_df[i] = status_breakdown_percentage_df[i].astype(str).add('%')
    # return the whole html children table
    return html.Div([

        dash_table.DataTable(
        sort_action='native',
        columns=[{"name": i, "id": i} for i in status_breakdown_percentage_df.columns],
        data=status_breakdown_percentage_df.to_dict("records"),
        fixed_rows={'headers': True},
        style_table={"height": "35vh", "maxHeight": "35vh",'overflowY': 'auto'},
        style_cell={'height': 'auto','minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal','text-align':'center'}
    )

        ]
    )


    
#################### Follows Up ##########################




########################## Monthly Progress ################################




@app.callback(
        dash.dependencies.Output('monthly_progress_table','children'),
        [dash.dependencies.Input('sbu', 'value')],
        [dash.dependencies.Input('client_name', 'value')],
        [dash.dependencies.Input('office_key', 'value')],
        
        )

def update_monthly_progress_table(sbu,client_name,office_key):

        # initial string 
    select_all_string = str('SELECT * FROM [Credentialing_Dashboard].[dbo].[Credentialling_Monthly_Progresss]')
    sbu_string = str()
    client_name_string = str()
    office_key_string = str()


    # if user clear one of the filter, the dash will no update 
    if (len(sbu) < 1 ) or (len(client_name) < 1) or (len(office_key) <1):
        return dash.no_update
    
    filter_model = Filter_query()

    sbu_string = filter_model.filter_sub_string(sbu,'SBU')

    client_name_string = filter_model.filter_sub_string(client_name,'Client_name')

    office_key_string = filter_model.filter_sub_string(office_key,'Office_key')

    query=f"""
                {select_all_string}
                {sbu_string} {client_name_string} {office_key_string} 
            ;
            """ 

    monthly_progress_df= cache_query_df(query)
        
    monthly_progress_df = monthly_progress_df.rename({'INN_Approved': 'INN-Approved', 'OON_Approved':'OON-Approved',
                            'Office_Key':'Office Key','Client_Name':'Client Name','Market_Closed':'Market Closed',} ,axis='columns')
    
    
    # return the whole html children table

    return html.Div([

        dash_table.DataTable(
        sort_action='native',
        columns=[{"name": i, "id": i} for i in monthly_progress_df.columns],
        data=monthly_progress_df.to_dict("records"),
        fixed_rows={'headers': True},
        style_table={"height": "35vh", "maxHeight": "35vh",'overflowY': 'auto'},
        style_cell={'height': 'auto','minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal','text-align':'center'}
    )

        ]
    )




############################ Follow-up Due volume ##########################

@app.callback(
        dash.dependencies.Output('follow_up_volumne_table','children'),
        [dash.dependencies.Input('sbu', 'value')],
        [dash.dependencies.Input('client_name', 'value')],
        [dash.dependencies.Input('office_key', 'value')],
        
        )

def update_follow_up_volume_table(sbu,client_name,office_key):

    select_all_string = str('SELECT * FROM [Credentialing_Dashboard].[dbo].[Credentialling_Follow_Up_Due_Volume]')
    sbu_string = str()
    client_name_string = str()
    office_key_string = str()


    # if user clear one of the filter, the dash will no update 
    if (len(sbu) < 1 ) or (len(client_name) < 1) or (len(office_key) <1):
        return dash.no_update
    
    filter_model = Filter_query()

    sbu_string = filter_model.filter_sub_string(sbu,'SBU')

    client_name_string = filter_model.filter_sub_string(client_name,'Client_name')

    office_key_string = filter_model.filter_sub_string(office_key,'Office_key')

    query=f"""
                {select_all_string}
                {sbu_string} {client_name_string} {office_key_string} 
            ;
            """ 
    
    follow_up_volume_df= cache_query_df(query)
        
    follow_up_volume_df = follow_up_volume_df.rename({'Office_Key':'Office Key','Client_Name':'Client Name',
                                                        'Over_7_Plus_Days_Due':'Over 7+ Days','One_To_Seven_Days_Due':'1-7 Days','Today_Due':'Today','Tomorrow_Due':'Tomorrow'} ,axis='columns') 
    # return the whole html children table
    return html.Div([

        dash_table.DataTable(
        sort_action='native',
        columns=[{"name": i, "id": i} for i in follow_up_volume_df.columns],
        data=follow_up_volume_df.to_dict("records"),
        fixed_rows={'headers': True},
        style_table={"height": "35vh", "maxHeight": "35vh",'overflowY': 'auto'},
        style_cell={'height': 'auto','minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal','text-align':'center'}
    )

        ]
    )


################## daily follow up #######################

@app.callback(
        dash.dependencies.Output('daily_follow_up_table','children'),
        [dash.dependencies.Input('sbu', 'value')],
        [dash.dependencies.Input('client_name', 'value')],
        [dash.dependencies.Input('office_key', 'value')],
        [dash.dependencies.Input('date_range', 'value')],
        [dash.dependencies.Input('date_range_picker', 'start_date')],  
        [dash.dependencies.Input('date_range_picker', 'end_date')],
        
        )

def update_daily_follow_up_table(sbu,client_name,office_key,date_range,start_date,end_date):

    select_all_string = str('SELECT * FROM [Credentialing_Dashboard].[dbo].[Credentialling_Daily_Follow_Ups]')
    sbu_string = str()
    client_name_string = str()
    office_key_string = str()


    # if user clear one of the filter, the dash will no update 
    if (len(sbu) < 1 ) or (len(client_name) < 1) or (len(office_key) <1):
        return dash.no_update
    
    filter_model = Filter_query()

    sbu_string = filter_model.filter_sub_string(sbu,'SBU')

    client_name_string = filter_model.filter_sub_string(client_name,'Client_name')

    office_key_string = filter_model.filter_sub_string(office_key,'Office_key')

    query=f"""
                {select_all_string}
                {sbu_string} {client_name_string} {office_key_string} 
            ;
            """ 

        
    daily_follow_up_df= cache_query_df(query)
    date_range_model = Date_range(daily_follow_up_df,date_range)

    if (start_date is not None) and (end_date is not None):
        daily_follow_up_df = date_range_model.date_range_picker(start_date,end_date)
        start_date_string = "From: " + date.fromisoformat(start_date).strftime('%m/%d/%Y')
        end_date_string = "To: " + date.fromisoformat(end_date).strftime('%m/%d/%Y')

    else:
        if date_range is not None:
            daily_follow_up_df = date_range_model.date_range_df()
            start_date_string = date_range_model.start_date_output()
            end_date_string = date_range_model.end_date_output()

        else:
            dash.no_update



    daily_follow_up_df = convert_row_to_column(daily_follow_up_df,["SBU", "Office_Key","Client_Name","Follow_Up_Date"])
    daily_follow_up_df = daily_follow_up_df.rename({'Office_Key':'Office Key','Client_Name':'Client Name'},axis='columns') 

    # return the whole html children table
    return html.Div([
        html.H4(children="Daily Follow-ups by SBU and Client ",style={'display':'inline-block'}),
        html.H5(children=start_date_string ,style={'display':'inline-block','margin': '40px'}),
        html.H5(children=end_date_string,style={'display':'inline-block','margin': '20px'}),
        dash_table.DataTable(
        sort_action='native',
        columns=[{"name": i, "id": i} for i in daily_follow_up_df.columns],
        data=daily_follow_up_df.to_dict("records"),
        fixed_rows={'headers': True},
        style_table={"height": "35vh", "maxHeight": "35vh",'overflowY': 'auto'},
        style_cell={'height': 'auto','minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal','text-align':'center'}
    )

        ]
    )


##################### Agent Level #######################



################ agent daily follow up count

@app.callback(
        dash.dependencies.Output('agent_daily_follow_up_table','children'),
        [dash.dependencies.Input('sbu_head', 'value')],
        [dash.dependencies.Input('agent_name', 'value')],  
        [dash.dependencies.Input('date_range', 'value')],
        [dash.dependencies.Input('date_range_picker', 'start_date')],  
        [dash.dependencies.Input('date_range_picker', 'end_date')],
        )

def update_agent_daily_follow_up_table(sbu_head,agent_name,date_range,start_date,end_date):

    select_all_string = str('SELECT * FROM [Credentialing_Dashboard].[dbo].[Credentialling_Agent_Level_Daily_Follow_Ups_Count]')
    sbu_string = str()
    agent_name_string = str()



    # if user clear one of the filter, the dash will no update 
    if (len(sbu_head) < 1 ) or (len(agent_name) < 1) :
        return dash.no_update
    
    filter_model = Filter_query()

    sbu_string = filter_model.filter_sub_string(sbu_head,'SBU_head')

    agent_name_string = filter_model.filter_sub_string(agent_name,'Record_Owner')

    query=f"""
                {select_all_string}
                {sbu_string} {agent_name_string} 
            ;
            """ 

            
    agent_daily_follow_up_df= cache_query_df(query)
    
    date_range_model = Date_range(agent_daily_follow_up_df,date_range)


    if (start_date is not None) and (end_date is not None):
        agent_daily_follow_up_df = date_range_model.date_range_picker(start_date,end_date)
       
       # transform the date format into mm/dd/yyyy
        start_date_string = "From:" + date.fromisoformat(start_date).strftime('%m/%d/%Y')
        end_date_string = " To:" + date.fromisoformat(end_date).strftime('%m/%d/%Y')

    else:
        if date_range is not None:
            agent_daily_follow_up_df = date_range_model.date_range_df()
            start_date_string = date_range_model.start_date_output()
            end_date_string = date_range_model.end_date_output()

        else:
            dash.no_update

    agent_daily_follow_up_df = convert_row_to_column(agent_daily_follow_up_df,["SBU_Head", "Record_Owner","Follow_Up_Date"])

    agent_daily_follow_up_df = agent_daily_follow_up_df.rename({'Record_Owner': 'Agent' ,'SBU_Head':'SBU'},axis='columns')
        
    # return the whole html children table
    return  html.Div([
            html.H4(children='Daily Follow-up Count ' ,style={'display':'inline-block'}),
            html.H5(children=start_date_string ,style={'display':'inline-block','margin': '50px'}),
            html.H5(children=end_date_string,style={'display':'inline-block','margin': '30px'}),
            dash_table.DataTable(
            sort_action='native',
            columns=[{"name": i, "id": i} for i in agent_daily_follow_up_df.columns],
            data=agent_daily_follow_up_df.to_dict("records"),
            fixed_rows={'headers': True},
            style_table={"height": "35vh", "maxHeight": "35vh",'overflowY': 'auto'},
            style_cell={'height': 'auto','minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
            'whiteSpace': 'normal','text-align':'center'}
        ),

            ]
        
        )
    


####################### agent level daily approval count

# @app.callback(
#         dash.dependencies.Output('agent_daily_approval_count_table','children'),
#         [dash.dependencies.Input('sbu_head', 'value')],
#         [dash.dependencies.Input('agent_name', 'value')],  
#         )

# def update_agent_approval_count_table(sbu_head,agent_name):

#         if (sbu_head is not None) and (agent_name is not None):
#             # initial string 
#             sbu_string = str()
#             agent_name_string = str()

#             and_string = str(' and ')
#             # set the global variable to count number of filter 
#             count = 0
            

#             if (len(sbu_head) < 1 ) or (len(agent_name) < 1):
#                 return dash.no_update
            
#             # If all filters is select-all, return empyty string. 
#             if (sbu_head[-1] == 'Select-All') and (agent_name[-1] == 'Select-All'):
#                 filter_string = str()
#             # if at least one filter have been used, it will start to use where 
#             else:
#                 filter_string = str('where ')
                    
#             # if the dropdown is not select-all, return cpt select query  
#             if sbu_head[-1] != 'Select-All':
#                 count+=1
#                 # if this query is not the first one, need to add the 'and' before the string
#                 if count > 1:
                
#                     sbu_string = and_string + str('SBU_Head in (') + str(sbu_head)[1:-1] +str(')')
#                 # if the query is the first one, not need to add 'and'
#                 else:
#                     sbu_string = str('SBU_Head in (') + str(sbu_head)[1:-1] +str(')')

#             if agent_name[-1] != 'Select-All':
#                 count+=1
#                 if count > 1:
#                     agent_name_string = and_string + agent_name_string + str('Record_Owner in (') + str(agent_name)[1:-1] +str(')')
#                 else:
#                     agent_name_string = str('Record_Owner in (') + str(agent_name)[1:-1] +str(')')
            


#             # query based on user input
#             query=f"""
#                     SELECT *
#                     FROM [Credentialing_Dashboard].[dbo].[Credentialling_Agent_Level_Daily_Follow_Ups_Approval_Count]
#                         {filter_string} {sbu_string} {agent_name_string}
#                     ;
#                     """ 
            
#             agent_daily_approval_count_df= cache_query_df(query)
              
#             # return the whole html children table
#             return html.Div([

#                 dash_table.DataTable(
#                 sort_action='native',
#                 columns=[{"name": i, "id": i} for i in agent_daily_approval_count_df.columns],
#                 data=agent_daily_approval_count_df.to_dict("records"),
#                 fixed_rows={'headers':'True','data':0},
#                 style_table={"height": "35vh", "maxHeight": "35vh",'overflowY': 'auto'},
#                 style_cell={'height': 'auto','minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
#                 'whiteSpace': 'normal','text-align':'center'}
#             )
        
#                 ]
#             )

#         else:
#             return dash.no_update



############################### dropdown callback ################################



########## summary and follow up dropdwon 

# when user select select-all, clear all the options
# office key dropdown
@app.callback(

dash.dependencies.Output(component_id='office_key', component_property='value'),
[dash.dependencies.Input(component_id='office_key', component_property='value')])

def update_office_key(office_key):
    
    if (office_key is None) or (len(office_key) < 1):
        return dash.no_update
    else:
        if office_key[-1] == 'Select-All':
            return ['Select-All']
        else:
            if 'Select-All' in office_key:
                office_key.remove('Select-All')

        return office_key



# sbu dropdown
@app.callback(

dash.dependencies.Output(component_id='sbu', component_property='value'),
[dash.dependencies.Input(component_id='sbu', component_property='value')])

def update_sbu(sbu):
    
    if (sbu is None) or (len(sbu) < 1):
        return dash.no_update
    else:

        if sbu[-1] == 'Select-All':
            return ['Select-All']
        else:
            if 'Select-All' in sbu:
                sbu.remove('Select-All')

        return sbu

# client name dropdown
@app.callback(

dash.dependencies.Output(component_id='client_name', component_property='value'),
[dash.dependencies.Input(component_id='client_name', component_property='value')])

def update_client_name(client_name):
    
    if (client_name is None) or (len(client_name) < 1):
        return dash.no_update
    else:
        if client_name[-1] == 'Select-All':
            return ['Select-All']
        else:
            if 'Select-All' in client_name:
                client_name.remove('Select-All')

        return client_name

######################  agent level dropdown 

# agent level sbu head dropdown
@app.callback(

dash.dependencies.Output(component_id='sbu_head', component_property='value'),
[dash.dependencies.Input(component_id='sbu_head', component_property='value')])

def update_agent_sbu(sbu_head):
    
    if (sbu_head is None) or (len(sbu_head) < 1):
        return dash.no_update
    else:
        if sbu_head[-1] == 'Select-All':
            return ['Select-All']
        else:
            if 'Select-All' in sbu_head:
                sbu_head.remove('Select-All')

        return sbu_head


# agent name dropdown
@app.callback(

dash.dependencies.Output(component_id='agent_name', component_property='value'),
[dash.dependencies.Input(component_id='agent_name', component_property='value')])

def update_agent_name(agent_name):
    
    if (agent_name is None) or (len(agent_name) < 1):
        return dash.no_update
    else:
        if agent_name[-1] == 'Select-All':
            return ['Select-All']
        else:
            if 'Select-All' in agent_name:
                agent_name.remove('Select-All')

        return agent_name

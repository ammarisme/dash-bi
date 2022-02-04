from dash_app.base.model import Model



# create the credentialing model
credentialing = Model()


status_breakdown_query='''
SELECT [SBU]
      ,[Office_Key]
      ,[Client_Name]
      ,[Last_Six_Month_Billed]
      ,[INN_Approved]
      ,[INN_Rejected]
      ,[OON_Approved]
      ,[OON_Rejected]
      ,[In-Process]
      ,[Pending]
      ,[On-Hold]
      ,[Market_Closed]
      ,[Other]
  FROM [Credentialing_Dashboard].[dbo].[Credentialling_Status_Breakdown_Numbers]
'''

# get the dataframe from sql server, use for dropdown options  
status_breakdown_df = credentialing.query_connect(status_breakdown_query)



agent_level_daily_query = '''
SELECT TOP (1000) [SBU_Head]
      ,[Record_Owner]
      ,[Follow_Up_Date]
      ,[Follow_Up_Count]
  FROM [Credentialing_Dashboard].[dbo].[Credentialling_Agent_Level_Daily_Follow_Ups_Count]

'''

# get the agent level dataframe from sql server , use fir dropdown options
agent_level_daily_df = credentialing.query_connect(agent_level_daily_query)
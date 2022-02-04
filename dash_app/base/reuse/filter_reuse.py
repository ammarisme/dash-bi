from flask_caching import Cache
from dash_app.app import app
from dash_app.base.model import Model
import pandas as pd
from datetime import date,timedelta
from dateutil.relativedelta import relativedelta

def convert_row_to_column(df,index_subset):
    #df['Follow_Up_Date'] = pd.to_datetime(df['Follow_Up_Date'], format='%y-%m-%d').dt.strftime('%d-%m-%y')
    df['Follow_Up_Date'] = df['Follow_Up_Date'].astype(str)
    #df['Follow_Up_Date']=pd.to_datetime(df['Follow_Up_Date'].astype(str), format='%d-%m-%Y')
    two_level_index_series = df.set_index(index_subset)["Follow_Up_Count"].unstack()
    df = two_level_index_series.rename_axis(columns=None)
    df = df.reset_index()

    return df

class Date_range():

    def __init__(self,df,date_range):
        self.df = df
        self.date_range = date_range
        self.start_date = None
        self.start_date_string = None
        self.end_date = None
        self.end_date_string = None
    
    def convert_date_range(self):
        
        
        # day
        if self.date_range == 'Today':
            self.start_date = date.today()
            self.end_date = date.today()
        
        elif self.date_range == 'Yesterday':
            self.start_date = date.today() + relativedelta(days=-1)
            self.end_date = date.today()+ relativedelta(days=-1)

                
        # week
        elif self.date_range == 'Week_to_date':
            self.start_date = date.today() - timedelta(days=date.today().weekday())
            self.end_date = date.today()

        elif self.date_range == 'This_week':
            self.start_date = date.today() - timedelta(days=date.today().weekday())
            self.end_date = self.start_date + timedelta(days=6)

        elif self.date_range == 'Previous_week':

            self.start_date = date.today() - timedelta(days=date.today().weekday()) + relativedelta(weeks=-1)
            self.end_date = self.start_date + timedelta(days=6)
        
        elif self.date_range == 'Last_two_week':
            self.start_date = date.today() - timedelta(days=date.today().weekday()) + relativedelta(weeks=-2)
            self.end_date = date.today()
        
        elif self.date_range == 'Last_three_week':
            self.start_date = date.today() - timedelta(days=date.today().weekday()) + relativedelta(weeks=-3)
            self.end_date = date.today()

        # Month

        elif self.date_range == 'Month_to_date':
            self.start_date = date.today().replace(day=1)
            self.end_date = date.today()
        
        elif self.date_range == 'This_month':
            self.start_date = date.today().replace(day=1)
            # first day of next month - 1 day
            self.end_date = date.today().replace(day=1) + relativedelta(months=+1) + relativedelta(days=-1)
        
        elif self.date_range == 'Previous_month':
            # first day of this month - one month
            self.start_date = date.today().replace(day=1) + relativedelta(months=-1)
            # first day of this month - one day
            self.end_date = date.today().replace(day=1) + relativedelta(days=-1)
        
        elif self.date_range == 'Last_two_month':
            # first day of this month - one month
            self.start_date = date.today().replace(day=1) + relativedelta(months=-1)
            # first day of next month - 1 day
            self.end_date = date.today().replace(day=1) + relativedelta(months=+1) + relativedelta(days=-1)
        
        elif self.date_range == 'Last_three_month':
            # first day of this month - one month
            self.start_date = date.today().replace(day=1) + relativedelta(months=-2)
            # first day of next month - 1 day
            self.end_date = date.today().replace(day=1) + relativedelta(months=+1) + relativedelta(days=-1)
        

        
        self.start_date = pd.to_datetime(self.start_date)
        self.end_date = pd.to_datetime(self.end_date)
        return self.start_date, self.end_date

    def date_range_filter(self):

        # change the date time format to pandas datetime fromat
        self.df['Follow_Up_Date'] = pd.to_datetime(self.df['Follow_Up_Date'])

        # select the correct date range from user input
        self.df = self.df[(self.df['Follow_Up_Date'] >= self.start_date)]
        self.df = self.df[(self.df['Follow_Up_Date'] <= self.end_date)]

        # return the filtered dataframe
        return self.df
    
    def date_range_picker(self,start_date,end_date):
        
        # date range picker is come from calendar 
        # init the date range from user input
        self.start_date = start_date
        self.end_date = end_date
        
        # filter the right date range 
        self.date_range_filter()
        return self.df
    
    def date_range_df(self):
        
        # date range come from date range dropdown
        # convert the dropdown date range into start date and end date 
        self.convert_date_range()
        
        # filter the right date range
        self.date_range_filter()
        return self.df
    
    def start_date_output(self):
        
        # output the start date string
        self.convert_date_range() 
        self.start_date_string = str(" From: ") + str(self.start_date.strftime('%m/%d/%Y'))
        return self.start_date_string
    
    def end_date_output(self):

        # output the end date string
        self.convert_date_range()
        self.end_date_string = str(" To: ") + str(self.end_date.strftime('%m/%d/%Y'))
        return self.end_date_string



class Filter_query():

    def __init__(self):
        # count is to check if the query is the first one or not, 0 mean is the first one, and it don't need to add 'and' string
        self.count = 0
        # and string is the used to connect two sub query 
        self.and_string = str(' and ')
        # where string is used to filter the sepecific query
        self.where_string = str(' where ')
        self.filter_string = str()


    def filter_sub_string(self,filter_input,sub_query):
        # init the output string
        output_string = str()


        if ('Select-All' not in filter_input):
            
            self.count+=1
            
            # if this query is not the first one, need to add the 'and' before the string
            if self.count > 1:
                output_string = self.and_string + str(sub_query+' in (') + str(filter_input)[1:-1] +str(')')
            # if the query is the first one, not need to add 'and'
            else:
                output_string = self.where_string + str(sub_query+' in (') + str(filter_input)[1:-1] +str(')')
        return output_string


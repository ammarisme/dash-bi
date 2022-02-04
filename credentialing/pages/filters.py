from credentialing.models import status_breakdown_df,agent_level_daily_df


class dropdown:
    

    
    """ This function is use to create the dropdown options list contain select-all option
        and other options from sepecific column
        
        Args:
        data: pandas dataframe
        input_column: String, The column name from the dataframe 

        Output:
        output_list : List, The list contain dropdown options for that column

    """

    def dropdown_data_list(data,input_column):
        output_list = []
        
        output_list.append({'label':'Select-All','value':'Select-All'})


        for i in data[input_column].unique():
            
            if i is None:
                output_list.append({'label':'NaN','value':'NaN'})
            else:
                output_list.append({'label':i,'value':i})
        
        return output_list

# client name dropdown options list
client_name_list = dropdown.dropdown_data_list(status_breakdown_df,'Client_Name')

# officekey dropdown options list
office_key_list = dropdown.dropdown_data_list(status_breakdown_df,'Office_Key')

# sbu dropdown options list
sbu_list = dropdown.dropdown_data_list(status_breakdown_df,'SBU')

# agent dropdown options list
agent_list = dropdown.dropdown_data_list(agent_level_daily_df,'Record_Owner')


# agent level sbu options list 
agent_sbu_head_list = dropdown.dropdown_data_list(agent_level_daily_df,'SBU_Head')



filter_date_list = []
# day
filter_date_list.append({'label':'Today','value':'Today'})
filter_date_list.append({'label':'Yesterday','value':'Yesterday'})


# week
filter_date_list.append({'label':'Week To Date','value':'Week_to_date'})
filter_date_list.append({'label':'This Week','value':'This_week'})
filter_date_list.append({'label':'Previous Week','value':'Previous_week'})
filter_date_list.append({'label':'Last Two Week','value':'Last_two_week'})
filter_date_list.append({'label':'Last Three Week','value':'Last_three_week'})

# month
filter_date_list.append({'label':'Month To Date','value':'Month_to_date'})
filter_date_list.append({'label':'This Month','value':'This_month'})
filter_date_list.append({'label':'Previous Month','value':'Previous_month'})
filter_date_list.append({'label':'Last Two Month','value':'Last_two_month'})
filter_date_list.append({'label':'Last Three Month','value':'Last_three_month'})


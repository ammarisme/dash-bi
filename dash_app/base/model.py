import logging
import pandas as pd
from pandas.core.frame import DataFrame
import pyodbc
import pymssql

from environs import Env

# read the password from .env file
env = Env()
env.read_env()


from dash_app.base.db import MssqlInstance, RedisConnection
from dash_app.config import (
    DATABASES, 
    REDIS_DS
)
from dash_app.app import cache, CONF_PARAMETER


# logger setup
logger = logging.getLogger('core')

# Connection to redis server
REDIS_SERVER = RedisConnection(REDIS_DS[CONF_PARAMETER]).connect()

# creating SQL server db instance
MSSQL = MssqlInstance(DATABASES['SQL_server']['HOST'],
                      DATABASES['SQL_server']['DATABASE'],
                      DATABASES['SQL_server']['USER'],
                      DATABASES['SQL_server']['PASSWORD'])

# Caching into redis decorator



class Model():
    """
    Model class that is responsible to handle data tables
    """
    def __init__(self):
        self.db = MSSQL
        self.r = REDIS_SERVER
        self.df = None
        self.conn = None
        self.cursor = None

    def change_database(self, db):
        self.db.database = db

    def db_connect(self):
        self.conn = self.db.connect()
        return self.conn

    def get_cursor(self):
        self.cursor = self.db.connect().cursor()
        return self.cursor

    def query_connect(self,query):

         
        # self.df = pd.read_sql(query,self.db_connect())
        # self.close_connection()

        # self.db_connect()
        # self.get_cursor()

        # self.cursor.excute(query)

        # self.df = pd.DataFrame(self.cursor.fetchall())
        # self.close_connection()
        
        
        # return self.df

        connect = pymssql.connect(
                host='52.201.153.152',  
                user='hrcadmin',       
                password=env("MSSQL_PASSWORD"),   
                charset='utf8',  
                database='Credentialing_Dashboard')     
        
        self.df = pd.read_sql(query,con=connect)

        return self.df

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
    

    def dict_to_dataframe(self, dictionary):
        self.df = pd.DataFrame(dictionary)
        return self.df

    def csv_to_dataframe(self, csv):
        self.df = pd.read_csv(csv)
        return self.df

    @staticmethod
    def redis_caching(func):
        """
        If the output of the query is pandas DataFrame then
        json format of the output will be sent to redis cache
        """
        t = REDIS_DS[CONF_PARAMETER]['TIMEOUT']
        @cache.memoize(timeout=t)
        def query(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, pd.core.frame.DataFrame):
                raise TypeError('Return value should be DataFrame')
            else:
                print('converting to json...')
                return result.to_json(date_format='iso', orient='split')
        return query

    def cache_and_read_csv_as_df(self, csv):
        print('caching and getting df...')
        return pd.read_json(
            self.redis_caching(self.csv_to_dataframe)(csv),
            orient='split'
        )

    def cache_dict_and_return_df(self, dictionary):
        print('caching and getting df...')
        return pd.read_json(
            self.redis_caching(self.dict_to_dataframe)(dictionary),
            orient='split'
        )




    

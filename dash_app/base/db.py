import redis
import pyodbc
from abc import ABC, abstractmethod
from dash_app import config


class DbInstance(ABC):
    """
    interface to create db instancs and
    defining set of functions
    """
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_connection_string(self):
        pass

    @abstractmethod
    def execute_many(self):
        pass


class MssqlInstance(DbInstance):
    """
    MSSQL db instance which is based on the above abstract class
    provides db adaptor functionality
    """
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        """
        returns the conn
        """
        

        # parameter dictionary
        param_dic = {
            'driver': config.DATABASES['SQL_server']['OPTIONS']['driver'],
            'server': self.host,
            'database': self.database,
            'uid': self.user,
            'pwd': self.password
        }

        conn = None
        try:
            conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.host+';DATABASE='+self.database+';UID='+self.user+';PWD='+ self.password)
            #conn = pyodbc.connect(*param_dic)
            return conn
        except Exception as error:
            print(error)

    def get_connection_string(self):
        return f"host is: {self.host}, user is {self.user}, and database is {self.database}"

    def execute_many(self, cursor, query, chunk, fast_execute=True):
        """
        Try to use fast execute many for sql server if flag in Dbparams is set
        cursor: database cursor
        query: sql query
        chunk: list, rows of parameters
        """
        try:
            cursor.fast_executemany = fast_execute
            cursor.executemany(query, chunk)
            cursor.commit()
        except MemoryError:
            cursor.fast_executemany = False
            cursor.executemany(query, chunk)
            cursor.commit()

    def __str__(self):
        return self.get_connection_string()

    def __repr(self):
        return self.get_connection_string()


class RedisConnection:
    """
    An interface for redis client
    """
    def __init__(self, redis_dic: dict):
        self.CACHE_TYPE = 'redis'
        self.CACHE_REDIS_HOST = redis_dic['HOST']
        self.CACHE_REDIS_PORT = redis_dic['PORT']
        self.CACHE_REDIS_DB = redis_dic['DB']
        self.CACHE_REDIS_URL = redis_dic['URL']
        self.CACHE_DEFAULT_TIMEOUT = redis_dic['TIMEOUT']

    def connect(self):
        """Connecting redis memory data structure"""
        r = redis.Redis(
            host=self.CACHE_REDIS_HOST,
            port=self.CACHE_REDIS_PORT,
            db=self.CACHE_REDIS_DB)
        return r

    def get_config(self):
        """Getting config dictionary"""
        return {
            'CACHE_TYPE': self.CACHE_TYPE,
            'CACHE_REDIS_HOST': self.CACHE_REDIS_HOST,
            'CACHE_REDIS_PORT': self.CACHE_REDIS_PORT,
            'CACHE_REDIS_DB': self.CACHE_REDIS_DB,
            'CACHE_REDIS_URL': self.CACHE_REDIS_URL,
            'CACHE_DEFAULT_TIMEOUT': self.CACHE_DEFAULT_TIMEOUT,
        }
import os
from dotenv import load_dotenv


# Production
DEV = True


# loading env varaiables
load_dotenv()

# Base path of the project, which will get executed in the index file
BASE_PATH = os.getcwd()

# Database connection parameters
DATABASES = {
    'SQL_server': {
        'HOST': "52.201.153.152",
        'DATABASE': 'Credentialing_Dashboard',
        'USER': "hrcadmin",
        'PASSWORD': os.getenv('MSSQL_PASSWORD'),
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        }
    }
}

# Redis connection parameters
REDIS_DS = {
    'Dev': {
        'HOST': 'myapp-redis',
        'DB': 0,
        'PORT': 6379,
        'URL': 'redis://myapp-redis:6379',
        'TIMEOUT': 500
    },
}

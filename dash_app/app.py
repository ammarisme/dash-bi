import dash
import dash_bootstrap_components as dbc
from flask_caching import Cache

from dash_app.base.db import RedisConnection
from dash_app.config import (
    REDIS_DS,
    DEV
)

# app deployment status config
CONF_PARAMETER = 'Dev' if DEV else 'Prod'


# dash app configuration
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

server = app.server
app.config.suppress_callback_exceptions = True

# Redis cache config
redis_config = RedisConnection(REDIS_DS[CONF_PARAMETER]).get_config()
cache = Cache(server, config=redis_config)

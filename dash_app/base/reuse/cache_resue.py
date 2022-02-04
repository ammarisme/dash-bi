from flask_caching import Cache
from dash_app.base.model import Model
from dash_app.app import app
################### caching ################################

# cache to local filesystem
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

TIMEOUT = 600

# cache the filtered dataframe from sql server and save it into local filesystem
@cache.memoize(timeout=TIMEOUT)
def cache_query_df(query):

    df_model = Model()
    df = df_model.query_connect(query)

    return df


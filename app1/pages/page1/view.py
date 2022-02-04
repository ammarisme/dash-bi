from dash import html, dcc
from dash.dependencies import Output, Input
import plotly.express as px
from dash_app.app import app
from app1.models import gap_minder_df as df

# html layout
page1_layout = html.Div([
    html.H1('Test'),
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(id='year-slider',
               min=df['year'].min(),
               max=df['year'].max(),
               value=df['year'].min(),
               marks={str(year): str(year)
                      for year in df['year'].unique()},
               step=None)
])


# callbacks
@app.callback(Output('graph-with-slider', 'figure'),
              Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df,
                     x="gdpPercap",
                     y="lifeExp",
                     size="pop",
                     color="continent",
                     hover_name="country",
                     log_x=True,
                     size_max=55)

    fig.update_layout(transition_duration=500)

    return fig

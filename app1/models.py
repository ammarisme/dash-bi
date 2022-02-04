from dash_app.base.model import Model

gap_minder = Model()
gap_minder_df = gap_minder.csv_to_dataframe(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
)

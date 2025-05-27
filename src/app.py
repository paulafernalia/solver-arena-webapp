import dash_bootstrap_components as dbc
from dash import Dash

from callbacks import register_callbacks
from layout import layout

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = layout

register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)

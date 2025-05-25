import time

import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, callback

from layout import layout

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])


app.layout = layout


@callback(
    Output("output-div", "style"),
    Input("run-button", "n_clicks"),
    State("output-div", "style"),
    prevent_initial_call=True,
)
def show_div(n_clicks, current_style):
    if n_clicks:
        new_style = current_style.copy()
        new_style["display"] = "block"
        new_style["opacity"] = "1"
        new_style["transform"] = "translateX(0)"
        return new_style
    return current_style


@callback(
    Output("loading-output", "children"),
    Input("run-button", "n_clicks"),
    prevent_initial_call=True,
)
def input_triggers_nested(n_clicks):
    if n_clicks:
        time.sleep(5)
        return "Results"


if __name__ == "__main__":
    app.run(debug=True)

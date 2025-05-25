import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, callback

from layout import layout

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])


app.layout = layout


@callback(
    Output("output-div", "style"),
    Input("show-button", "n_clicks"),
    State("output-div", "style"),
    prevent_initial_call=True,
)
def show_div(n_clicks, current_style):
    print("clicked")
    if n_clicks:
        new_style = current_style.copy()
        new_style["display"] = "block"
        new_style["opacity"] = "1"
        new_style["transform"] = "translateX(0)"
        return new_style
    return current_style


if __name__ == "__main__":
    app.run(debug=True)

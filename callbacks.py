from dash import Input, Output, State, callback


def register_callbacks(app):
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

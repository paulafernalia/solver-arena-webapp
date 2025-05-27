from dash import ALL, Input, Output, State, callback, ctx


def register_callbacks(app):
    @callback(
        Output("output-div", "style"),
        Input("run-button", "n_clicks"),
        State("output-div", "style"),
        prevent_initial_call=True,
    )
    def show_div(n_clicks, current_style):
        """
        Show right panel when clicking on the run button
        """
        if n_clicks:
            new_style = current_style.copy()
            new_style["display"] = "block"
            new_style["opacity"] = "1"
            new_style["transform"] = "translateX(0)"
            return new_style
        return current_style

    @callback(
        Output({"type": "solver-toggle-results", "index": ALL}, "className"),
        Input({"type": "solver-toggle-results", "index": ALL}, "n_clicks"),
        prevent_initial_call=True,
    )
    def highlight_selected(n_clicks_list):
        triggered = ctx.triggered_id  # get the ID of the triggered button

        if triggered is None:
            return ["custom-button"] * len(n_clicks_list)

        selected_index = triggered["index"]
        return [
            "custom-button selected"
            if i["id"]["index"] == selected_index
            else "custom-button"
            for i in ctx.inputs_list[0]
        ]

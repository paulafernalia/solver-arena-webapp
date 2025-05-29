from dash import ALL, Input, Output, State, callback, ctx, no_update

from components import plots
from utils import solvers


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

    @app.callback(
        Output("selected-solvers-store", "data"),
        Input({"type": "solver-toggle-results", "index": ALL}, "n_clicks"),
        State({"type": "solver-toggle-results", "index": ALL}, "value"),
        State("selected-solvers-store", "data"),
    )
    def update_selected_buttons(n_clicks_list, values, selected_buttons):
        if not ctx.triggered_id:
            return no_update

        clicked_value = ctx.triggered_id["index"]

        if clicked_value in selected_buttons:
            selected_buttons.remove(clicked_value)
        else:
            selected_buttons.append(clicked_value)

        return selected_buttons

    @app.callback(
        Output({"type": "solver-toggle-results", "index": ALL}, "className"),
        Input("selected-solvers-store", "data"),
        State({"type": "solver-toggle-results", "index": ALL}, "value"),
    )
    def update_selected_solver_styles(selected_buttons, values):
        if not selected_buttons:
            return ["custom-button"] * len(values)
        return [
            "custom-button selected" if val in selected_buttons else "custom-button"
            for val in values
        ]

    @app.callback(
        Output("ub-line-chart-container", "children"),
        Input("selected-solvers-store", "data"),
    )
    def update_gap_chart(selected_solvers):
        if len(selected_solvers) == 0:
            return plots.gap_progress_line_chart(solvers.names)

        return plots.gap_progress_line_chart(selected_solvers)

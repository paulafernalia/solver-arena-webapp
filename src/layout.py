from dash import html

from components import buttons, plots, selectors, text
from utils import solvers

layout = html.Div(
    style={
        "display": "flex",
        "height": "100vh",  # full viewport height
        "width": "100vw",  # full viewport width
    },
    children=[
        # Left panel (INPUTS)
        html.Div(
            id="input-div",
            children=[
                #
                # TITLE + SUBTITLE:
                text.title("SolverArena"),
                text.subtitle("MIP Solver Benchmarking"),
                html.Div(style={"height": "50px"}),
                #
                # Step 1: UPLOAD
                text.step("1. Upload an instance in .mps or .lp format"),
                html.Div(style={"height": "10px"}),
                buttons.upload_button(label="Upload file"),
                html.Div(style={"height": "50px"}),
                #
                # Step 2: SELECT SOLVERS
                text.step("2. Select solvers"),
                selectors.checklist(
                    id_="solver-checklist", labels=solvers.names, values=solvers.names
                ),
                html.Div(style={"height": "50px"}),
                #
                # Step 3: CONFIGURE PARAMETERS
                #
                # Step 4: RUN SolverArena
                text.step("4. Benchmark selected solvers"),
                html.Div(style={"height": "20px"}),
                buttons.regular_button(id_="run-button", label="Run comparison"),
            ],
            className="left-panel",
        ),
        # Right panel (RESULTS)
        html.Div(
            children=[
                #
                # TITLE + Selected file:
                text.title("Benchmarking results", "grey"),
                text.subtitle("for myproblem.mps"),
                html.Div(style={"height": "50px"}),
                #
                # Basic KPI bar chart
                # plots.bar_chart(),
                #
                # Optimality gap progress
                html.Div(
                    style={
                        "display": "flex",
                        "flexDirection": "row",
                        "justifyContent": "space-between",
                        "alignItems": "flex-start",
                    },
                    children=[
                        # Chart on the left
                        html.Div(
                            id="ub-line-chart-container",
                            children=plots.gap_progress_line_chart("GUROBI"),
                            style={"flex": "1"},
                        ),
                        selectors.button_toggle(
                            id_="solver-toggle-results", labels=solvers.names
                        ),
                        # Hidden div for the selected solvers
                        dcc.Store(id="selected-solvers-store", data=[]),
                    ],
                ),
            ],
            id="output-div",
            className="right-panel",
            style={
                "display": "none",
                "opacity": "0",
                "transform": "translateX(-100%)",
                "transition": "all 0.5s ease",
            },
        ),
    ],
)

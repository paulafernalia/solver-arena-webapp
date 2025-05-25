import dash_bootstrap_components as dbc
from dash import dcc, html

from utils import colors, fonts


def input_column():
    return html.Div(
        id="input-div",
        children=[
            title("SolverArena"),
            subtitle("MIP Solver Benchmarking"),
            html.Div(style={"height": "50px"}),
            steps_text("1. Upload an instance in .mps or .lp format"),
            html.Div(style={"height": "10px"}),
            upload_button(),
            html.Div(style={"height": "50px"}),
            steps_text("2. Select solvers"),
            solver_select(),
            html.Div(style={"height": "50px"}),
            steps_text("4. Benchmark selected solvers"),
            html.Div(style={"height": "20px"}),
            run_button(),
        ],
        style={
            "backgroundColor": colors.LIGHT_BLACK,
            "width": "33%",
            "padding": "50px",
            "boxSizing": "border-box",
            "height": "100vh",
            "margin": "auto",
        },
    )


def title(text: str):
    return html.H3(
        text,
        style={
            "color": colors.MUSTARD_YELLOW,
            "fontFamily": fonts.MONO,
            "fontSize": "28px",
        },
    )


def subtitle(text: str):
    return html.H4(
        text,
        style={
            "color": "#BBBBBB",  # grey color
            "fontFamily": fonts.MONO,
            "marginTop": "4px",
            "fontWeight": "normal",
            "fontSize": "15px",
        },
    )


def steps_text(text: str):
    return html.P(
        text,
        style={
            "fontSize": fonts.SMALL_SIZE,
            "color": colors.TEXT_LIGHT,  # grey color
            "fontFamily": fonts.MONO,
        },
    )


def solver_select():
    return dcc.Checklist(
        id="item-checklist",
        options=[
            {"label": "Gurobi", "value": "gurobi"},
            {"label": "HiGHS", "value": "highs"},
            {"label": "SCIP", "value": "scip"},
            {"label": "CPLEX", "value": "cplex"},
            {"label": "CBC", "value": "cbc"},
        ],
        value=[],  # default selected
        className="custom-checkbox",
        labelStyle={
            "display": "block",
            "marginLeft": "25px",
            "fontSize": fonts.SMALL_SIZE,
            "color": colors.TEXT_LIGHT,
            "fontFamily": fonts.MONO,
        },
    )


def run_button():
    return dbc.Button(
        "Run comparison",
        id="show-button",
        n_clicks=0,
        className="custom-button",
        style={
            "display": "block",
            "margin": "0 auto",
        },
    )


def upload_button():
    return dcc.Upload(
        children=html.Button(
            "Upload file",
            className="custom-button",
            style={
                "padding": "8px 25px",
            },
        ),
        multiple=False,
        style={"textAlign": "center"},
    )

from dash import dcc, html

from components import base
from utils import colors


def output_column():
    return html.Div(
        children=[
            base.title("Benchmarking results", "grey"),
            base.subtitle("for myproblem.mps"),
            html.Div(style={"height": "50px"}),
            dcc.Loading(
                children=[html.Div(id="loading-output")],
                type="circle",
                className="custom-spinner",
                color=colors.MUSTARD_YELLOW,
            ),
        ],
        id="output-div",
        style={
            "display": "none",
            "opacity": "0",
            "transform": "translateX(-100%)",
            "transition": "all 0.5s ease",
            "backgroundColor": colors.DARK_BLACK,
            "width": "67%",
            "padding": "50px",
            "boxSizing": "border-box",
            "height": "100vh",
            "margin": "auto",
        },
    )

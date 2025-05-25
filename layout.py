from dash import html

from components.input_column import input_column
from utils import colors

layout = html.Div(
    style={
        "display": "flex",
        "height": "100vh",  # full viewport height
        "width": "100vw",  # full viewport width
    },
    children=[
        input_column(),
        html.Div(
            "Right column content",
            id="output-div",
            style={
                "display": "none",
                "opacity": "0",
                "transform": "translateX(-100%)",
                "transition": "all 0.5s ease",
                "backgroundColor": colors.DARK_BLACK,
                "width": "67%",
                "padding": "20px",
                "boxSizing": "border-box",
                "height": "100vh",
                "margin": "auto",
            },
        ),
    ],
)

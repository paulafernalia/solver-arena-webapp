from dash import html

from components.input_column import input_column
from components.output_column import output_column

layout = html.Div(
    style={
        "display": "flex",
        "height": "100vh",  # full viewport height
        "width": "100vw",  # full viewport width
    },
    children=[
        input_column(),
        output_column(),
    ],
)

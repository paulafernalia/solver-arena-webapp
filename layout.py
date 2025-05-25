from dash import html
from components.content_column import ContentColumn
from utils import colors

layout = html.Div(
    children=[
        ContentColumn(),
        # You can add Header(), Footer(), or other components here later
    ],
    style={
        "height": "100vh",
        "backgroundColor": colors.DARK_BLACK,
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "center",
        "margin": "0",
        "padding": "0",
    },
)
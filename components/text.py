from dash import html

from utils import colors, fonts


def title(text: str, color: str = colors.ACCENT):
    return html.H3(
        text,
        style={
            "color": color,
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


def step(text: str):
    return html.P(
        text,
        style={
            "fontSize": fonts.SMALL_SIZE,
            "color": colors.TEXT_LIGHT,  # grey color
            "fontFamily": fonts.MONO,
        },
    )

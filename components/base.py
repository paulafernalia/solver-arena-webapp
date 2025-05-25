from dash import html

from utils import colors, fonts


def title(text: str, color: str = colors.MUSTARD_YELLOW):
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

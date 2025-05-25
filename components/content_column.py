from dash import html, dcc
from utils import colors

def ContentColumn():
    return html.Div(
        children=[
            html.H3(
                "SolverArena",
                style={
                    "color": colors.MUSTARD_YELLOW,
                    "fontFamily": "Consolas, monospace"
                }
            ),
            html.H4(
                "MIP Solver Benchmarking",
                style={
                    "color": "#BBBBBB",  # grey color
                    "fontFamily": "Consolas, monospace",
                    "marginTop": "4px",
                    "fontWeight": "normal",
                    "fontSize": "16px",  # smaller size
                }
            ),

            dcc.Upload(
                id='upload-data',
                children=html.Button(
                    'Upload .mps',
                    style={
                        "fontFamily": "Consolas, monospace",
                        "fontSize": "14px",
                        "padding": "10px 30px",
                        "marginTop": "50px",  # more vertical space
                        "cursor": "pointer",
                        "borderRadius": "3px",  # rounded corners
                        "border": "1px solid #666",  # subtle border
                        "transition": "background-color 0.3s ease",
                    },
                    id="upload-button"
                ),
                multiple=False,
                style={"textAlign": "center", "width": "100%"},
                # To add hover effect, you'd use CSS in assets/styles.css
            )
        ],
        style={
            "backgroundColor": colors.LIGHT_BLACK,
            "width": "100%",
            "maxWidth": "600px",
            "margin": "auto",
            "height": "97vh",
            "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
            "justifyContent": "flex-start",
            "textAlign": "center",
            "padding": "40px 20px",
            "borderRadius": "8px",
        },
    )
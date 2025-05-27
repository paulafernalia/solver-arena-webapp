import dash_bootstrap_components as dbc
from dash import dcc, html


def regular_button(id_, label):
    return dbc.Button(
        "Run comparison",
        id="run-button",
        n_clicks=0,
        className="custom-button",
        style={
            "display": "block",
            "margin": "0 auto",
        },
    )


def upload_button(label):
    return dcc.Upload(
        children=html.Button(
            label,
            className="custom-button",
            style={
                "padding": "8px 25px",
            },
        ),
        multiple=False,
        style={"textAlign": "center"},
    )

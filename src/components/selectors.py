from dash import dcc, html

from utils import colors, fonts


def checklist(id_, labels, values):
    return dcc.Checklist(
        id=id_,
        options=[
            {"label": label, "value": value} for label, value in zip(labels, values)
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


def button_toggle(id_, labels):
    return html.Div(
        id=id_,
        children=[html.Div(style={"height": "30px"})]
        + [
            html.Div(
                id={"type": id_, "index": label},
                children=label,
                n_clicks=0,
                className="custom-button",
                style={
                    "margin-bottom": "10px",
                    # "padding": "8px 2px",
                    "width": "130px",
                    "textAlign": "center",
                },
            )
            for label in labels
        ],
        style={
            "display": "flex",
            "flexDirection": "column",
            "marginLeft": "30px",
            "marginTop": "10px",
            "minWidth": "150px",
        },
    )

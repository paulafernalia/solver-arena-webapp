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
        children=[
            html.Div(id=id_ + "-selected", style={"display": "none"}),
            html.Div(style={"height": "30px"}),
        ]
        + [
            html.Button(
                label,
                id={"type": id_, "index": label},
                n_clicks=0,
                className="custom-button",
                style={"margin-bottom": "10px", "padding": "6px", "width": "130px"},
                value=label,
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

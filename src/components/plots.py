import numpy as np
import plotly.graph_objects as go
from dash import dash_table, dcc
from dash.dash_table.Format import Format, Symbol

from utils import colors, data, fonts

solvers = ["Gurobi  ", "HiGHS  ", "SCIP  ", "CPLEX  ", "CBC  "]


def bar_chart():
    values = [10, 15, 7, 12, 10]

    fig = go.Figure(
        go.Bar(
            x=values,
            y=solvers,
            orientation="h",
            marker=dict(
                color=colors.ACCENT,
                line=dict(
                    color=colors.ACCENT,  # Solid mustard yellow border
                    width=2,
                ),
            ),
            width=0.5,
            text=values,  # labels to show inside bars
            textposition="inside",  # position inside the bars
            textfont=dict(color="white", weight="bold"),  # white font color
        )
    )

    # Remove gridlines and ticks on x-axis
    fig.update_xaxes(
        showgrid=False,
        showticklabels=False,
    )

    fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor=colors.DARK_BLACK,
        height=60 * len(solvers),
        font=dict(
            family=fonts.MONO,
            size=14,
            color=colors.TEXT_LIGHT,
        ),
        margin=dict(l=80, r=20, t=20, b=50),
    )

    return dcc.Graph(id="time-bar-chart", figure=fig)


def gap_progress_line_chart(solvers):
    x = list(range(100))  # e.g., time or iterations
    fig = go.Figure()

    for solver in solvers:
        y = data.generate_ub_data(steps=100)

        fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                mode="lines",
                name=solver,
                line=dict(color=colors.ACCENT, width=1),
                marker=dict(size=6),
                showlegend=False,
            )
        )
        fig.add_trace(
            go.Scatter(
                x=x,
                y=[-value + 1500 for value in y],
                mode="lines",
                name=solver,
                line=dict(color=colors.ACCENT, dash="dash", width=1),
                marker=dict(size=6),
                showlegend=False,
            )
        )

    fig.update_layout(
        xaxis=dict(
            title="Time(s)",
            showgrid=False,
            title_font=dict(size=14),
        ),
        yaxis=dict(
            title="Objective value",
            showgrid=False,
            title_font=dict(size=14),
        ),
        height=300,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white", family=fonts.MONO, size=14),
        margin=dict(l=80, r=20, t=20, b=50),
    )

    return dcc.Graph(figure=fig)


def generate_background_styles(
    df, hex_color=colors.ACCENT, border_color=colors.DARK_BLACK
):
    """
    Generate conditional styles for DataTable:
    - Background colors for numeric cells based on value intensity.
    - Borders for all data cells.
    """
    styles = []

    numeric_cols = df.select_dtypes(include=[np.number]).columns

    for col in numeric_cols:
        col_values = df[col]
        min_val = col_values.min()
        max_val = col_values.max()

        for i, val in enumerate(col_values):
            bg_color, opacity = colors.get_conditional_color(
                val, min_val, max_val, hex_color, True
            )
            font_color = colors.TEXT_DARK if opacity < 0.4 else colors.DARK_BLACK
            styles.append(
                {
                    "if": {"row_index": i, "column_id": col},
                    "backgroundColor": bg_color,
                    "color": font_color,
                }
            )

        # Add border to this column's data cells
        styles.append({"if": {"column_id": col}, "border": f"2px solid {border_color}"})

    return styles


def summary_datatable(summary_df):
    percentage = dash_table.FormatTemplate.percentage(2)

    columns = [
        dict(id="solvers", name="Solvers"),
        dict(id="ub", name="Best solution"),
        dict(id="lb", name="Best bound"),
        dict(id="nodes", name="Nodes"),
        dict(
            id="time",
            name="Time",
            type="numeric",
            format=Format().symbol(Symbol.yes).symbol_suffix("s"),
        ),
        dict(id="gap", name="Gap", type="numeric", format=percentage),
    ]

    return dash_table.DataTable(
        data=summary_df.to_dict("records"),
        columns=columns,
        style_header={
            "backgroundColor": colors.DARK_BLACK,
            "color": colors.TEXT_DARK,
            "fontSize": fonts.SMALL_SIZE,
            "border": "none",
        },
        style_data={
            "backgroundColor": colors.DARK_BLACK,
            "color": colors.TEXT_DARK,
            "fontSize": fonts.SMALL_SIZE,
            "border": "none",
        },
        style_data_conditional=generate_background_styles(summary_df),
        style_table={"backgroundColor": "transparent"},
        style_cell={
            "minWidth": "100px",
            "maxWidth": "120px",
            "width": "120px",
            "textAlign": "center",
            "whiteSpace": "normal",
        },
        style_cell_conditional=[
            {
                "if": {"column_id": summary_df.columns[0]},
                "textAlign": "left",
            },  # left align first column
        ],
    )

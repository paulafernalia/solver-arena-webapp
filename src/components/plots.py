import plotly.graph_objects as go
from dash import dcc

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
        height=350,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white", family=fonts.MONO, size=14),
        margin=dict(l=80, r=20, t=20, b=50),
    )

    return dcc.Graph(figure=fig)

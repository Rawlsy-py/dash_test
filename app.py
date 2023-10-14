from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

df = pd.DataFrame(
    {
        "Day": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        * 100,
        "Sales": [10, 13, 14, 15, 14, 13, 10] * 100,
        "Marketing Spend": [100, 130, 140, 150, 140, 130, 100] * 100,
        "Profit": [50, 60, 70, 80, 70, 60, 50] * 100,
    }
)

app = Dash(__name__)

fig = px.line(df, x="Day", y="Sales", title="Sales per day")

app.layout = html.Div(
    children=[
        html.H1(children="Marketing Dashboard"),
        html.Div(children="Review of XXX Company data"),
        dcc.Graph(id="sales", figure=fig),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)

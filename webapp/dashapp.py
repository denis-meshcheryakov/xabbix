import dash
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
import plotly
import plotly.graph_objs as go
import yaml


def init_dash_app(server):

    dash_app = dash.Dash(__name__, server=server,
                         url_base_pathname='/monitoring/')

    dash_app.layout = html.Div([dcc.Graph(id='live-graph'),
                                dcc.Interval(
                                id='graph-update',
                                interval=5*1000,
                                n_intervals=5), ])

    init_callbacks(dash_app)
    return dash_app.server


def init_callbacks(dash_app):
    app = dash_app

    @app.callback(
        Output('live-graph', 'figure'),
        [Input('graph-update', 'n_intervals')])
    def update_graph_scatter(n):

        with open('success_packet_perc.yaml') as f:
            p_dict = yaml.safe_load(f)

        x_axis = []
        y_axis = []
        for x, y in p_dict.items():
            x_axis.append(x)
            y_axis.append(y)
        # print(x_axis, y_axis)
        data = plotly.graph_objs.Scatter(
                x=x_axis,
                y=y_axis,
                name='Scatter',
                mode='lines+markers')

        return {'data': [data],
                'layout': go.Layout(xaxis=dict(range=[min(x_axis),
                                    max(x_axis)]),
                                    yaxis=dict(range=[0, 100]))}

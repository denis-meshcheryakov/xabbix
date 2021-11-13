import dash
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
import plotly
import plotly.graph_objs as go
import yaml


def init_dash_app(server):

    BS = "https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css"

    dash_app = dash.Dash(__name__, server=server,
                         url_base_pathname='/monitoring/',
                         external_stylesheets=[BS])

    dash_app.layout = html.Div(
        children=[
            html.H1(children='Роутер R1'),
            html.Div([dcc.Graph(id='live-graph_R1'),
                     dcc.Interval(
                                id='graph-update_R1',
                                interval=10*1000,
                                n_intervals=10), ]),
            html.H1(children='Роутер R2'),
            html.Div([dcc.Graph(id='live-graph_R2'),
                     dcc.Interval(
                                id='graph-update_R2',
                                interval=10*1000,
                                n_intervals=10), ]),
            html.H1(children='Роутер R3'),
            html.Div([dcc.Graph(id='live-graph_R3'),
                     dcc.Interval(
                                id='graph-update_R3',
                                interval=10*1000,
                                n_intervals=10), ])
                                ])
    init_callbacks(dash_app)
    return dash_app.server


def init_callbacks(dash_app):
    app = dash_app

    @app.callback(
        Output('live-graph_R1', 'figure'),
        [Input('graph-update_R1', 'n_intervals')])
    def update_graph_scatter(n):
        with open('192.168.0.105_success_packet_perc.yaml') as f:
            p_dict = yaml.safe_load(f)
        x_axis = []
        y_axis = []
        for x, y in p_dict.items():
            x_axis.append(x)
            y_axis.append(y)
        data = plotly.graph_objs.Scatter(
                x=x_axis,
                y=y_axis,
                name='Scatter',
                mode='lines+markers')
        return {'data': [data],
                'layout': go.Layout(xaxis=dict(range=[min(x_axis),
                                    max(x_axis)]),
                                    yaxis=dict(range=[0, 110]))}

    @app.callback(
        Output('live-graph_R2', 'figure'),
        [Input('graph-update_R2', 'n_intervals')])
    def update_graph_scatter(n):
        with open('192.168.0.108_success_packet_perc.yaml') as f:
            p_dict = yaml.safe_load(f)
        x_axis = []
        y_axis = []
        for x, y in p_dict.items():
            x_axis.append(x)
            y_axis.append(y)
        data = plotly.graph_objs.Scatter(
                x=x_axis,
                y=y_axis,
                name='Scatter',
                mode='lines+markers')
        return {'data': [data],
                'layout': go.Layout(xaxis=dict(range=[min(x_axis),
                                    max(x_axis)]),
                                    yaxis=dict(range=[0, 110]))}

    @app.callback(
        Output('live-graph_R3', 'figure'),
        [Input('graph-update_R3', 'n_intervals')])
    def update_graph_scatter(n):
        with open('192.168.0.112_success_packet_perc.yaml') as f:
            p_dict = yaml.safe_load(f)
        x_axis = []
        y_axis = []
        for x, y in p_dict.items():
            x_axis.append(x)
            y_axis.append(y)
        data = plotly.graph_objs.Scatter(
                x=x_axis,
                y=y_axis,
                name='Scatter',
                mode='lines+markers')
        return {'data': [data],
                'layout': go.Layout(xaxis=dict(range=[min(x_axis),
                                    max(x_axis)]),
                                    yaxis=dict(range=[0, 110]))}

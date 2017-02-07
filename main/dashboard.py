import psycopg2.extensions
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
from plotly import tools
from os import path
from sys import argv
from base64 import b64decode
from datetime import date
from datetime import timedelta

base_chart = {
    "values": [40, 10, 10, 10, 10, 10, 10],
    "labels": ["-", "-", "-", "-", "-", "-", "-"],
    "domain": {"x": [0, .48]},
    "marker": {
        "colors": [
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)'
        ],
        "line": {
            "width": 1
        }
    },
    "name": "Gauge",
    "hole": .4,
    "type": "pie",
    "direction": "clockwise",
    "rotation": 108,
    "showlegend": False,
    "hoverinfo": "none",
    "textinfo": "none",
    "textposition": "outside"
}

meter_chart = {
    "values": [50, 10, 10, 10, 10, 10],
    "labels": ["Retirada 5.8", "0-20%", "21-40%", "41-60%", "61-80%", "81-100%"],
    "marker": {
        'colors': [
            'rgb(255, 255, 255)',
            'rgb(200,255,200)',
            'rgb(102,255,102)',
            'rgb(51,255,51)',
            'rgb(0,204,0)',
            'rgb(0,153,0)'
        ]
    },
    "domain": {"x": [0, 0.48]},
    "name": "Gauge",
    "hole": .3,
    "type": "pie",
    "direction": "clockwise",
    "rotation": 90,
    "showlegend": False,
    "textinfo": "label",
    "textposition": "inside",
    "hoverinfo": "none"
}

layout = {
    'xaxis': {
        'showticklabels': False,
        'autotick': False,
        'showgrid': False,
        'zeroline': False,
    },
    'yaxis': {
        'showticklabels': False,
        'autotick': False,
        'showgrid': False,
        'zeroline': False,
    },
    'shapes': [
        {
            'type': 'path',
            'path': 'M 0.24 0.5 L 0.20425 0.5715 L 0.24 0.5 Z',
            'fillcolor': 'rgba(0, 0, 0, 0.5)',
            'line': {
                'width': 0.5
            },
            'xref': 'paper',
            'yref': 'paper'
        }
    ],
    'annotations': [
        {
            'xref': 'paper',
            'yref': 'paper',
            'x': 0.23,
            'y': 0.45,
            'text': '50',
            'showarrow': False
        }
    ]
}

# we don't want the boundary now
base_chart['marker']['line']['width'] = 0

fig = {"data": [base_chart, meter_chart],
       "layout": layout}
py.plot(fig, filename='gauge-meter-chart')

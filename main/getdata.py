import psycopg2.extensions
import pandas as pd
import plotly as py
import plotly.graph_objs as go
from plotly import tools
from os import path
from sys import argv
from base64 import b64decode
from datetime import date
from datetime import timedelta
from datetime import datetime


"""
Variáveis para acesso ao Banco de Dados
"""
dbHost = "127.0.0.1"
dbName = "temosportal"
dbUser = "temos"
dbPass = "tw28()KP"

end_date = date.today()
start_contract = '2016-08-22'
start_date = end_date - timedelta(days=7)


def getEvo():
    trace0 = go.Scatter(
        x=[datetime(year=2017, month=2, day=12),
           datetime(year=2017, month=8, day=11)
          ],
        y=[0,460],
        mode = 'lines',
        name = 'Postos Previstos'
    )
    trace1 = go.Scatter(
        x=[datetime(year=2017, month=2, day=13),
           datetime(year=2017, month=2, day=14),
           datetime(year=2017, month=2, day=15),
           datetime(year=2017, month=2, day=16),
           datetime(year=2017, month=2, day=17),
           datetime(year=2017, month=2, day=20),
           datetime(year=2017, month=2, day=21),
           datetime(year=2017, month=2, day=22),
          ],
        y=[5,5,6,8,11,18,21,26],
        mode = 'lines',
        name = 'Postos Realizados'
    )
    data = [trace0, trace1]
    layout = go.Layout(
        title='Evolução dos Postos Completados'
    )
    fig = go.Figure(data=data, layout=layout)
    html = py.offline.plot(fig,
        show_link=False,
        output_type='div',
        include_plotlyjs=True,
        auto_open=False
    )
    return html



def getLinhaBase():
    try:
        with psycopg2.connect(
            database=dbName,
            user=dbUser,
            host=dbHost,
            password=dbPass
        ) as conn_pg:
            with conn_pg.cursor(
            ) as conn_pgs:
                conn_pgs.execute(
                    "SELECT\
                            preventiva,\
                            as_built,\
                            plano_verao,\
                            preditiva,\
                            retirada58,\
                            antena915,\
                            sinal,\
                            outro,\
                            icr,\
                            suporte_angular\
                     FROM abastece_linhabase\
                     ORDER BY data_entrada DESC\
                     LIMIT 1"
                )
                realizado = conn_pgs.fetchall()[0]
                trace1 = go.Bar(
                    y=['Sup. Angular',
                       'ICR',
                       'Outros',
                       'Sinalização',
                       'Ajuste 915',
                       'Retirada 5.8',
                       'Preditiva',
                       'Plano Verão',
                       'As Built',
                       'Preventiva'],
                    x=[realizado[9],
                       realizado[8],
                       realizado[7],
                       realizado[6],
                       realizado[5],
                       realizado[4],
                       realizado[3],
                       realizado[2],
                       realizado[1],
                       realizado[0]],
                    orientation = 'h',
                    name = 'Realizado'
                )

                trace0 = go.Bar(
                    y=['Sup. Angular',
                       'ICR',
                       'Outros',
                       'Sinalização',
                       'Ajuste 915',
                       'Retirada 5.8',
                       'Preditiva',
                       'Plano Verão',
                       'As Built',
                       'Preventiva'],
                    x=[8,
                       25,
                       54,
                       216,
                       460,
                       460,
                       30,
                       460,
                       460,
                       460],
                    orientation = 'h',
                    name = 'Total'
                )
                data = [trace0, trace1]
                layout = go.Layout(
                    title='Acumulado das Ações Individuais'
                )
                fig = go.Figure(data=data, layout=layout)
                html = py.offline.plot(fig,
                    show_link=False,
                    output_type='div',
                    include_plotlyjs=True,
                    auto_open=False
                )
                return html
    except TypeError:
        import sys
        import traceback
        traceback.print_exc(file=sys.stderr)
        return None


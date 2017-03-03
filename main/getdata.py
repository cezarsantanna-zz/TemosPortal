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
                          data_entrada, posto_ok\
                      FROM abastece_linhabase"
                )
                realizado = conn_pgs.fetchall()

        df1 = pd.DataFrame([[ij for ij in i] for i in realizado])
        df1.rename(columns={
            0: 'Data',
            1: 'Postos'
            },
            inplace=True
        )

        trace0 = go.Scatter(
            x=[datetime(year=2017, month=2, day=12),
               datetime(year=2017, month=8, day=11)
            ],
            y=[0,460],
            mode = 'lines',
            name = 'Postos Previstos'
        )
        trace1 = go.Scatter(
            x=df1['Data'],
            y=df1['Postos'],
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

    except TypeError:
        import sys
        import traceback
        traceback.print_exc(file=sys.stderr)
        return None


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
                    "SELECT data_entrada\
                     FROM abastece_linhabase\
                     ORDER BY data_entrada DESC\
                     LIMIT 1"
                )
                data_entrada = conn_pgs.fetchall()[0]
            data_entrada = data_entrada[0]

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
                     LIMIT 2"
                )
                realizado = conn_pgs.fetchall()

            realizado_ontem = realizado[1]
            realizado_hoje = realizado[0]
            realizado = realizado[0]
            realizado_diff_0 = realizado_hoje[0] - realizado_ontem[0]
            realizado_diff_1 = realizado_hoje[1] - realizado_ontem[1]
            realizado_diff_2 = realizado_hoje[2] - realizado_ontem[2]
            realizado_diff_3 = realizado_hoje[3] - realizado_ontem[3]
            realizado_diff_4 = realizado_hoje[4] - realizado_ontem[4]
            realizado_diff_5 = realizado_hoje[5] - realizado_ontem[5]
            realizado_diff_6 = realizado_hoje[6] - realizado_ontem[6]
            realizado_diff_7 = realizado_hoje[7] - realizado_ontem[7]
            realizado_diff_8 = realizado_hoje[8] - realizado_ontem[8]
            realizado_diff_9 = realizado_hoje[9] - realizado_ontem[9]
            trace0 = go.Scatter(
                x=['Sup. Angular',
                   'ICR',
                   'Outros',
                   'Sinalização',
                   'Ajuste 915',
                   'Retirada 5.8',
                   'Preditiva',
                   'Plano Verão',
                   'As Built',
                   'Preventiva'],
                y=[8,
                   25,
                   54,
                   216,
                   460,
                   460,
                   30,
                   460,
                   460,
                   460],
                mode = 'markers',
                name = 'Total',
                marker = dict(
                    color='rgba(173, 21, 21, 0.7)',
                    )
            )
            trace1 = go.Bar(
                x=['Sup. Angular',
                   'ICR',
                   'Outros',
                   'Sinalização',
                   'Ajuste 915',
                   'Retirada 5.8',
                   'Preditiva',
                   'Plano Verão',
                   'As Built',
                   'Preventiva'],
                y=[realizado_ontem[9],
                   realizado_ontem[8],
                   realizado_ontem[7],
                   realizado_ontem[6],
                   realizado_ontem[5],
                   realizado_ontem[4],
                   realizado_ontem[3],
                   realizado_ontem[2],
                   realizado_ontem[1],
                   realizado_ontem[0]],
                name = 'Realizado Aculumado',
                marker=dict(
                    color='rgba(108, 201, 97, 0.7)',
                    line=dict(
                        color='rgba(108, 201, 97, 1.0)',
                        width = 2,
                    )
                )
            )
            trace2 = go.Bar(
                x=['Sup. Angular',
                   'ICR',
                   'Outros',
                   'Sinalização',
                   'Ajuste 915',
                   'Retirada 5.8',
                   'Preditiva',
                   'Plano Verão',
                   'As Built',
                   'Preventiva'],
                y=[realizado_diff_9,
                   realizado_diff_8,
                   realizado_diff_7,
                   realizado_diff_6,
                   realizado_diff_5,
                   realizado_diff_4,
                   realizado_diff_3,
                   realizado_diff_2,
                   realizado_diff_1,
                   realizado_diff_0],
                name = 'Realizado no último Report',
                marker=dict(
                    color='rgba(90, 108, 214, 0.7)',
                    line=dict(
                        color='rgba(90, 108, 214, 1.0)',
                        width = 2,
                    )
                )
            )

            data = [trace0, trace1, trace2]
            layout = go.Layout(
                title='Acumulado das Ações Individuais até %s' % (data_entrada),
                barmode='stack'
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


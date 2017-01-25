import csv
import pandas as pd
import plotly as py
from plotly.graph_objs import *
import psycopg2.extensions
from os import path
from sys import argv
from base64 import b64decode
from datetime import datetime


"""
Variáveis para acesso ao Banco de Dados
"""
dbHost = "127.0.0.1"
dbName = "temosportal"
dbUser = "temos"
dbPass = "tw28()KP"


def getData(_emp_id):
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
                    "SELECT date_trunc('day', to_timestamp(data_realizado)), \
                           sum(CASE \
                                    WHEN abastece_evento.form_id = 1 THEN \
                                       form_id \
                               END) AS MELHORIAS, \
                           sum(CASE \
                                    WHEN abastece_evento.form_id = 2 THEN \
                                       form_id \
                               END) AS CORRETIVAS, \
                           sum(CASE \
                                    WHEN abastece_evento.form_id = 3 THEN \
                                        form_id \
                               END) AS DESINSTALAR, \
                           sum(CASE \
                                    WHEN abastece_evento.form_id = 5 THEN \
                                        form_id \
                               END) AS ANTENA915, \
                           sum(CASE \
                                    WHEN abastece_evento.form_id = 6 THEN \
                                        form_id \
                               END) AS PLANOVERAO, \
                           sum(CASE \
                                    WHEN abastece_evento.form_id = 7 THEN \
                                        form_id \
                               END) AS PREDITIVA, \
                           sum(CASE \
                                    WHEN abastece_evento.form_id = 8 THEN \
                                        form_id \
                               END) AS PREVENTIVA, \
                           sum(CASE \
                                    WHEN abastece_evento.form_id = 9 THEN \
                                        form_id \
                               END) AS ANTENA58, \
                           sum(CASE \
                                    WHEN abastece_evento.form_id = 10 THEN \
                                        form_id \
                               END) AS SINAL, \
                           sum(CASE \
                                    WHEN abastece_evento.form_id = 11 THEN \
                                        form_id \
                               END) AS ICRSURVEY, \
                           sum(CASE \
                                    WHEN abastece_evento.form_id = 14 THEN \
                                        form_id \
                               END) AS ICRINFRA, \
                           sum(CASE \
                                    WHEN abastece_evento.form_id = 15 THEN \
                                        form_id \
                               END) AS ICRCONEX \
                    FROM abastece_evento \
                    WHERE empresa_id = %s \
                    GROUP BY date_trunc('day', to_timestamp(data_realizado));",
                        (_emp_id)
                )
                rows = conn_pgs.fetchall()
                df = pd.DataFrame([[ij for ij in i] for i in rows])
                df.rename(columns={
                    0: 'Data',
                    1: 'A',
                    2: 'Corretivas',
                    3: 'D',
                    4: 'AAntena915',
                    5: 'PlanoVerao',
                    6: 'Preditiva',
                    7: 'Preventiva',
                    8: 'RetiradaAntena58',
                    9: 'Sinal',
                    10: 'ICR Survey',
                    11: 'ICR Infraestrutura',
                    12: 'ICR Conexao'
                    },
                    inplace=True
                )
                df = df.sort_values(by='Data', ascending=[1])

                trace1 = Scatter(
                    x=df['Data'],
                    y=df['A'],
                    mode='line'
                )
                trace2 = Scatter(
                    x=df['Data'],
                    y=df['Corretivas'],
                    mode='line'
                )
                layout = Layout(
                    title='Atendimentos',
                    paper_bgcolor='rgba(220, 220, 220, 1)',
                    plot_bgcolor='rgba(230, 230, 230, 1)',
                )
                data = Data([trace1, trace2])
                fig = Figure(data=data, layout=layout)
                html = py.offline.plot(fig,
                    show_link=False,
                    #output_type='div',
                    include_plotlyjs=True,
                    auto_open=True
                )
                #return html
    except TypeError:
        import sys
        import traceback
        traceback.print_exc(file=sys.stderr)
        return None

if __name__ == '__main__':
    getData(argv[1])

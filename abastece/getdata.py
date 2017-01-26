import psycopg2.extensions
import pandas as pd
import plotly as py
from plotly.graph_objs import *
from plotly import tools
from os import path
from sys import argv
from base64 import b64decode
from datetime import date
from datetime import timedelta


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


def getAtendimentoAcumulados(_emp_id):
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
                    "SELECT base.real,\
                           SUM(sum(base.MEL)) OVER (\
                                                    ORDER BY base.real) \
                                                    AS SUM_MEL,\
                           SUM(sum(base.COR)) OVER (\
                                                    ORDER BY base.real) \
                                                    AS SUM_COR,\
                           SUM(sum(base.DES)) OVER (\
                                                    ORDER BY base.real) \
                                                    AS SUM_DES,\
                           SUM(sum(base.ANT915)) OVER (\
                                                       ORDER BY base.real) \
                                                       AS SUM_ANT915,\
                           SUM(sum(base.PLAV)) OVER (\
                                                     ORDER BY base.real) \
                                                     AS SUM_PLAV,\
                           SUM(sum(base.PRED)) OVER (\
                                                     ORDER BY base.real) \
                                                     AS SUM_PRED,\
                           SUM(sum(base.PREV)) OVER (\
                                                     ORDER BY base.real) \
                                                     AS SUM_PREV,\
                           SUM(sum(base.RET58)) OVER (\
                                                      ORDER BY base.real) \
                                                      AS SUM_RET58,\
                           SUM(sum(base.SIN)) OVER (\
                                                    ORDER BY base.real) \
                                                    AS SUM_SIN,\
                           SUM(sum(base.ICRS)) OVER (\
                                                     ORDER BY base.real) \
                                                     AS SUM_ICRS,\
                           SUM(sum(base.ICRI)) OVER (\
                                                     ORDER BY base.real) \
                                                     AS SUM_ICRI,\
                           SUM(sum(base.ICRC)) OVER (\
                                                     ORDER BY base.real) \
                                                     AS SUM_ICRC\
                    FROM\
                        (SELECT date_trunc('day', \
                        to_timestamp(data_realizado)::TIMESTAMP WITHOUT \
                        TIME ZONE) \
                        AS real,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 1 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS MEL,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 2 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS COR,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 3 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS DES,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 5 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS ANT915,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 6 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS PLAV,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 7 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS PRED,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 8 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS PREV,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 9 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS RET58,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 10 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS SIN,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 11 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS ICRS,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 14 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS ICRI,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 15 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS ICRC\
                         FROM abastece_evento\
                         WHERE empresa_id = %s\
                         GROUP BY real\
                         ORDER BY real) AS base\
                    GROUP BY base.real;",
                        (_emp_id)
                )
                realizados = conn_pgs.fetchall()
                conn_pgs.execute(
                    "SELECT base.real,\
                           SUM(sum(base.MEL)) OVER (\
                                                    ORDER BY base.real) \
                                                    AS SUM_MEL,\
                           SUM(sum(base.COR)) OVER (\
                                                    ORDER BY base.real) \
                                                    AS SUM_COR,\
                           SUM(sum(base.DES)) OVER (\
                                                    ORDER BY base.real) \
                                                    AS SUM_DES,\
                           SUM(sum(base.ANT915)) OVER (\
                                                       ORDER BY base.real) \
                                                       AS SUM_ANT915,\
                           SUM(sum(base.PLAV)) OVER (\
                                                     ORDER BY base.real) \
                                                     AS SUM_PLAV,\
                           SUM(sum(base.PRED)) OVER (\
                                                     ORDER BY base.real) \
                                                     AS SUM_PRED,\
                           SUM(sum(base.PREV)) OVER (\
                                                     ORDER BY base.real) \
                                                     AS SUM_PREV,\
                           SUM(sum(base.RET58)) OVER (\
                                                      ORDER BY base.real) \
                                                      AS SUM_RET58,\
                           SUM(sum(base.SIN)) OVER (\
                                                    ORDER BY base.real) \
                                                    AS SUM_SIN,\
                           SUM(sum(base.ICRS)) OVER (\
                                                     ORDER BY base.real) \
                                                     AS SUM_ICRS,\
                           SUM(sum(base.ICRI)) OVER (\
                                                     ORDER BY base.real) \
                                                     AS SUM_ICRI,\
                           SUM(sum(base.ICRC)) OVER (\
                                                     ORDER BY base.real) \
                                                     AS SUM_ICRC\
                    FROM\
                        (SELECT date_trunc('day', \
                        to_timestamp(data_planejado)::TIMESTAMP WITHOUT \
                        TIME ZONE) \
                        AS real,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 1 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS MEL,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 2 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS COR,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 3 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS DES,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 5 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS ANT915,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 6 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS PLAV,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 7 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS PRED,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 8 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS PREV,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 9 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS RET58,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 10 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS SIN,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 11 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS ICRS,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 14 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS ICRI,\
                                sum(CASE\
                                        WHEN abastece_evento.form_id = 15 \
                                        THEN 1\
                                        ELSE 0\
                                    END) AS ICRC\
                         FROM abastece_evento\
                         WHERE empresa_id = %s\
                         GROUP BY real\
                         ORDER BY real) AS base\
                    GROUP BY base.real;",
                        (_emp_id)
                )
                previstos = conn_pgs.fetchall()
                df1 = pd.DataFrame([[ij for ij in i] for i in previstos])
                df2 = pd.DataFrame([[ij for ij in i] for i in realizados])
                df1.rename(columns={
                    0: 'Data',
                    1: 'MEL',
                    2: 'COR',
                    3: 'DES',
                    4: 'ANT915',
                    5: 'PLANV',
                    6: 'PRED',
                    7: 'PREV',
                    8: 'RET58',
                    9: 'SIN',
                    10: 'ICRS',
                    11: 'ICRI',
                    12: 'ICRC'
                    },
                    inplace=True
                )
                df2.rename(columns={
                    0: 'Data',
                    1: 'MEL',
                    2: 'COR',
                    3: 'DES',
                    4: 'ANT915',
                    5: 'PLANV',
                    6: 'PRED',
                    7: 'PREV',
                    8: 'RET58',
                    9: 'SIN',
                    10: 'ICRS',
                    11: 'ICRI',
                    12: 'ICRC'
                    },
                    inplace=True
                )
                df1 = df1.sort_values(by='Data', ascending=[1])
                df2 = df1.sort_values(by='Data', ascending=[1])

                trace1_a = Scatter(
                    x=df1['Data'],
                    y=df1['MEL'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace1_b = Scatter(
                    x=df2['Data'],
                    y=df2['MEL'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace2_a = Scatter(
                    x=df1['Data'],
                    y=df1['COR'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace2_b = Scatter(
                    x=df2['Data'],
                    y=df2['COR'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace3_a = Scatter(
                    x=df1['Data'],
                    y=df1['DES'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace3_b = Scatter(
                    x=df2['Data'],
                    y=df2['DES'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace4_a = Scatter(
                    x=df1['Data'],
                    y=df1['ANT915'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace4_b = Scatter(
                    x=df2['Data'],
                    y=df2['ANT915'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace5_a = Scatter(
                    x=df1['Data'],
                    y=df1['PLANV'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace5_b = Scatter(
                    x=df2['Data'],
                    y=df2['PLANV'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace6_a = Scatter(
                    x=df1['Data'],
                    y=df1['PRED'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace6_b = Scatter(
                    x=df2['Data'],
                    y=df2['PRED'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace7_a = Scatter(
                    x=df1['Data'],
                    y=df1['PREV'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace7_b = Scatter(
                    x=df2['Data'],
                    y=df2['PREV'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace8_a = Scatter(
                    x=df1['Data'],
                    y=df1['RET58'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace8_b = Scatter(
                    x=df2['Data'],
                    y=df2['RET58'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace9_a = Scatter(
                    x=df1['Data'],
                    y=df1['SIN'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace9_b = Scatter(
                    x=df2['Data'],
                    y=df2['SIN'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace10_a = Scatter(
                    x=df1['Data'],
                    y=df1['ICRS'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace10_b = Scatter(
                    x=df2['Data'],
                    y=df2['ICRS'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace11_a = Scatter(
                    x=df1['Data'],
                    y=df1['ICRI'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace11_b = Scatter(
                    x=df2['Data'],
                    y=df2['ICRI'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace12_a = Scatter(
                    x=df1['Data'],
                    y=df1['ICRC'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace12_b = Scatter(
                    x=df2['Data'],
                    y=df2['ICRC'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                fig = tools.make_subplots(
                    rows=12,
                    cols=1,
                    subplot_titles=(
                    'Corretivas',
                    'Preventivas',
                    'Preditivas',
                    'Ações de Melhoria',
                    'Plano Verão',
                    'Retirada Antena 5.8GHz',
                    'Ajuste Antena 915MHz',
                    'Survey ICR',
                    'Infraestrutura ICR',
                    'Conexão ICR',
                    'Sinalizações',
                    'Desinstalações de Postos'
                    ),
                    shared_xaxes=True,
                    shared_yaxes=False,
                )
                fig.append_trace(trace2_a, 1, 1)
                fig.append_trace(trace2_b, 1, 1)
                fig.append_trace(trace7_a, 2, 1)
                fig.append_trace(trace7_b, 2, 1)
                fig.append_trace(trace6_a, 3, 1)
                fig.append_trace(trace6_b, 3, 1)
                fig.append_trace(trace1_a, 4, 1)
                fig.append_trace(trace1_b, 4, 1)
                fig.append_trace(trace5_a, 5, 1)
                fig.append_trace(trace5_b, 5, 1)
                fig.append_trace(trace8_a, 6, 1)
                fig.append_trace(trace8_b, 6, 1)
                fig.append_trace(trace4_a, 7, 1)
                fig.append_trace(trace4_b, 7, 1)
                fig.append_trace(trace10_a, 8, 1)
                fig.append_trace(trace10_b, 8, 1)
                fig.append_trace(trace11_a, 9, 1)
                fig.append_trace(trace11_b, 9, 1)
                fig.append_trace(trace12_a, 10, 1)
                fig.append_trace(trace12_b, 10, 1)
                fig.append_trace(trace9_a, 11, 1)
                fig.append_trace(trace9_b, 11, 1)
                fig.append_trace(trace3_a, 12, 1)
                fig.append_trace(trace3_b, 12, 1)

                fig['layout'].update(
                    height=2500,
                    #width=650,
                    showlegend=False,
                    title='<b>Atendimentos Acumulado</b>',
                    paper_bgcolor='rgba(220, 220, 220, 1)',
                    plot_bgcolor='rgba(230, 230, 230, 1)',
                    autosize=True,
                    margin=Margin(
                        l=25,
                        r=25,
                        b=0,
                        t=60,
                        pad=4
                    ),
                    xaxis=dict(
                        range=(start_contract, end_date),
                        type='date',
                        autorange=False,
                    ),


                )
                html = py.offline.plot(fig,
                    show_link=False,
                    output_type='div',
                    include_plotlyjs=False,
                    auto_open=False
                )
                return html
    except TypeError:
        import sys
        import traceback
        traceback.print_exc(file=sys.stderr)
        return None

def getAtendimentoDia(_emp_id):
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
                    "SELECT date_trunc('day', \
                     to_timestamp(data_planejado)::TIMESTAMP WITHOUT \
                     TIME ZONE) \
                     AS real,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 1 THEN 1\
                                    ELSE 0\
                                END) AS MEL,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 2 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS COR,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 3 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS DES,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 5 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS ANT915,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 6 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS PLAV,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 7 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS PRED,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 8 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS PREV,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 9 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS RET58,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 10 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS SIN,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 11 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS ICRS,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 14 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS ICRI,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 15 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS ICRC\
                     FROM abastece_evento\
                     WHERE empresa_id = %s\
                     GROUP BY real\
                     ORDER BY real;",
                    (_emp_id)
                )
                previstos = conn_pgs.fetchall()
                conn_pgs.execute(
                    "SELECT date_trunc('day', \
                     to_timestamp(data_realizado)::TIMESTAMP WITHOUT \
                     TIME ZONE) \
                     AS real,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 1 THEN 1\
                                    ELSE 0\
                                END) AS MEL,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 2 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS COR,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 3 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS DES,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 5 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS ANT915,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 6 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS PLAV,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 7 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS PRED,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 8 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS PREV,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 9 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS RET58,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 10 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS SIN,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 11 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS ICRS,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 14 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS ICRI,\
                            sum(CASE\
                                    WHEN abastece_evento.form_id = 15 \
                                    THEN 1\
                                    ELSE 0\
                                END) AS ICRC\
                     FROM abastece_evento\
                     WHERE empresa_id = %s\
                     GROUP BY real\
                     ORDER BY real;",
                    (_emp_id)
                )
                realizados = conn_pgs.fetchall()
                df1 = pd.DataFrame([[ij for ij in i] for i in previstos])
                df2 = pd.DataFrame([[ij for ij in i] for i in realizados])
                df1.rename(columns={
                    0: 'Data',
                    1: 'MEL',
                    2: 'COR',
                    3: 'DES',
                    4: 'ANT915',
                    5: 'PLANV',
                    6: 'PRED',
                    7: 'PREV',
                    8: 'RET58',
                    9: 'SIN',
                    10: 'ICRS',
                    11: 'ICRI',
                    12: 'ICRC'
                    },
                    inplace=True
                )
                df2.rename(columns={
                    0: 'Data',
                    1: 'MEL',
                    2: 'COR',
                    3: 'DES',
                    4: 'ANT915',
                    5: 'PLANV',
                    6: 'PRED',
                    7: 'PREV',
                    8: 'RET58',
                    9: 'SIN',
                    10: 'ICRS',
                    11: 'ICRI',
                    12: 'ICRC'
                    },
                    inplace=True
                )
                df1 = df1.sort_values(by='Data', ascending=[1])
                df2 = df1.sort_values(by='Data', ascending=[1])

                trace1_a = Scatter(
                    x=df1['Data'],
                    y=df1['MEL'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace1_b = Scatter(
                    x=df2['Data'],
                    y=df2['MEL'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace2_a = Scatter(
                    x=df1['Data'],
                    y=df1['COR'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace2_b = Scatter(
                    x=df2['Data'],
                    y=df2['COR'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace3_a = Scatter(
                    x=df1['Data'],
                    y=df1['DES'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace3_b = Scatter(
                    x=df2['Data'],
                    y=df2['DES'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace4_a = Scatter(
                    x=df1['Data'],
                    y=df1['ANT915'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace4_b = Scatter(
                    x=df2['Data'],
                    y=df2['ANT915'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace5_a = Scatter(
                    x=df1['Data'],
                    y=df1['PLANV'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace5_b = Scatter(
                    x=df2['Data'],
                    y=df2['PLANV'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace6_a = Scatter(
                    x=df1['Data'],
                    y=df1['PRED'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace6_b = Scatter(
                    x=df2['Data'],
                    y=df2['PRED'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace7_a = Scatter(
                    x=df1['Data'],
                    y=df1['PREV'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace7_b = Scatter(
                    x=df2['Data'],
                    y=df2['PREV'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace8_a = Scatter(
                    x=df1['Data'],
                    y=df1['RET58'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace8_b = Scatter(
                    x=df2['Data'],
                    y=df2['RET58'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace9_a = Scatter(
                    x=df1['Data'],
                    y=df1['SIN'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace9_b = Scatter(
                    x=df2['Data'],
                    y=df2['SIN'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace10_a = Scatter(
                    x=df1['Data'],
                    y=df1['ICRS'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace10_b = Scatter(
                    x=df2['Data'],
                    y=df2['ICRS'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace11_a = Scatter(
                    x=df1['Data'],
                    y=df1['ICRI'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace11_b = Scatter(
                    x=df2['Data'],
                    y=df2['ICRI'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                trace12_a = Scatter(
                    x=df1['Data'],
                    y=df1['ICRC'],
                    mode='line',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                trace12_b = Scatter(
                    x=df2['Data'],
                    y=df2['ICRC'],
                    mode='line',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                fig = tools.make_subplots(
                    rows=12,
                    cols=1,
                    subplot_titles=(
                    'Corretivas',
                    'Preventivas',
                    'Preditivas',
                    'Ações de Melhoria',
                    'Plano Verão',
                    'Retirada Antena 5.8GHz',
                    'Ajuste Antena 915MHz',
                    'Survey ICR',
                    'Infraestrutura ICR',
                    'Conexão ICR',
                    'Sinalizações',
                    'Desinstalações de Postos'
                    ),
                    shared_xaxes=True,
                    shared_yaxes=False,
                )
                fig.append_trace(trace2_a, 1, 1)
                fig.append_trace(trace2_b, 1, 1)
                fig.append_trace(trace7_a, 2, 1)
                fig.append_trace(trace7_b, 2, 1)
                fig.append_trace(trace6_a, 3, 1)
                fig.append_trace(trace6_b, 3, 1)
                fig.append_trace(trace1_a, 4, 1)
                fig.append_trace(trace1_b, 4, 1)
                fig.append_trace(trace5_a, 5, 1)
                fig.append_trace(trace5_b, 5, 1)
                fig.append_trace(trace8_a, 6, 1)
                fig.append_trace(trace8_b, 6, 1)
                fig.append_trace(trace4_a, 7, 1)
                fig.append_trace(trace4_b, 7, 1)
                fig.append_trace(trace10_a, 8, 1)
                fig.append_trace(trace10_b, 8, 1)
                fig.append_trace(trace11_a, 9, 1)
                fig.append_trace(trace11_b, 9, 1)
                fig.append_trace(trace12_a, 10, 1)
                fig.append_trace(trace12_b, 10, 1)
                fig.append_trace(trace9_a, 11, 1)
                fig.append_trace(trace9_b, 11, 1)
                fig.append_trace(trace3_a, 12, 1)
                fig.append_trace(trace3_b, 12, 1)

                fig['layout'].update(
                    height=2500,
                    #width=650,
                    showlegend=False,
                    title='<b>Atendimentos Diários</b>',
                    paper_bgcolor='rgba(220, 220, 220, 1)',
                    plot_bgcolor='rgba(230, 230, 230, 1)',
                    autosize=True,
                    margin=Margin(
                        l=25,
                        r=25,
                        b=0,
                        t=60,
                        pad=4
                    ),
                    xaxis=dict(
                        range=(start_date, end_date),
                        type='date',
                        autorange=False,
                    ),

                )
                html = py.offline.plot(fig,
                    show_link=False,
                    output_type='div',
                    include_plotlyjs=False,
                    auto_open=False
                )
                return html
    except TypeError:
        import sys
        import traceback
        traceback.print_exc(file=sys.stderr)
        return None


if __name__ == '__main__':
    if argv[1] == 'acu':
        getAtendimentoAcumulados(argv[2])
    elif argv[1] == 'dia':
        getAtendimentoDia(argv[2])
    else:
        pass

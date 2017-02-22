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


def getKPIs(_emp_id):
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
                    "SELECT base.planejada,\
                           SUM(sum(base.MEL)) OVER (\
                                                    ORDER BY base.planejada) \
                                                    AS SUM_MEL,\
                           SUM(sum(base.COR)) OVER (\
                                                    ORDER BY base.planejada) \
                                                    AS SUM_COR,\
                           SUM(sum(base.DES)) OVER (\
                                                    ORDER BY base.planejada) \
                                                    AS SUM_DES,\
                           SUM(sum(base.ANT915)) OVER (\
                                                       ORDER BY base.planejada)\
                                                       AS SUM_ANT915,\
                           SUM(sum(base.PLAV)) OVER (\
                                                     ORDER BY base.planejada) \
                                                     AS SUM_PLAV,\
                           SUM(sum(base.PRED)) OVER (\
                                                     ORDER BY base.planejada) \
                                                     AS SUM_PRED,\
                           SUM(sum(base.PREV)) OVER (\
                                                     ORDER BY base.planejada) \
                                                     AS SUM_PREV,\
                           SUM(sum(base.RET58)) OVER (\
                                                      ORDER BY base.planejada) \
                                                      AS SUM_RET58,\
                           SUM(sum(base.SIN)) OVER (\
                                                    ORDER BY base.planejada) \
                                                    AS SUM_SIN,\
                           SUM(sum(base.ICRS)) OVER (\
                                                     ORDER BY base.planejada) \
                                                     AS SUM_ICRS,\
                           SUM(sum(base.ICRI)) OVER (\
                                                     ORDER BY base.planejada) \
                                                     AS SUM_ICRI,\
                           SUM(sum(base.ICRC)) OVER (\
                                                     ORDER BY base.planejada) \
                                                     AS SUM_ICRC\
                    FROM\
                        (SELECT date_trunc('day', to_timestamp(data_planejado -\
                            extract(timezone from \
                            date_trunc('day', to_timestamp(data_planejado))))) \
                            AS planejada,\
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
                         GROUP BY planejada\
                         ORDER BY planejada) AS base\
                    GROUP BY base.planejada;",
                        (_emp_id)
                )
                previstos = conn_pgs.fetchall()
                df1 = pd.DataFrame([[ij for ij in i] for i in previstos])
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
                df1 = df1.sort_values(by='Data', ascending=[1])

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

                conn_pgs.execute(
                    "SELECT base.realizada,\
                           SUM(sum(base.MEL)) OVER (\
                                                    ORDER BY base.realizada) \
                                                    AS SUM_MEL,\
                           SUM(sum(base.COR)) OVER (\
                                                    ORDER BY base.realizada) \
                                                    AS SUM_COR,\
                           SUM(sum(base.DES)) OVER (\
                                                    ORDER BY base.realizada) \
                                                    AS SUM_DES,\
                           SUM(sum(base.ANT915)) OVER (\
                                                       ORDER BY base.realizada)\
                                                       AS SUM_ANT915,\
                           SUM(sum(base.PLAV)) OVER (\
                                                     ORDER BY base.realizada) \
                                                     AS SUM_PLAV,\
                           SUM(sum(base.PRED)) OVER (\
                                                     ORDER BY base.realizada) \
                                                     AS SUM_PRED,\
                           SUM(sum(base.PREV)) OVER (\
                                                     ORDER BY base.realizada) \
                                                     AS SUM_PREV,\
                           SUM(sum(base.RET58)) OVER (\
                                                      ORDER BY base.realizada) \
                                                      AS SUM_RET58,\
                           SUM(sum(base.SIN)) OVER (\
                                                    ORDER BY base.realizada) \
                                                    AS SUM_SIN,\
                           SUM(sum(base.ICRS)) OVER (\
                                                     ORDER BY base.realizada) \
                                                     AS SUM_ICRS,\
                           SUM(sum(base.ICRI)) OVER (\
                                                     ORDER BY base.realizada) \
                                                     AS SUM_ICRI,\
                           SUM(sum(base.ICRC)) OVER (\
                                                     ORDER BY base.realizada) \
                                                     AS SUM_ICRC\
                    FROM\
                        (SELECT date_trunc('day', to_timestamp(data_realizado -\
                            extract(timezone from \
                            date_trunc('day', to_timestamp(data_realizado))))) \
                            AS realizada,\
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
                         GROUP BY realizada\
                         ORDER BY realizada) AS base\
                    GROUP BY base.realizada;",
                        (_emp_id)
                )
                realizados = conn_pgs.fetchall()
                df2 = pd.DataFrame([[ij for ij in i] for i in realizados])
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
                df2 = df2.sort_values(by='Data', ascending=[1])

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
                    height=3500,
                    #width=650,
                    showlegend=False,
                    title='<b>Atendimentos Acumulado</b>',
                    paper_bgcolor='rgba(220, 220, 220, 1)',
                    plot_bgcolor='rgba(230, 230, 230, 1)',
                    autosize=True,
                    margin=Margin(
                        l=35,
                        r=35,
                        b=0,
                        t=60,
                    ),
                    xaxis=dict(
                        range=(start_contract, end_date),
                        type='date',
                        autorange=True,
                    ),
                )
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
                    "SELECT date_trunc('day', to_timestamp(data_planejado -\
                        extract(timezone from \
                        date_trunc('day', to_timestamp(data_planejado))))) \
                        AS planejada,\
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
                     GROUP BY planejada\
                     ORDER BY planejada;",
                    (_emp_id)
                )
                previstos = conn_pgs.fetchall()
                df1 = pd.DataFrame([[ij for ij in i] for i in previstos])
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
                df1 = df1.sort_values(by='Data', ascending=[1])

                mel_plan = Scatter(
                    x=df1['Data'],
                    y=df1['MEL'],
                    mode='line',
                    xaxis='x',
                    yaxis='y',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                cor_plan = Scatter(
                    x=df1['Data'],
                    y=df1['COR'],
                    mode='line',
                    xaxis='x2',
                    yaxis='y2',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                des_plan = Scatter(
                    x=df1['Data'],
                    y=df1['DES'],
                    mode='line',
                    xaxis='x3',
                    yaxis='y3',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                ant915_plan = Scatter(
                    x=df1['Data'],
                    y=df1['ANT915'],
                    mode='line',
                    xaxis='x4',
                    yaxis='y4',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                planv_plan = Scatter(
                    x=df1['Data'],
                    y=df1['PLANV'],
                    mode='line',
                    xaxis='x5',
                    yaxis='y5',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                pred_plan = Scatter(
                    x=df1['Data'],
                    y=df1['PRED'],
                    mode='line',
                    xaxis='x6',
                    yaxis='y6',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                prev_plan = Scatter(
                    x=df1['Data'],
                    y=df1['PREV'],
                    mode='line',
                    xaxis='x7',
                    yaxis='y7',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                ret58_plan = Scatter(
                    x=df1['Data'],
                    y=df1['RET58'],
                    mode='line',
                    xaxis='x8',
                    yaxis='y8',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                sin_plan = Scatter(
                    x=df1['Data'],
                    y=df1['SIN'],
                    mode='line',
                    xaxis='x9',
                    yaxis='y9',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                icrs_plan = Scatter(
                    x=df1['Data'],
                    y=df1['ICRS'],
                    mode='line',
                    xaxis='x10',
                    yaxis='y10',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                icri_plan = Scatter(
                    x=df1['Data'],
                    y=df1['ICRI'],
                    mode='line',
                    xaxis='x11',
                    yaxis='y11',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )

                conn_pgs.execute(
                    "SELECT date_trunc('day', to_timestamp(data_realizado -\
                        extract(timezone from \
                        date_trunc('day', to_timestamp(data_realizado))))) \
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

                df2 = pd.DataFrame([[ij for ij in i] for i in realizados])
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
                df2 = df2.sort_values(by='Data', ascending=[1])

                mel_real = Scatter(
                    x=df2['Data'],
                    y=df2['MEL'],
                    mode='line',
                    xaxis='x',
                    yaxis='y',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                cor_real = Scatter(
                    x=df2['Data'],
                    y=df2['COR'],
                    mode='line',
                    xaxis='x2',
                    yaxis='y2',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                des_real = Scatter(
                    x=df2['Data'],
                    y=df2['DES'],
                    mode='line',
                    xaxis='x3',
                    yaxis='y3',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                ant915_real = Scatter(
                    x=df2['Data'],
                    y=df2['ANT915'],
                    mode='line',
                    xaxis='x4',
                    yaxis='y4',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                planv_real = Scatter(
                    x=df2['Data'],
                    y=df2['PLANV'],
                    mode='line',
                    xaxis='x5',
                    yaxis='y5',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                pred_real = Scatter(
                    x=df2['Data'],
                    y=df2['PRED'],
                    mode='line',
                    xaxis='x6',
                    yaxis='y6',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                prev_real = Scatter(
                    x=df2['Data'],
                    y=df2['PREV'],
                    mode='line',
                    xaxis='x7',
                    yaxis='y7',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                ret58_real = Scatter(
                    x=df2['Data'],
                    y=df2['RET58'],
                    mode='line',
                    xaxis='x8',
                    yaxis='y8',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                sin_real = Scatter(
                    x=df2['Data'],
                    y=df2['SIN'],
                    mode='line',
                    xaxis='x9',
                    yaxis='y9',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                icrs_real = Scatter(
                    x=df2['Data'],
                    y=df2['ICRS'],
                    mode='line',
                    xaxis='x10',
                    yaxis='y10',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                icri_real = Scatter(
                    x=df2['Data'],
                    y=df2['ICRI'],
                    mode='line',
                    xaxis='x11',
                    yaxis='y11',
                    line=dict(
                        color = ('rgb(205, 12, 24)'),
                        width = 1,
                    ),
                    name='Realizado'
                )
                icrc_plan = Scatter(
                    x=df1['Data'],
                    y=df1['ICRC'],
                    mode='line',
                    xaxis='x12',
                    yaxis='y12',
                    line=dict(
                        color = ('rgb(0, 0, 0)'),
                        width = 1,
                    ),
                    name='Previsto'
                )
                icrc_real = Scatter(
                    x=df2['Data'],
                    y=df2['ICRC'],
                    mode='line',
                    xaxis='x12',
                    yaxis='y12',
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
                )
                fig.append_trace(cor_plan, 1, 1)
                fig.append_trace(cor_real, 1, 1)
                fig.append_trace(prev_plan, 2, 1)
                fig.append_trace(prev_real, 2, 1)
                fig.append_trace(pred_plan, 3, 1)
                fig.append_trace(pred_real, 3, 1)
                fig.append_trace(mel_plan, 4, 1)
                fig.append_trace(mel_real, 4, 1)
                fig.append_trace(planv_plan, 5, 1)
                fig.append_trace(planv_real, 5, 1)
                fig.append_trace(ret58_plan, 6, 1)
                fig.append_trace(ret58_real, 6, 1)
                fig.append_trace(ant915_plan, 7, 1)
                fig.append_trace(ant915_real, 7, 1)
                fig.append_trace(icrs_plan, 8, 1)
                fig.append_trace(icrs_real, 8, 1)
                fig.append_trace(icri_plan, 9, 1)
                fig.append_trace(icri_real, 9, 1)
                fig.append_trace(icrc_plan, 10, 1)
                fig.append_trace(icrc_real, 10, 1)
                fig.append_trace(sin_plan, 11, 1)
                fig.append_trace(sin_real, 11, 1)
                fig.append_trace(des_plan, 12, 1)
                fig.append_trace(des_real, 12, 1)

                fig['layout']['yaxis1'].update(range=[0, 25])
                fig['layout']['yaxis2'].update(range=[0, 15])
                fig['layout']['yaxis3'].update(range=[0, 15])
                fig['layout']['yaxis4'].update(range=[0, 15])
                fig['layout']['yaxis5'].update(range=[0, 15])
                fig['layout']['yaxis6'].update(range=[0, 15])
                fig['layout']['yaxis7'].update(range=[0, 15])
                fig['layout']['yaxis8'].update(range=[0, 15])
                fig['layout']['yaxis9'].update(range=[0, 15])
                fig['layout']['yaxis10'].update(range=[0, 15])
                fig['layout']['yaxis11'].update(range=[0, 15])
                fig['layout']['yaxis12'].update(range=[0, 15])
                fig['layout'].update(
                    height=3500,
                    #width=650,
                    showlegend=False,
                    title='<b>Atendimentos Diários</b>',
                    paper_bgcolor='rgba(220, 220, 220, 1)',
                    plot_bgcolor='rgba(230, 230, 230, 1)',
                    autosize=True,
                    margin=Margin(
                        l=35,
                        r=35,
                        b=50,
                        t=50,
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
                    include_plotlyjs=True,
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

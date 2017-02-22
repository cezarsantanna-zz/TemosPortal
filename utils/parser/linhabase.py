#!/home/cezar.santanna/.virtualenvs/abastece/bin/python
# -*- coding: utf-8 -*-
import csv
import psycopg2.extensions
from io import StringIO
from datetime import datetime
from datetime import date
from lxml import html


"""
Variáveis para acesso ao Banco de Dados
"""
dbHost = "127.0.0.1"
dbName = "temosportal"
dbUser = "temos"
dbPass = "tw28()KP"

def getPostoID(_CGMP):
    """
    Esta função retorna o ID do posto na base abastece_posto baseada no código
    CGMP de cada posto cadastrado
    O código CGMP é um número inteiro de 4 digitos.
    Caso não seja possível encontrar o ID para o código CGMP fornecido, será
    retornado o valor None, que deve ser tratado pelo processo chamador.
    """
    try:
        if _CGMP is None:
            raise ValueError('Código CGMP não pode ser vazio')
    except ValueError:
        print('Erro encontrado')
        raise
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
                    "SELECT id FROM abastece_posto \
                     WHERE active = True and cgmp = (%s);",
                    (_CGMP,)
                )
                _id = int(conn_pgs.fetchone()[0])
                return _id
    except TypeError:
        import sys
        import traceback
        print('Erro ao obter ID do Posto ', _CGMP, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


def checkData(_data):
    if _data == '':
        return None
    elif _data == 'OK':
        return date(year=2016, month=12, day=31)
    else:
        data = date(year = int(_data.split('/')[2]),
                    month = int(_data.split('/')[1]),
                    day = int(_data.split('/')[0])
               )
        return data
       


def parserCronograma(_source, _attach, _data):
    dest_err = _source.replace('/new/', '/Cronograma/not_parsed/')
    dest_ok = _source.replace('/new/', '/Cronograma/parsed/')
    buffer = StringIO(_attach)
    csvreader = csv.reader(buffer)
    try:
        with psycopg2.connect(
            database=dbName,
            user=dbUser,
            host=dbHost,
            password=dbPass
        ) as conn_pg:
            with conn_pg.cursor() as conn_pgs:
                for line in csvreader:
                    ano = int(_data[0:4])
                    mes = int(_data[4:6])
                    dia = int(_data[6:8])
                    data_entrada = date(year = ano,
                                        month = mes,
                                        day = dia)
                    posto_id = getPostoID(line[0])
                    preventiva = checkData(line[1])
                    asbuilt = checkData(line[2])
                    plano_verao = checkData(line[3])
                    preditiva = checkData(line[4])
                    retirada58 = checkData(line[5])
                    antena915 = checkData(line[6])
                    sinal = checkData(line[7])
                    outro = checkData(line[8])
                    icr = checkData(line[9])
                    suporte_angular = checkData(line[10])
                    conn_pgs.execute(
                        'INSERT INTO abastece_cronograma\
                         (data_entrada, posto_id,\
                          preventiva, asbuilt, plano_verao,\
                          preditiva, retirada58, antena915,\
                          sinal, outro, icr, suporte_angular)\
                         VALUES \
                         (%s, %s, %s, %s, %s, %s, %s, %s, %s,\
                          %s, %s, %s);',
                         (data_entrada, posto_id,
                          preventiva, asbuilt, plano_verao,
                          preditiva, retirada58, antena915,
                          sinal, outro, icr, suporte_angular,)
                    )
                    status = conn_pgs.statusmessage
                    if status == 'INSERT 0':
                        return dest_err
                    else:
                        pass
                return dest_ok
    except:
        import sys
        import traceback
        print('Whoops! Problem:', file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return dest_err

def parserTotais(_source, _attach, data_entrada):
    dest_err = _source.replace('/new/', '/Totais/not_parsed/')
    dest_ok = _source.replace('/new/', '/Totais/parsed/')
    return dest_err

def parserLinhaBase(_source, _mail):
    if 'Cronograma_Atividades_E2i9_Totais' in _mail.subject:
        _attach = _mail.attachments_list[0]['payload']
        _data_entrada = _mail.subject.split('_')[4]
        return parserTotais(_source, _attach, _data_entrada)
    elif 'Cronograma_Atividades_E2i9' in _mail.subject:
        _attach = _mail.attachments_list[0]['payload']
        _data_entrada = _mail.subject.split('_')[3]
        return parserCronograma(_source, _attach, _data_entrada)
    else:
        return _source.replace('/new/', '/ServiceNow/Others/not_parsed/')

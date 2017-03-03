#!/home/cezar.santanna/.virtualenvs/abastece/bin/python
# -*- coding: utf-8 -*-
import csv
import psycopg2.extensions
from io import StringIO
from datetime import datetime
from datetime import date
from lxml import html
from sys import argv

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
        return '-'
    else:
        return _data

def DateFromExcel(_data):
    return date.fromordinal(date(1900, 1, 1).toordinal() + int(_data) - 2)


def parserCronograma(_source, _attach):
    dest_err = _source.replace('/new/', '/Cronograma/not_parsed/')
    dest_ok = _source.replace('/new/', '/Cronograma/parsed/')
    buffer = StringIO(_attach)
    csvreader = csv.reader(buffer, delimiter=';')
    try:
        with psycopg2.connect(
            database=dbName,
            user=dbUser,
            host=dbHost,
            password=dbPass
        ) as conn_pg:
            with conn_pg.cursor() as conn_pgs:
                conn_pgs.execute(
                    'TRUNCATE abastece_cronograma'
                )
                for line in csvreader:
                    posto_cgmp = line[0][:4]
                    posto_nome = line[1][:50]
                    preventiva = checkData(line[2])
                    asbuilt = checkData(line[3])
                    plano_verao = checkData(line[4])
                    preditiva = checkData(line[5])
                    retirada58 = checkData(line[6])
                    antena915 = checkData(line[7])
                    sinal = checkData(line[8])
                    outro = checkData(line[9])
                    icr = checkData(line[10])
                    suporte_angular = checkData(line[11])
                    conn_pgs.execute(
                        'INSERT INTO abastece_cronograma\
                         (posto_cgmp, posto_nome,\
                          preventiva, asbuilt, plano_verao,\
                          preditiva, retirada58, antena915,\
                          sinal, outro, icr, suporte_angular)\
                         VALUES \
                         (%s, %s, %s, %s, %s, %s, %s, %s, %s,\
                          %s, %s, %s);',
                         (posto_cgmp, posto_nome,
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


def parserCronogramaFromFile(_filename):
    with open(_filename, 'r') as srcfile:
        csvreader = csv.reader(srcfile, delimiter=';')
        try:
            with psycopg2.connect(
                database=dbName,
                user=dbUser,
                host=dbHost,
                password=dbPass
            ) as conn_pg:
                with conn_pg.cursor() as conn_pgs:
                    conn_pgs.execute(
                        'TRUNCATE abastece_cronograma'
                    )
                    for line in csvreader:
                        posto_cgmp = line[0]
                        posto_nome = line[1]
                        preventiva = checkData(line[2])
                        asbuilt = checkData(line[3])
                        plano_verao = checkData(line[4])
                        preditiva = checkData(line[5])
                        retirada58 = checkData(line[6])
                        antena915 = checkData(line[7])
                        sinal = checkData(line[8])
                        outro = checkData(line[9])
                        icr = checkData(line[10])
                        suporte_angular = checkData(line[11])
                        conn_pgs.execute(
                            'INSERT INTO abastece_cronograma\
                             (posto_cgmp, posto_nome,\
                              preventiva, asbuilt, plano_verao,\
                              preditiva, retirada58, antena915,\
                              sinal, outro, icr, suporte_angular)\
                             VALUES \
                             (%s, %s, %s, %s, %s, %s, %s, %s, %s,\
                              %s, %s, %s);',
                             (posto_cgmp, posto_nome,
                              preventiva, asbuilt, plano_verao,
                              preditiva, retirada58, antena915,
                              sinal, outro, icr, suporte_angular,)
                        )
        except:
            import sys
            import traceback
            print('Whoops! Problem:', file=sys.stderr)
            traceback.print_exc(file=sys.stderr)


def parserTotais(_source, _attach):
    dest_err = _source.replace('/new/', '/Totais/not_parsed/')
    dest_ok = _source.replace('/new/', '/Totais/parsed/')
    buffer = StringIO(_attach)
    csvreader = csv.reader(buffer, delimiter=';')
    try:
        with psycopg2.connect(
            database=dbName,
            user=dbUser,
            host=dbHost,
            password=dbPass
        ) as conn_pg:
            with conn_pg.cursor() as conn_pgs:
                for line in csvreader:
                    preventiva = line[1]
                    as_built = line[2]
                    plano_verao = line[3]
                    preditiva = line[4]
                    retirada58 = line[5]
                    antena915 = line[6]
                    sinal = line[7]
                    outro = line[8]
                    icr = line[9]
                    suporte_angular = line[10]
                    posto_ok = line[11]
                    data_entrada = DateFromExcel(line[12])
                    conn_pgs.execute(
                        'INSERT INTO abastece_linhabase\
                         (data_entrada,\
                          preventiva, as_built, plano_verao,\
                          preditiva, retirada58, antena915,\
                          sinal, outro, icr, suporte_angular,\
                          posto_ok)\
                         VALUES \
                         (%s, %s, %s, %s, %s, %s, %s, %s, %s,\
                          %s, %s, %s);',
                         (data_entrada,
                          preventiva, as_built, plano_verao,
                          preditiva, retirada58, antena915,
                          sinal, outro, icr, suporte_angular,
                          posto_ok,)
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

def parserLinhaBase(_source, _mail):
    if 'Cronograma_Atividades_E2i9_Totais' in _mail.subject:
        _attach = _mail.attachments_list[0]['payload']
        return parserTotais(_source, _attach)
    elif 'Cronograma_Atividades_E2i9' in _mail.subject:
        _attach = _mail.attachments_list[0]['payload']
        return parserCronograma(_source, _attach)
    else:
        return _source.replace('/new/', '/Others/not_parsed/')


if __name__ == '__main__':
    parserCronogramaFromFile(argv[1])

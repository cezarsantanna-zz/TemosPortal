# -*- coding: utf-8 -*-
import csv
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


def getpPostoID():
    pass
    return None


def getWarehouseID(_w_name):
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
                    'SELECT id FROM abastece_warehouse \
                     WHERE \
                     name = %s;',
                    (_w_name,)
                )
                _id = conn_pgs.fetchone()[0]
                return _id
    except:
        import sys
        import traceback
        print('Whoops! Problem:', file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None
    return None


def getBaseID(_b_name):
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
                    'SELECT id FROM abastece_base \
                     WHERE \
                     name = %s;',
                    (_b_name,)
                )
                _id = conn_pgs.fetchone()[0]
                return _id
    except:
        import sys
        import traceback
        print('Whoops! Problem:', file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None
    return None

def getEmployeeID(_e_name):
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
                    'SELECT id FROM abastece_employee \
                     WHERE \
                     name = %s;',
                    (_e_name,)
                )
                _id = conn_pgs.fetchone()[0]
                return _id
    except:
        import sys
        import traceback
        print('Whoops! Problem:', file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None
    return None


def getClaseeID(_c_name):
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
                    'SELECT id FROM abastece_classe \
                     WHERE \
                     name = %s;',
                    (_c_name,)
                )
                _id = conn_pgs.fetchone()[0]
                return _id
    except:
        import sys
        import traceback
        print('Whoops! Problem:', file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None
    return None

def importPostoCSV(_File):
    try:
        with open(_File, 'r') as srcfile:
            reader = csv.reader(srcfile, delimiter=';')
            try:
                with psycopg2.connect(
                    database=dbName,
                    user=dbUser,
                    host=dbHost,
                    password=dbPass
                ) as conn_pg:
                    for row in reader:
                        p_code = row[0]
                        p_name = row[1]
                        p_opc = row[2]
                        p_vip = row[3]
                        p_coordy = row[4]
                        p_coordx = row[5]
                        p_classe = getClaseeID(row[6])
                        p_base = getBaseID(row[7])
                        p_warehouse = getWarehouseID(row[8])
                        print(
                            p_code,
                            p_name,
                            p_classe,
                            p_warehouse,
                        )
                        try:
                            with conn_pg.cursor(
                            ) as conn_pgs:
                                conn_pgs.execute(
                                    'INSERT INTO abastece_posto \
                                    (active, name, cgmp, status_opc, \
                                     status_vip, coordx, coordy, base_id, \
                                     classe_id, warehouse_id) \
                                    VALUES \
                                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);',
                                    (True, p_name, p_code, p_opc, p_vip,
                                     p_coordx, p_coordy, p_base, p_classe,
                                     p_warehouse)
                                )
                                status = conn_pgs.statusmessage
                                print(status)
                        except:
                            import sys
                            import traceback
                            print(
                                p_code,
                                p_name,
                                p_classe,
                                p_warehouse,
                            )
                            print('Whoops! Problem:', file=sys.stderr)
                            traceback.print_exc(file=sys.stderr)
                            return None
            except:
                import sys
                import traceback
                print('Whoops! Problem:', file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return None

    except:
        import sys
        import traceback
        print('Whoops! Problem:', file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


def importWarehouseCSV(_File):
    try:
        with open(_File, 'r') as srcfile:
            reader = csv.reader(srcfile, delimiter=';')
            try:
                with psycopg2.connect(
                    database=dbName,
                    user=dbUser,
                    host=dbHost,
                    password=dbPass
                ) as conn_pg:
                    for row in reader:
                        w_name = row[0]
                        try:
                            with conn_pg.cursor(
                            ) as conn_pgs:
                                conn_pgs.execute(
                                    'INSERT INTO abastece_warehouse \
                                    (active, name) \
                                    VALUES \
                                    (%s, %s);',
                                    (True, w_name,)
                                )
                        except:
                            import sys
                            import traceback
                            print(
                                'Whoops! Problem: %s não pode ser inserido',
                                file=sys.stderr
                            ) % (w_name)
                            traceback.print_exc(file=sys.stderr)
                            return None
            except:
                import sys
                import traceback
                print('Whoops! Problem:', file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return None

    except:
        import sys
        import traceback
        print('Whoops! Problem:', file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


if __name__ == '__main__':
    if argv[1] == 'warehouse':
        importWarehouseCSV(argv[2])
    elif argv[1] == 'posto':
        importPostoCSV(argv[2])

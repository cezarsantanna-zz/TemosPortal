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


def getPostoID(_p_name):
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
                    'SELECT id FROM abastece_posto \
                     WHERE \
                     name = %s;',
                    (_p_name,)
                )
                _id = int(conn_pgs.fetchone()[0])
                return _id
    except TypeError:
        import sys
        import traceback
        print('Erro ao obter ID do Posto ', _p_name, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
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
                _id = int(conn_pgs.fetchone()[0])
                return _id
    except TypeError:
        import sys
        import traceback
        print('Erro ao obter ID do Warehouse ', _w_name, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
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
                _id = int(conn_pgs.fetchone()[0])
                return _id
    except TypeError:
        import sys
        import traceback
        print('Erro ao obter ID da Base ', _b_name, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
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
                _id = int(conn_pgs.fetchone()[0])
                return _id
    except TypeError:
        import sys
        import traceback
        print('Erro ao obter ID do Funcionário ', _e_name, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
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
    except TypeError:
        import sys
        import traceback
        print('Erro ao obter ID da Classe ', _c_name, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


def getFormID(_f_name):
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
                    'SELECT id FROM abastece_form \
                     WHERE \
                     name = %s;',
                    (_f_name,)
                )
                _id = conn_pgs.fetchone()[0]
                return _id
    except TypeError:
        import sys
        import traceback
        print('Erro ao obter ID do Formulário ', _f_name, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


def getBaseIDFromPostoID(_posto_id):
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
                    'SELECT base_id FROM abastece_posto \
                     WHERE \
                     id = %s;',
                    (_posto_id,)
                )
                _id = conn_pgs.fetchone()[0]
                return _id
    except TypeError:
        import sys
        import traceback
        print('Erro ao obter ID da Base via ', _posto_id, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


def getEmployeeIDFromBaseID(_base_id):
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
                    'SELECT employee_id FROM abastece_base \
                     WHERE \
                     id = %s;',
                    (_posto_id,)
                )
                _id = conn_pgs.fetchone()[0]
                return _id
    except TypeError:
        import sys
        import traceback
        print('Erro ao obter ID do Funcionário via ', _base_id, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


def parseEventNumber(_number):
    EventNumber = _number
    EventNumber = EventNumber.strip()
    EventNumber = EventNumber.replace("TASC", "TASK")
    EventNumber = EventNumber.replace("-", ";")
    EventNumber = EventNumber.replace("/", ";")
    EventNumber = EventNumber.replace(",", ";")
    EventNumber = EventNumber.replace(" ", ";")
    regex = re.compile('\;+')
    EventNumber = re.sub(regex, ';', EventNumber)
    if 'INC' in EventNumber:
        EventNumber = EventNumber.replace("INC;", "INC")
        EventNumber = EventNumber.replace("INC1", "INC01")
        EventNumber = EventNumber.replace(";0", ";INC0")
        EventNumber = EventNumber.replace(";1", ";INC01")
        return EventNumber
    elif 'TASK' in EventNumber:
        EventNumber = EventNumber.replace("TASK;", "TASK")
        EventNumber = EventNumber.replace("TASK1", "TASK01")
        EventNumber = EventNumber.replace(";0", ";TASK0")
        EventNumber = EventNumber.replace(";1", ";TASK01")
        return EventNumber
    else:
        if FormName == 'CORRETIVA':
            EventNumber = 'INC' + EventNumber
            EventNumber = EventNumber.replace(";", ";INC")
            EventNumber = EventNumber.replace("INC1", "INC01")
            return EventNumber
        else:
            EventNumber = 'TASK' + EventNumber
            EventNumber = EventNumber.replace(";", ";TASK")
            EventNumber = EventNumber.replace("TASK1", "TASK01")
            return EventNumber
    if EventNumber is None:
        EventNumber = 'Null'
        return EventNumber


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
                        except:
                            import sys
                            import traceback
                            print('Erro ao inserir posto no banco:',
                                  file=sys.stderr)
                            traceback.print_exc(file=sys.stderr)
                            return None
            except:
                import sys
                import traceback
                print('Erro ao conectar com o banco de dados', file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return None

    except:
        import sys
        import traceback
        print('Erro ao abrir arquivo CSV:', file=sys.stderr)
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
                                'Erro ao inserir %s',
                                file=sys.stderr
                            ) % (w_name)
                            traceback.print_exc(file=sys.stderr)
                            return None
            except:
                import sys
                import traceback
                print('Erro ao conectar com o banco de dados', file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return None

    except:
        import sys
        import traceback
        print('Erro ao abrir arquivo CSV:', file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


def importEventoCSV(_file):
    """
    Função para importar eventos planejados e/ou realizados via arquivo CSV
    o arquivo deve seguir o seguinte formato:
    Separador ou Delimitador ;
    Ordem dos campos:
        data_plan;date_real;cgmp;chamado;tipo;funcionário
        data_plan: Data para qual a atividade foi planejada
        data_real: Data na qual a atividade foi efetivamente realizada
        cgmp: Código de 4 digitos que indentificam o Posto na Sem Parar
        chamado: Número do chamado no Service Now (TASK ou INC)
        tipo: Tipo de eventos, estão descritos na tabela abastece_form
        funcionário: primeiro nome do técnico que atendeu o chamado, deve ser
            ao indicado no OfficeTrack
    """
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
                        e_data_planejado = row[0]
                        e_data_realizado = row[1]
                        e_posto = getPostoID(row[2])
                        e_number = parseEventNumber(row[3])
                        e_tipo = row[5]
                        e_employee = row[6]
                        if e_data_realizado is not None:
                            try:
                                with conn_pg.cursor(
                                ) as conn_pgs:
                                    conn_pgs.execute(
                                        'UPDATE abastece_evento \
                                         SET data_realizado = %s \
                                         WHERE \
                                         form_id = %s and \
                                         posto_id = %s and \
                                         number = %s;',
                                        (EntryDate,
                                         form_id,
                                         posto_id,
                                         EventNumber)
                                    )
                                    status=conn_pgs.statusmessage
                                    query=conn_pgs.query
                                    if status == 'UPDATE 0':
                                        conn_pgs.execute(
                                            'SELECT id FROM abastece_evento \
                                             WHERE form_id = %s and \
                                             posto_id = %s and \
                                             number = %s;',
                                            (form_id,
                                             posto_id,
                                             'Agendado')
                                        )
                                        event_id = conn_pgs.fetchone()

                                if event_id is not None:
                                    event_id = event_id[0]
                                    conn_pgs.execute(
                                        'UPDATE abastece_evento SET data_realizado = %s \
                                         WHERE \
                                         id = %s;',
                                        (EntryDate, event_id)
                                    )
                                    status = conn_pgs.statusmessage
                                    query = conn_pgs.query
                                    if status == 'UPDATE 0':
                                        conn_pgs.execute(
                                            'INSERT INTO abastece_evento \
                                            (active, entry_date, \
                                             data_planejado, \
                                             data_realizado, number, resumo, \
                                             posto_id, base_id, employee_id, \
                                             form_id, empresa_id) \
                                            VALUES \
                                            (%s, %s, %s, %s, %s, %s, %s, %s, \
                                             %s, %s, %s);',
                                            (True,
                                             entry_date,
                                             EntryDate,
                                             EntryDate,
                                             EventNumber,
                                             None,
                                             posto_id,
                                             base_id,
                                             employee_id,
                                             form_id,
                                             empresa_id)
                                        )
                                        status = conn_pgs.statusmessage
                                        if status == 'INSERT 0':
                                            return dest_err
                                        else:
                                            return dest_ok
                                    else:
                                        return dest_ok
                                else:
                                    conn_pgs.execute(
                                        'INSERT INTO abastece_evento \
                                        (active, entry_date, data_planejado, \
                                         data_realizado, number, resumo, posto_id, \
                                         base_id, employee_id, form_id, empresa_id) \
                                        VALUES \
                                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);',
                                        (True,
                                         entry_date,
                                         EntryDate,
                                         EntryDate,
                                         EventNumber,
                                         None,
                                         posto_id,
                                         base_id,
                                         employee_id,
                                         form_id,
                                         empresa_id)
                                    )
                                    status = conn_pgs.statusmessage
                                    if status == 'INSERT 0':
                                        return dest_err
                                    else:
                                        return dest_ok
                            else:
                                return dest_ok
                            except:
                                import sys
                                import traceback
                                print('Erro ao inserir posto no banco:', file=sys.stderr)
                                traceback.print_exc(file=sys.stderr)
                                return None
                        else:
                            try:
                                with conn_pg.cursor(
                                ) as conn_pgs:
                                    'UPDATE abastece_evento \
                                    SET data_realizado = %s \
                                 WHERE \
                                 form_id = %s and posto_id = %s and \
                                 number = %s;',
                                (EntryDate, form_id, posto_id, EventNumber)
                            )
                            status=conn_pgs.statusmessage
                            query=conn_pgs.query
                            if status == 'UPDATE 0':
                                conn_pgs.execute(
                                    'SELECT id FROM abastece_evento \
                                     WHERE form_id = %s and posto_id = %s and \
                                     number = %s;',
                                     (form_id, posto_id, 'Agendado')
                                )
                                event_id = conn_pgs.fetchone()

                                if event_id is not None:
                                    event_id = event_id[0]
                                    conn_pgs.execute(
                                        'UPDATE abastece_evento SET data_realizado = %s \
                                         WHERE \
                                         id = %s;',
                                        (EntryDate, event_id)
                                    )
                                    status = conn_pgs.statusmessage
                                    query = conn_pgs.query
                                    if status == 'UPDATE 0':
                                        conn_pgs.execute(
                                            'INSERT INTO abastece_evento \
                                            (active, entry_date, \
                                             data_planejado, \
                                             data_realizado, number, resumo, \
                                             posto_id, base_id, employee_id, \
                                             form_id, empresa_id) \
                                            VALUES \
                                            (%s, %s, %s, %s, %s, %s, %s, %s, \
                                             %s, %s, %s);',
                                            (True,
                                             entry_date,
                                             EntryDate,
                                             EntryDate,
                                             EventNumber,
                                             None,
                                             posto_id,
                                             base_id,
                                             employee_id,
                                             form_id,
                                             empresa_id)
                                        )
                                        status = conn_pgs.statusmessage
                                        if status == 'INSERT 0':
                                            return dest_err
                                        else:
                                            return dest_ok
                                    else:
                                        return dest_ok
                                else:
                                    conn_pgs.execute(
                                        'INSERT INTO abastece_evento \
                                        (active, entry_date, data_planejado, \
                                         data_realizado, number, resumo, posto_id, \
                                         base_id, employee_id, form_id, empresa_id) \
                                        VALUES \
                                        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);',
                                        (True,
                                         entry_date,
                                         EntryDate,
                                         EntryDate,
                                         EventNumber,
                                         None,
                                         posto_id,
                                         base_id,
                                         employee_id,
                                         form_id,
                                         empresa_id)
                                    )
                                    status = conn_pgs.statusmessage
                                    if status == 'INSERT 0':
                                        return dest_err
                                    else:
                                        return dest_ok
                            else:
                                return dest_ok
                            except:
                                import sys
                                import traceback
                                print('Erro ao inserir posto no banco:', file=sys.stderr)
                                traceback.print_exc(file=sys.stderr)
                                return None
            except:
                import sys
                import traceback
                print('Erro ao conectar com o banco de dados', file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
                return None

    except:
        import sys
        import traceback
        print('Erro ao abrir arquivo CSV:', file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


if __name__ == '__main__':
    if argv[1] == 'warehouse':
        importWarehouseCSV(argv[2])
    elif argv[1] == 'posto':
        importPostoCSV(argv[2])
    elif argv[1] == 'evento':
        importPostoCSV(argv[2])

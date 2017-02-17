# -*- coding: utf-8 -*-
import csv
import re
import psycopg2.extensions
from os import path
from sys import argv
from base64 import b64decode
from datetime import datetime
from datetime import date


"""
Variáveis para acesso ao Banco de Dados
"""
dbHost = "127.0.0.1"
dbName = "temosportal"
dbUser = "temos"
dbPass = "tw28()KP"


def getPostoIDFromName(_p_name):
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


def getPostoIDFromCode(_p_cgmp):
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
                     cgmp = %s;',
                    (_p_cgmp,)
                )
                _id = int(conn_pgs.fetchone()[0])
                return _id
    except TypeError:
        import sys
        import traceback
        print('Erro ao obter ID do Posto ', _p_cgmp, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


def getWarehouseIDFromName(_w_name):
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


def getBaseIDFromName(_b_name):
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


def getEmployeeIDFromName(_e_name):
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


def getClasseID(_c_name):
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


def getFormIDFromName(_f_name):
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
                    (_base_id,)
                )
                _id = conn_pgs.fetchone()[0]
                return _id
    except TypeError:
        import sys
        import traceback
        print('Erro ao obter ID do Funcionário via ', _base_id, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


def parseEventNumber(_number, _tipo):
    EventNumber = _number
    FormName = _tipo
    if EventNumber == 'Agendado':
        return EventNumber
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
                        p_classe = getClasseID(row[6])
                        p_base = getBaseIDFromName(row[7])
                        p_warehouse = getWarehouseIDFromName(row[8])
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


def importEventoCSV(_File):
    """
    Função para importar eventos planejados e/ou realizados via arquivo CSV
    o arquivo deve seguir o seguinte formato:
    Separador ou Delimitador ;
    Ordem dos campos:
        data_plan;date_real;cgmp;chamado;tipo;base
        data_plan: Data para qual a atividade foi planejada
        data_real: Data na qual a atividade foi efetivamente realizada
        cgmp: Código de 4 digitos que indentificam o Posto na Sem Parar
        chamado: Número do chamado no Service Now (TASK ou INC)
        tipo: Tipo de eventos, estão descritos na tabela abastece_form
        base: base do técnico que atendeu o chamado, deve ser igual ao indicado
            no OfficeTrack
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
                    linha=1
                    for row in reader:
                        e_data_planejado = row[0]
                        e_data_realizado = row[1]
                        e_posto = row[2]
                        e_number = row[3]
                        e_tipo = row[4]
                        e_base = row[5]

                        _posto_id = getPostoIDFromCode(e_posto)
                        _number = parseEventNumber(e_number, e_tipo)
                        _form_id = getFormIDFromName(e_tipo)
                        _base_id = getBaseIDFromName(e_base)
                        _employee_id = getEmployeeIDFromBaseID(_base_id)
                        if e_base == 'UNICOM':
                            _empresa_id = 2
                        else:
                            _empresa_id = 1

                        entry_date = date.today()

                        if e_data_realizado != '' and e_data_planejado == '0':
                            try:
                                with conn_pg.cursor() as conn_pgs:
                                    conn_pgs.execute(
                                        'UPDATE abastece_evento \
                                         SET data_realizado = %s \
                                         WHERE \
                                         form_id = %s and \
                                         posto_id = %s and \
                                         number = %s and \
                                         data_realizado is Null;',
                                        (e_data_realizado,
                                         _form_id,
                                         _posto_id,
                                         _number)
                                    )
                                    status=conn_pgs.statusmessage
                                    query=conn_pgs.query
                                    if status == 'UPDATE 0':
                                        conn_pgs.execute(
                                            'SELECT id FROM abastece_evento \
                                             WHERE form_id = %s and \
                                             posto_id = %s and \
                                             number = %s and \
                                             data_realizado is Null;',
                                            (_form_id,
                                             _posto_id,
                                             'Agendado')
                                        )
                                        event_id = conn_pgs.fetchone()
                                        if event_id is not None:
                                            event_id = event_id[0]
                                            conn_pgs.execute(
                                                'UPDATE abastece_evento SET \
                                                 data_realizado = %s \
                                                 WHERE \
                                                 id = %s;',
                                                (e_data_realizado,
                                                 event_id)
                                            )
                                            status = conn_pgs.statusmessage
                                            query = conn_pgs.query
                                            if status == 'UPDATE 0':
                                                print('Erro ao importar \
                                                           linha:', linha)
                                            else:
                                                print('Linha',linha,'importada')
                                        else:
                                            conn_pgs.execute(
                                                'INSERT INTO \
                                                 abastece_evento \
                                                 (active, entry_date, \
                                                 data_planejado, \
                                                 data_realizado, number, \
                                                 resumo, posto_id, base_id,\
                                                 employee_id, \
                                                 form_id, empresa_id) \
                                                VALUES \
                                                (%s, %s, %s, \
                                                 %s, %s, %s, \
                                                 %s, %s, %s, %s, %s);',
                                                (True,
                                                 entry_date,
                                                 None,
                                                 e_data_realizado,
                                                 _number,
                                                 None,
                                                 _posto_id,
                                                 _base_id,
                                                 _employee_id,
                                                 _form_id,
                                                 _empresa_id)
                                            )
                                            status = conn_pgs.statusmessage
                                            query = conn_pgs.query
                                            if status == 'INSERT 0':
                                                print('Erro ao importar linha',
                                                      linha)
                                            else:
                                                print('Linha',linha,'importada')
                                    else:
                                        print('Linha',linha,'importada')
                            except:
                                import sys
                                import traceback
                                print('Erro ao inserir posto no banco:',
                                      file=sys.stderr)
                                traceback.print_exc(file=sys.stderr)
                                return None
                        else:
                            e_data_realizado = None
                            try:
                                with conn_pg.cursor() as conn_pgs:
                                    conn_pgs.execute(
                                        'UPDATE abastece_evento \
                                         SET data_planejado = %s \
                                         WHERE \
                                         form_id = %s and \
                                         posto_id = %s and \
                                         number = %s and \
                                         data_planejado is Null;',
                                        (e_data_planejado,
                                         _form_id,
                                         _posto_id,
                                         _number)
                                    )
                                    status=conn_pgs.statusmessage
                                    query=conn_pgs.query
                                    if status == 'UPDATE 0':
                                        conn_pgs.execute(
                                            'SELECT id FROM abastece_evento \
                                             WHERE form_id = %s and \
                                             posto_id = %s and \
                                             number = %s and \
                                             data_planejado is Null;',
                                            (_form_id,
                                             _posto_id,
                                             'Agendado')
                                        )
                                        event_id = conn_pgs.fetchone()
                                        if event_id is not None:
                                            event_id = event_id[0]
                                            conn_pgs.execute(
                                                'UPDATE abastece_evento SET \
                                                 data_planejado = %s \
                                                 WHERE \
                                                 id = %s;',
                                                (e_data_planejado,
                                                 event_id)
                                            )
                                            status = conn_pgs.statusmessage
                                            query = conn_pgs.query
                                            if status == 'UPDATE 0':
                                                print('Erro ao importar \
                                                          linha', linha)
                                            else:
                                                print('Linha',linha,'importada')
                                        else:
                                            conn_pgs.execute(
                                                'INSERT INTO \
                                                 abastece_evento \
                                                 (active, entry_date, \
                                                 data_planejado, \
                                                 data_realizado, number, \
                                                 resumo, posto_id, base_id,\
                                                 employee_id, \
                                                 form_id, empresa_id) \
                                                VALUES \
                                                (%s, %s, %s, \
                                                 %s, %s, %s, \
                                                 %s, %s, %s, %s, %s);',
                                                (True,
                                                 entry_date,
                                                 e_data_planejado,
                                                 e_data_realizado,
                                                 _number,
                                                 None,
                                                 _posto_id,
                                                 _base_id,
                                                 _employee_id,
                                                 _form_id,
                                                 _empresa_id)
                                            )
                                            status = conn_pgs.statusmessage
                                            query = conn_pgs.query
                                            if status == 'INSERT 0':
                                                print('Erro ao importar \
                                                      linha', linha)
                                            else:
                                                print('Linha',linha,'importada')
                                    else:
                                        print('Linha',linha,'importada')
                            except:
                                import sys
                                import traceback
                                print('Erro ao inserir posto no banco:', file=sys.stderr)
                                traceback.print_exc(file=sys.stderr)
                                return None
                        linha = linha + 1
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


def importLinhaBaseCSV(_File):
    """
    Função para importar linha de base via arquivo CSV
    o arquivo deve seguir o seguinte formato:
    Separador ou Delimitador ;
    Ordem dos campos:
        cgmp;data_planejado;tipo;chamado
        cgmp: Código de 4 digitos que indentificam o Posto na Sem Parar
        data_plan: Data para qual a atividade foi planejada
        tipo: Tipo de eventos, estão descritos na tabela abastece_form
        chamado: Número do chamado no Service Now (TASK ou INC) ou Agendado
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
                    linha=1
                    for row in reader:
                        e_posto = row[0]
                        e_data_planejado = row[1]
                        e_data_realizado = None
                        e_tipo = row[2]
                        e_number = row[3]
                        e_emp = 'E2i9'

                        _posto_id = getPostoIDFromCode(e_posto)
                        _number = parseEventNumber(e_number, e_tipo)
                        _form_id = getFormIDFromName(e_tipo)
                        _base_id = getBaseIDFromPostoID(_posto_id)
                        _employee_id = getEmployeeIDFromBaseID(_base_id)

                        if e_emp == 'UNICOM':
                            _empresa_id = 2
                        elif e_emp == 'E2i9':
                            _empresa_id = 1

                        entry_date = date.today()
                        e_data_realizado = None
                        try:
                            with conn_pg.cursor() as conn_pgs:
                                conn_pgs.execute(
                                    'INSERT INTO \
                                     abastece_evento \
                                     (active, entry_date, \
                                     data_planejado, \
                                     data_realizado, number, \
                                     resumo, posto_id, base_id,\
                                     employee_id, \
                                     form_id, empresa_id) \
                                    VALUES \
                                    (%s, %s, %s, \
                                     %s, %s, %s, \
                                     %s, %s, %s, %s, %s);',
                                    (True,
                                     entry_date,
                                     e_data_planejado,
                                     e_data_realizado,
                                     _number,
                                     None,
                                     _posto_id,
                                     _base_id,
                                     _employee_id,
                                     _form_id,
                                     _empresa_id)
                                )
                                status = conn_pgs.statusmessage
                                query = conn_pgs.query
                                if status == 'INSERT 0':
                                    print('Erro ao importar \
                                          linha', linha)
                                else:
                                    print('Linha',linha,'importada')
                        except:
                            import sys
                            import traceback
                            print('Erro ao inserir posto no banco:', file=sys.stderr)
                            traceback.print_exc(file=sys.stderr)
                            return None
                        linha = linha + 1
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


def importCorretivasCSV(_File):
    """
    Função para importar média de corretivas por dia via arquivo CSV
    o arquivo deve seguir o seguinte formato:
    Separador ou Delimitador ;
    Ordem dos campos:
        data_planejado;numero de eventos no dia
        data_plan: Data para qual a atividade foi planejada
        número de eventos no dia: Média de eventos esperados para o dia
        informado em data_planejado
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
                    linha=1
                    for row in reader:
                        e_data_planejado = row[0]
                        e_n_eventos = int(row[1])
                        e_data_realizado = None
                        e_tipo = 'CORRETIVA'
                        e_number = None
                        e_emp = 'E2i9'

                        _posto_id = None
                        _number = 'Agendado'
                        _form_id = getFormIDFromName(e_tipo)
                        _base_id = None
                        _employee_id = None

                        if e_emp == 'UNICOM':
                            _empresa_id = 2
                        elif e_emp == 'E2i9':
                            _empresa_id = 1

                        entry_date = date.today()
                        try:
                            for i in range(e_n_eventos):
                                with conn_pg.cursor() as conn_pgs:
                                    conn_pgs.execute(
                                        'INSERT INTO \
                                         abastece_evento \
                                         (active, entry_date, \
                                         data_planejado, \
                                         data_realizado, number, \
                                         resumo, posto_id, base_id,\
                                         employee_id, \
                                         form_id, empresa_id) \
                                        VALUES \
                                        (%s, %s, %s, \
                                         %s, %s, %s, \
                                         %s, %s, %s, %s, %s);',
                                        (True,
                                         entry_date,
                                         e_data_planejado,
                                         e_data_realizado,
                                         _number,
                                         None,
                                         _posto_id,
                                         _base_id,
                                         _employee_id,
                                         _form_id,
                                         _empresa_id)
                                    )
                                    status = conn_pgs.statusmessage
                                    query = conn_pgs.query
                                    if status == 'INSERT 0':
                                        print('Erro ao importar \
                                              linha', linha)
                                    else:
                                        print('Linha',linha,'importada')
                        except:
                            import sys
                            import traceback
                            print('Erro ao inserir posto no banco:', file=sys.stderr)
                            traceback.print_exc(file=sys.stderr)
                            return None
                        linha = linha + 1
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


def importFormCSV(_File):
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
                        form_name = row[0]
                        try:
                            with conn_pg.cursor(
                            ) as conn_pgs:
                                conn_pgs.execute(
                                    'INSERT INTO abastece_form \
                                    (active, name) \
                                    VALUES \
                                    (%s, %s);',
                                    (True, form_name,)
                                )
                        except:
                            import sys
                            import traceback
                            print(
                                'Erro ao inserir %s',
                                file=sys.stderr
                            ) % (form_name)
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
        importEventoCSV(argv[2])
    elif argv[1] == 'linhabase':
        importLinhaBaseCSV(argv[2])
    elif argv[1] == 'corretivas':
        importCorretivasCSV(argv[2])
    elif argv[1] == 'form':
        importFormCSV(argv[2])

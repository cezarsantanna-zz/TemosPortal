# -*- coding: utf-8 -*-
import re
import psycopg2.extensions
from base64 import b64decode
from datetime import datetime
from lxml import etree


"""
Variáveis para acesso ao Banco de Dados
"""
dbHost = "127.0.0.1"
dbName = "temosportal"
dbUser = "temos"
dbPass = "tw28()KP"


def getFormID(_FormName):
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
                    "SELECT id FROM abastece_form \
                     WHERE active = True and name = (%s);",
                    (_FormName,)
                )
                _id = int(conn_pgs.fetchone()[0])
                return _id
    except TypeError:
        import sys
        import traceback
        print('Erro ao obter ID do Formulário ', _FormName, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


def getPostoID(_CGMP):
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



def getBaseIDFromEmployeeID(_Employee_id):
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
                    "SELECT id FROM abastece_base \
                     WHERE active = True and employee_id = (%s);",
                    (_Employee_id,)
                )
                _id = int(conn_pgs.fetchone()[0])
                return _id
    except TypeError:
        import sys
        import traceback
        print('Erro ao obter ID da Base via ', _Employee_id, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


def getEmployeeID(_EmployeeFirstName):
    try:
        if _EmployeeFirstName is None:
            raise ValueNone('Nome do Funcionário não pode ser vazio')
    except ValueNone:
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
                    "SELECT id FROM abastece_employee \
                     WHERE active = True and name = (%s);",
                    (_EmployeeFirstName,)
                )
                _id = int(conn_pgs.fetchone()[0])
                return _id
    except TypeError:
        import sys
        import traceback
        print('Erro ao obter ID do Funcionário ', _EmployeeFirstName, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


def getEquipID(_equipamento):
    try:
        with psycopg2.connect(
            database=dbName,
            user=dbUser,
            host=dbHost, password=dbPass
        ) as conn_pg:
            with conn_pg.cursor() as conn_pgs:
                conn_pgs.execute(
                    "SELECT id from abastece_item \
                    WHERE active = True and name = (%s);",
                    (_equipamento,)
                )
                _id = int(conn_pgs.fetchone()[0])
                return _id
    except TypeError:
        import sys
        import traceback
        print('Erro ao obter ID do Equipamento ', _equipamento, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return None


"""
Campos comuns em todos os XMLs do OfficeTrack
"""
def getEventType(_xml):
    _EventType = _xml.find('EventType')
    if _EventType is not None:
        return _EventType.text
    else:
        return None


def getEntryType(_xml):
    _EntryType = _xml.find('EntryType')
    if _EntryType is not None:
        return _EntryType.text
    else:
        return None


def getEntryDateFromEpoch(_xml):
    _EntryDateFromEpoch = _xml.find('EntryDateFromEpoch')
    if _EntryDateFromEpoch is not None:
        return int(_EntryDateFromEpoch.text[0:10])
    else:
        return None


def getEmployeeFirstName(_xml):
    _EmployeeFirstName = _xml.find('Employee/FirstName')
    if _EmployeeFirstName is not None:
        if 'SP01' in EmployeeFirstName:
            EmployeeFirstName = 'Wesley'
        elif 'SP02' in EmployeeFirstName:
            EmployeeFirstName = 'Alex'
        elif 'SP03' in EmployeeFirstName:
            EmployeeFirstName = 'Ítalo'
        elif 'SP04' in EmployeeFirstName:
            EmployeeFirstName = 'Renan'
        elif 'SP05' in EmployeeFirstName:
            EmployeeFirstName = 'Matheus'
        elif 'SP06' in EmployeeFirstName:
            EmployeeFirstName = 'Diego'
        elif 'SP07' in EmployeeFirstName:
            EmployeeFirstName = 'Rafhael'
        elif 'SOR01' in EmployeeFirstName:
            EmployeeFirstName = 'Wellington'
        elif 'SOR02' in EmployeeFirstName:
            EmployeeFirstName = 'Raphael'
        elif 'PR01' in EmployeeFirstName:
            EmployeeFirstName = 'Adélio'
        elif 'RJ01' in EmployeeFirstName:
            EmployeeFirstName = 'Vitor'
        elif 'RJ02' in EmployeeFirstName:
            EmployeeFirstName = 'Vitor'
        return _EmployeeFirstName.text
    else:
        return None


def getEntryLocationX(_xml):
    _EntryLocationX = _xml.find('EntryLocation/X')
    if _EntryLocationX is not None:
        return _EntryLocationX.text
    else:
        return None


def getEntryLocationY(_xml):
    _EntryLocationY = _xml.find('EntryLocation/Y')
    if _EntryLocationY is not None:
        return _EntryLocationY.text
    else:
        return None


"""
Campos comuns aos XMLs de Tasks
EntryTypes 21, 22, 23, 24, 25, 26 e 29
"""
def getTaskTaskNumber(_xml):
    _TaskTaskNumber = _xml.find('Task/TaskNumber')
    if _TaskTaskNumber is not None:
        return _TaskTaskNumber.text
    else:
        return None


def getTaskStatus(_xml):
    _TaskStatus = _xml.find('Task/Status')
    if _TaskStatus is not None:
        return _TaskStatus.text
    else:
        return None


def getTaskDescription(_xml):
    _TaskDescription = _xml.find('Task/Description')
    if _TaskDescription is not None:
        return _TaskDescription.text
    else:
        return None


def getTaskTaskTypeCode(_xml):
    _TaskTaskTypeCode = _xml.find('Task/TaskType/Code')
    if _TaskTaskTypeCode is not None:
        return _TaskTaskTypeCode.text
    else:
        return None


def getTaskTaskTypeName(_xml):
    _TaskTaskTypeName = _xml.find('Task/TaskType/Name')
    if _TaskTaskTypeName is not None:
        return _TaskTaskTypeName.text
    else:
        return None


def getTaskCustomerCustomerNumber(_xml):
    _TaskCustomerCustomerNumber = _xml.find('Task/Customer/CustomerNumber')
    if _TaskCustomerCustomerNumber is not None:
        return _TaskCustomerCustomerNumber.text
    else:
        return None


def getTaskCustomerName(_xml):
    _TaskCustomerName = _xml.find('Task/Customer/Name')
    if _TaskCustomerName is not None:
        return _TaskCustomerName.text
    else:
        return None


"""
Campos comuns aos XMLs de Formulários
EntryType 60
"""
def getFormName(_xml):
    _FormName = _xml.find('Form/Name')
    if _FormName is not None:
        return _FormName.text
    else:
        return None


def getEventNumber(_xml):
    FormName = getFormName(_xml)
    for _element in _xml.iter("Field"):
        if (_element[0].text == 'NÚMERO DE CHAMADO' or
            _element[0].text == 'NÚMERO DO CHAMADO'):
           EventNumber = _element[1].text.upper()
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
           elif 'TASK' in EventNumber:
               EventNumber = EventNumber.replace("TASK;", "TASK")
               EventNumber = EventNumber.replace("TASK1", "TASK01")
               EventNumber = EventNumber.replace(";0", ";TASK0")
               EventNumber = EventNumber.replace(";1", ";TASK01")
           else:
               if FormName == 'CORRETIVA':
                   EventNumber = 'INC' + EventNumber
                   EventNumber = EventNumber.replace(";", ";INC")
                   EventNumber = EventNumber.replace("INC1", "INC01")
               else:
                   EventNumber = 'TASK' + EventNumber
                   EventNumber = EventNumber.replace(";", ";TASK")
                   EventNumber = EventNumber.replace("TASK1", "TASK01")
           if EventNumber is None:
               EventNumber = 'Null'
           return EventNumber
    return 'Null'


def getRefPOICustomerNumber(_xml):
    _RefPOICustomerNumber = _xml.find(
        'ReferencedPointsOfInterest/PointOfInterest/CustomerNumber')
    if _RefPOICustomerNumber is not None:
        return _RefPOICustomerNumber.text[-4:]
    else:
        return None


def getRefPOIName(_xml):
    _RefPOIName = _xml.find(
        'ReferencedPointsOfInterest/PointOfInterest/Name')
    if _RefPOIName is not None:
        return _RefPOIName.text
    else:
        return None


def getEquipREM(_xml):
    FormName = getFormName(_xml)
    if (getEntryType(_xml) == '60' and
        (FormName == 'CORRETIVA' or
         FormName == 'PREDITIVA' or
         FormName == 'AÇÕES DE MELHORIA')):
        for element in _xml.iter("Field"):
            if (element[0].text == 'PERIFÉRICOS REMOVIDOS' or
                    element[0].text == 'PERIFÉRICOS RETIRADOS'):
                _rows = element[1]
                rows = []
                for _row in _rows.iter("Row"):
                    equipamento = 'Nenhum'
                    local = 'Nenhum'
                    serial = 'N/A'
                    patri = 'N/A'
                    for column in _row.iter("Field"):
                        if (column[0].text == 'Item Removido' or
                                column[0].text == 'Item Retirado'):
                            equipamento = column[1].text
                        elif column[0].text == 'Local onde estava instalado':
                            local = column[1].text
                        elif column[0].text == 'Número Serial':
                            serial = column[1].text
                        elif column[0].text == 'Número Patrimônio':
                            patri = column[1].text
                    row = {
                        'Equipamento': equipamento,
                        'Local': local,
                        'Serial': serial,
                        'Patrimônio': patri,
                    }
                    if equipamento != 'Nenhum':
                        rows.append(row)
                if len(rows) <= 0:
                    return None
                elif len(rows) > 0:
                    return rows
    return None


def getEquipADD(_xml):
    FormName = getFormName(_xml)
    if (getEntryType(_xml) == '60' and
        (FormName == 'CORRETIVA' or
         FormName == 'PREDITIVA' or
         FormName == 'AÇÕES DE MELHORIA')):
        for element in _xml.iter("Field"):
            if element[0].text == 'PERIFÉRICOS ADICIONADOS':
                _rows = element[1]
                rows = []
                for _row in _rows.iter("Row"):
                    equipamento = 'Nenhum'
                    local = 'Nenhum'
                    serial = 'N/A'
                    patri = 'N/A'
                    for column in _row.iter("Field"):
                        if column[0].text == 'Item Adicionado':
                            equipamento = column[1].text
                        elif column[0].text == 'Local onde foi instalado':
                            local = column[1].text
                        elif column[0].text == 'Número Serial':
                            serial = column[1].text
                        elif column[0].text == 'Número Patrimônio':
                            patri = column[1].text
                    row = {
                        'Equipamento': equipamento,
                        'Local': local,
                        'Serial': serial,
                        'Patrimônio': patri,
                    }
                    if equipamento != 'Nenhum':
                        rows.append(row)
                if len(rows) <= 0:
                    return None
                elif len(rows) > 0:
                    return rows
    return None


"""
Função exclusiva para PunchIn e PunchOut
"""
def setPunch(_xml, _source):
    EntryType = getEntryType(_xml)
    EntryDateFromEpoch = getEntryDateFromEpoch(_xml)
    EntryLocationX = getEntryLocationX(_xml)
    EntryLocationY = getEntryLocationY(_xml)
    EmployeeFirstName = getEmployeeFirstName(_xml)
    EmployeeFirstName = getEmployeeFirstName(_xml)
    _employee_id = getEmployeeID(EmployeeFirstName)
    entry_date = datetime.fromtimestamp(
        EntryDateFromEpoch).strftime(
        '%Y-%m-%d')
    if EntryType == '21':
        tipo = 'Entrada'
        dest_ok = _source.replace(
            '/new/',
            '/OfficeTrack/RH/PunchIn/parsed/'
        )
        dest_err = _source.replace(
            '/new/',
            '/OfficeTrack/RH/PunchIn/not_parsed/'
        )
        try:
            with psycopg2.connect(
                database=dbName,
                user=dbUser,
                host=dbHost,
                password=dbPass
            ) as conn_pg:
                with conn_pg.cursor() as conn_pgs:
                    conn_pgs.execute(
                        'INSERT INTO abastece_punch \
                        (active, in_time, out_time, entry_date, in_coordx, \
                         in_coordy, out_coordx, out_coordy, employee_id) \
                        VALUES \
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s);',
                        (True, EntryDateFromEpoch, None, entry_date,
                         EntryLocationX, EntryLocationY,
                         None, None, _employee_id,)
                    )
                    status = conn_pgs.statusmessage
                    if status == 'INSERT 0':
                        return dest_err
                    else:
                        return dest_ok
        except:
            import sys
            import traceback
            print('Whoops! Problem:', file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            return dest_err

    elif EntryType == '22':
        tipo = 'Saída'
        dest_ok = _source.replace(
            '/new/',
            '/OfficeTrack/RH/PunchOut/parsed/'
        )
        dest_err = _source.replace(
            '/new/',
            '/OfficeTrack/RH/PunchOut/not_parsed/'
        )
        try:
            with psycopg2.connect(
                database=dbName,
                user=dbUser,
                host=dbHost,
                password=dbPass
            ) as conn_pg:
                with conn_pg.cursor() as conn_pgs:
                    conn_pgs.execute(
                        'UPDATE abastece_punch SET out_time = %s, \
                         out_coordx = %s, out_coordy = %s \
                         WHERE \
                         entry_date = %s and employee_id = %s and \
                         in_time < %s and out_time is %s;',
                        (EntryDateFromEpoch, EntryLocationX, EntryLocationY,
                         entry_date, _employee_id, EntryDateFromEpoch, None,)
                    )
                    status = conn_pgs.statusmessage
                    query = conn_pgs.query
                    if status == 'UPDATE 0':
                        with conn_pg.cursor() as conn_pgs:
                            conn_pgs.execute(
                                'INSERT INTO abastece_punch \
                                (active, in_time, out_time, entry_date, \
                                 in_coordx, in_coordy, out_coordx, out_coordy, \
                                 employee_id) \
                                VALUES \
                                (%s, %s, %s, %s, %s, %s, %s, %s, %s);',
                                (True, None, EntryDateFromEpoch, entry_date,
                                 None, None, EntryLocationX, EntryLocationY,
                                 _employee_id,)
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
            print('Whoops! Problem:', file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            return dest_err


"""
Função exclusiva para Tasks Start, Close and Not Done
"""
def setTask(_xml, _source):
    # print(getEntryType(_xml))
    # print(getEntryDateFromEpoch(_xml))
    # print(getEntryLocationX(_xml))
    # print(getEntryLocationY(_xml))
    # print(getEmployeeFirstName(_xml))
    # print(getTaskTaskNumber(_xml))
    # print(getTaskDescription(_xml))
    # print(getTaskTaskTypeCode(_xml))
    # print(getTaskTaskTypeName(_xml))
    # print(getTaskCustomerCustomerNumber(_xml))
    # print(getTaskCustomerName(_xml))
    if getEntryType(_xml) == '23':
        return _source.replace('/new/', '/OfficeTrack/Task/Start/not_parsed/')
    elif getEntryType(_xml) == '26':
        return _source.replace('/new/', '/OfficeTrack/Task/Close/not_parsed/')
    elif getEntryType(_xml) == '29':
        return _source.replace('/new/', '/OfficeTrack/Task/NotDone/not_parsed/')


"""
Função exclusiva para Forms de Atendimento
"""
def setForm(_xml, _source):
    EntryType = getEntryType(_xml)
    EntryDate = getEntryDateFromEpoch(_xml)
    entry_date = datetime.fromtimestamp(
        EntryDate).strftime(
        '%Y-%m-%d')
    EmployeeFirstName = getEmployeeFirstName(_xml)
    FormName = getFormName(_xml)
    EventNumber = getEventNumber(_xml)
    if ';' in EventNumber:
        EventNumber = EventNumber.split(';')
        EventNumber = EventNumber[0]
    POIName = getRefPOIName(_xml)
    POICGMP = getRefPOICustomerNumber(_xml)
    EquipREM = getEquipREM(_xml)
    EquipADD = getEquipADD(_xml)

    posto_id = getPostoID(POICGMP)
    employee_id = getEmployeeID(EmployeeFirstName)
    base_id = getBaseIDFromEmployeeID(employee_id)
    form_id = getFormID(FormName)

    if EmployeeFirstName == 'UNICOM':
        empresa_id = 2
    else:
        empresa_id = 1
    dest_ok = _source.replace(
        '/new/',
        '/OfficeTrack/Reports/parsed/'
    )
    dest_err = _source.replace(
        '/new/',
        '/OfficeTrack/Reports/not_parsed/'
    )

    try:
        with psycopg2.connect(
            database=dbName,
            user=dbUser,
            host=dbHost,
            password=dbPass
        ) as conn_pg:
            with conn_pg.cursor() as conn_pgs:
                conn_pgs.execute(
                    'UPDATE abastece_evento SET data_realizado = %s \
                     WHERE \
                     form_id = %s and posto_id = %s and \
                     number = %s;',
                    (EntryDate, form_id, posto_id, EventNumber)
                )
                status = conn_pgs.statusmessage
                query = conn_pgs.query
                if status == 'UPDATE 0':
                    conn_pgs.execute(
                        'SELECT id FROM abastece_evento \
                         WHERE form_id = %s and posto_id = %s and \
                         number = %s;',
                         (form_id, posto_id, 'Agendado')
                    )
                    event_id = conn_pgs.fetchone()

                    if event_id is None:
                        pass
                    else:
                        event_id = event_id[0]

                    if event_id:
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
                    else:
                        # print(entry_date)
                        # print(EntryDate)
                        # print(EventNumber)
                        # print(posto_id)
                        # print(base_id)
                        # print(employee_id)
                        # print(form_id)
                        # print(empresa_id)
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
        print('Whoops! Problem:', file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return dest_err


def setInvent(_xml, _source):
    EntryDate = getEntryDateFromEpoch(_xml)
    EmployeeFirstName = getEmployeeFirstName(_xml)
    employee_id = getEmployeeID(EmployeeFirstName)
    for element in _xml.iter("Field"):
        if element[0].text:
            categoria = element[0].text
            _rows = []
            rows = element[1]
            for row in rows.iter("Row"):
                equipamento = row[0].text
                for column in row.iter("Field"):
                    novo = categoria + '01'
                    usado = categoria + '02'
                    defeito = categoria + '03'
                    if column[0].text == novo:
                        if column[1].text is None:
                            q_novo = 0
                        else:
                            q_novo = float(column[1].text)
                    elif column[0].text == usado:
                        if column[1].text is None:
                            q_usado = 0
                        else:
                            q_usado = float(column[1].text)
                    elif column[0].text == defeito:
                        if column[1].text is None:
                            q_defeito = 0
                        else:
                            q_defeito = float(column[1].text)
                updateInventario(EntryDate, employee_id, equipamento, q_novo,
                    q_usado, q_defeito, _source)
    return _source.replace('/new/', '/OfficeTrack/Inventories/not_parsed/')


def updateInventario(_EntryDate, _Wharehouse_id, _Equipamento,
    _q_novo, _q_usado, _q_defeito, _source):
    dest_ok = _source.replace(
        '/new/',
        '/OfficeTrack/Inventories/parsed/'
    )
    dest_err = _source.replace(
        '/new/',
        '/OfficeTrack/Inventories/not_parsed/'
    )


def parserOfficeTrack(_source, _mail):
    attach = b64decode(_mail.attachments_list[0]['payload'])
    xml = etree.fromstring(attach)
    if (getEmployeeFirstName(xml) == 'Eduardo' or
        getEmployeeFirstName(xml) == 'Cezar' or
            getEmployeeFirstName(xml) == 'Engenharia E2i9 TESTE API'):
        return _source.replace('/new/', '/trash/')
        pass
    else:
        if getEntryType(xml) == '21':
            return setPunch(xml, _source)

        elif getEntryType(xml) == '22':
            return setPunch(xml, _source)

        elif getEntryType(xml) == '23':
            return setTask(xml, _source)

        elif getEntryType(xml) == '26':
            return setTask(xml, _source)

        elif getEntryType(xml) == '29':
            return setTask(xml, _source)

        elif getEntryType(xml) == '60':
            FormName = getFormName(xml)
            if (FormName == 'INVENTÁRIO' or
                    FormName == 'INVENTARIO'):
                return setInvent(xml, _source)
            elif (FormName == 'AÇÕES DE MELHORIAS' or
                  FormName == 'ANTENA 915' or
                  FormName == 'CORRETIVA' or
                  FormName == 'DESINSTALAÇÃO DO POSTO' or
                  FormName == 'PLANO VERÃO' or
                  FormName == 'PREDITIVA' or
                  FormName == 'PREVENTIVA' or
                  FormName == 'RETIRADA ANTENA 5.8' or
                  FormName == 'SINALIZAÇÃO'):
                return setForm(xml, _source)
            else:
                return _source.replace('/new/',
                                       '/OfficeTrack/Others/not_parsed/')
        else:
            return _source.replace('/new/', '/OfficeTrack/Others/not_parsed/')

#!/home/cezar.santanna/.virtualenvs/abastece/bin/python
# -*- coding: utf-8 -*-
import psycopg2.extensions
from io import StringIO
from datetime import datetime
from lxml import html
from html2text import HTML2Text


"""
Variáveis para acesso ao Banco de Dados
"""
dbHost = "127.0.0.1"
dbName = "temosportal"
dbUser = "temos"
dbPass = "tw28()KP"


def parserINC(_email):
    if ('has been assigned to group Manutenção - Active' in
        _email['subject'] or
        'foi designado ao grupo Manutenção - E2i9' in
        _email['subject']):
        try:
            with psycopg2.connect(
                database=dbName,
                user=dbUser,
                host=dbHost,
                password=dbPass
            ) as conn_pg:
                with conn_pg.cursor() as conn_pgs:
                    conn_pgs.execute(
                        'INSERT INTO abastece_task \
                        (active, encerrado, numero, data_atribuido, \
                         data_fechado, posto_id, description) \
                        VALUES \
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s);',
                        (True, _Encerrado, _Chamado, _Atribuido,
                         _Fechado, _posto_id, _description,
                         None, None, _employee_id)
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

        return _source.replace('/new/', '/ServiceNow/Incidents/parsed/')
    elif ('has been assigned to you' in _email['subject'] or
          'foi assinalado à você' in _email['subject']):
        return _source.replace('/new/', '/ServiceNow/Incidents/parsed/')
    elif ('comments added' in _email['subject'] or
          'Comentários adicionados ao incidente' in _email['subject']):
        return _source.replace('/new/', '/ServiceNow/Incidents/parsed/')
    else:
        return _source.replace('/new/', '/ServiceNow/Incidents/not_parsed/')


def parserREQ(_email):
    # print u'Requisição-----------------------------------------------'
    # print _email['body']
    pass


def parserTASK(_email):
    # print u'Tarefa---------------------------------------------------'
    # if _email['html']:
        # h = HTML2Text()
        # h.ignore_links = True
        # html = StringIO(h.handle(_email['html']))
        # i = 0
        # for line in html:
            # print 'Linha [%s]: %s' % (i, line)
            # i = i + 1
    pass


def parserServiceNow(_source, _mail):
    if 'INC' in _mail.subject:
        return parserINC(_source, _mail)
    elif 'TASK' in _mail.subject:
        return parserTASK(_source, _mail)
    elif 'REQ' in _mail.subject:
        return parserREQ(_source, _mail)
    else:
        return _source.replace('/new/', '/ServiceNow/Others/not_parsed/')

#!/home/cezar.santanna/.virtualenvs/abastece/bin/python
# -*- coding: utf-8 -*-
from io import StringIO
from datetime import datetime
from lxml import html
from html2text import HTML2Text


def parserServiceNow(_email):
    if 'INC' in _email['subject']:
        parserINC(_email)
    if 'TASK' in _email['subject']:
        parserTASK(_email)
    if 'REQ' in _email['subject']:
        parserREQ(_email)


def parserINC(_email):
    if ('has been assigned to group Manutenção - Active' in
        _email['subject'] or
        'foi designado ao grupo Manutenção - E2i9' in
        _email['subject']):
        # print 'Incidente aberto--------------------------------------'
        # if _email['html']:
        #    tree = html.fromstring(_email['html'])
        #    mail = StringIO(tree.text_content())
        #    i = 1
        #    for line in mail:
        #        print 'Linha [%s]: %s' % (i, line)
        #        i = i + 1
        pass
    elif ('has been assigned to you' in _email['subject'] or
          'foi assinalado à você' in _email['subject']):
        # print 'Incidente fechado-------------------------------------'
        # if _email['html']:
        #    tree = html.fromstring(_email['html'])
        #    mail = StringIO(tree.text_content())
        #    i = 1
        #    for line in mail:
        #        print 'Linha [%s]: %s' % (i, line)
        #        i = i + 1
        pass
    elif ('comments added' in _email['subject'] or
          'Comentários adicionados ao incidente' in _email['subject']):
        # print 'Incidente follow-up-----------------------------------'
        # if _email['html']:
        #    tree = html.fromstring(_email['html'])
        #    mail = StringIO(tree.text_content())
        #    i = 1
        #    for line in mail:
        #        print 'Linha [%s]: %s' % (i, line)
        #        i = i + 1
        pass
    else:
        # print 'Incidente Não Classificado----------------------------'
        # print u'Não classificado'
        # print _email['subject']
        pass
    pass


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

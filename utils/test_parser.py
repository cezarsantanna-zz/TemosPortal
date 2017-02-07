#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
from base64 import b64decode
from lxml import etree
from datetime import datetime
from utils.parser.mailparser import MailParser

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


def main(_mailfile):
    mail = MailParser()
    mail.parse_from_file(_mailfile)
    attach = b64decode(mail.attachments_list[0]['payload'])
    xml = etree.fromstring(attach)
    EntryDateFromEpoch = xml.find('EntryDate')
    if EntryDateFromEpoch is not None:
        EntryDateFromEpoch = EntryDateFromEpoch.text
    else:
        EntryDateFromEpoch = 'Null'
    EmployeeFirstName = xml.find('Employee/FirstName')
    if EmployeeFirstName is not None:
        EmployeeFirstName = EmployeeFirstName.text
    else:
        EmployeeFirstName = 'Null'
    FormName = xml.find('Form/Name')
    if FormName is not None:
        FormName = FormName.text
        if 'PREDITIVA' in FormName:
            FormName = 'PREDITIVA'
        elif 'PREVENTIVA' in FormName:
            FormName = 'PREVENTIVA'
        elif 'CORRETIVA' in FormName:
            FormName = 'CORRETIVA'
        elif 'FOTOGRÁFICO' in FormName:
            FormName = 'N3'
        else:
            FormName = 'OUTROS'

    RefPOICustomerNumber = xml.find(
        'ReferencedPointsOfInterest/PointOfInterest/CustomerNumber')
    if RefPOICustomerNumber is not None:
        RefPOICustomerNumber = RefPOICustomerNumber.text
    else:
        RefPOICustomerNumber = 'Null'
    EventNumber = getEventNumber(xml)
    print(EmployeeFirstName,
        EntryDateFromEpoch,
        FormName,
        EventNumber,
        RefPOICustomerNumber,
        sep=";")



if __name__ == '__main__':
    main(sys.argv[1])

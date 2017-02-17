#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from os import rename
from sys import argv
from lxml import etree


def getFormName(_xml):
    _FormName = _xml.find('Form/Name')
    if _FormName is not None:
        return _FormName.text
    else:
        return None


def getEntryType(_xml):
    _EntryType = _xml.find('EntryType')
    if _EntryType is not None:
        return _EntryType.text
    else:
        return None

def getEntryDate(_xml):
    _EntryDate = _xml.find('EntryDate')
    if _EntryDate is not None:
        return _EntryDate.text
    else:
        return None

def getRefPOICustomerNumber(_xml):
    _RefPOICustomerNumber = _xml.find(
        'ReferencedPointsOfInterest/PointOfInterest/CustomerNumber')
    if _RefPOICustomerNumber is not None:
        return _RefPOICustomerNumber.text[-4:]
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



def main(_xmlfile):
    xml = etree.fromstring(_xmlfile)
    source = argv[1]
    FormName = getFormName(xml)
    if FormName == 'INVENTÁRIO':
        pass
    else:
        EntryDate = getEntryDate(xml)
        CustomerNumber = getRefPOICustomerNumber(xml)
        EventNumber = getEventNumber(xml)

        if EntryDate[2:8] == '012017':
            print(
                source,
                CustomerNumber,
                EntryDate[0:8],
                FormName,
                EventNumber,
                sep=";"
            )

if __name__ == '__main__':
    with open(argv[1], 'rb') as xmlfile:
        xml = xmlfile.read()
        main(xml)

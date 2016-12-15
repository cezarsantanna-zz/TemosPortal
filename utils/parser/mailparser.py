# -*- coding: utf-8 -*-
import email
import base64
from io import StringIO
from datetime import datetime
from email.utils import parseaddr
from email.utils import parsedate
from email.header import decode_header
from email.parser import Parser as EmailParser


class NotSupportedMailFormat(Exception):
    pass


def parse_attachment(message_part):
    content_disposition = message_part.get('Content-Disposition', None)
    if content_disposition:
        dispositions = content_dispositions.strip().split(';')
        if (content_disposition and
            dispositions[0].lower() == 'attachment'):
            file_data = message_part.get_payload(decode=True)
            attachment = StringIO(file_data)
            attachment.content_type = message_part.get_content_type()
            attachment.size = len(file_data)
            attachment.name = None
            attachment.create_date = None
            attachment.mod_date = None
            attachment.read_date = None
            for param in dispositions[1:]:
                name, value = param.split("=")
                name = name.lower()
                if name == "filename":
                    attachment.name = value
                elif name == "create-date":
                    attachment.create_date = value
                elif name == "modification-date":
                    attachment.mod_date = value
                elif name == "read-date":
                    attachment.read_date = value
            return attachment
    return None


def mailparse(content):
    p = EmailParser()
    msgobj = p.parse(content)
    if msgobj['Subject'] is not None:
        decodefrag = decode_header(msgobj['Subject'])
        subj_fragments = []
        for s, enc in decodefrag:
            if enc:
                s = str(s, enc).encode('utf8', 'replace')
            subj_fragments.append(s)
        subject = ''.join(subj_fragments)
    else:
        subject = None
    attachments = []
    body = None
    html = None
    for part in msgobj.walk():
        attachment = parse_attachment(part)
        if attachment:
            attachments.append(attachment)
        elif part.get_content_type() == "text/plain":
            if body is None:
                body = ""
            body += str(
                part.get_payload(decode=True),
                part.get_content_charset(),
                'replace'
            ).encode('utf8', 'replace')
        elif part.get_content_type() == "text/html":
            if html is None:
                html = ""
            html += str(
                part.get_payload(decode=True),
                part.get_content_charset(),
                'replace'
            ).encode('utf8', 'replace')
    return {
        'subject': subject,
        'body': body,
        'html': html,
        'from': parseaddr(msgobj.get('From'))[1],
        'to': parseaddr(msgobj.get('To'))[1],
        'X-Original-To': parseaddr(msgobj.get('X-Original-To'))[1],
        'date': parsedate(msgobj.get('date')),
        'attachments': attachments,
        'keys': list(msgobj.keys()),
    }

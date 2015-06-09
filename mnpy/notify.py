from model import *
import util
import datetime
from sqlalchemy import and_

MNPY_RECEIVER = 'weiyi@papayamobile.com'
#MNPY_RECEIVER = 'appflood_engineer@papayamobile.com'

MNPY_SNIPPET = """
<h4 style="margin:0;margin-bottom:6px;margin-top:6px">
<a style="font-size:14px;line-height:22px;font-weight:bold;text-decoration:none;color:#259;border:none;outline:none" href="%s" target="_blank">%s</a>&nbsp;&nbsp;</h4>
"""

def notify(body='\xe4\xbb\x80\xe4\xb9\x88\xe9\x83\xbd\xe6\xb2\xa1\xe6\x9c\x89......'):
    title = '[Python]\xe7\xa0\x81\xe5\x86\x9c\xe5\x91\xa8\xe5\x88\x8aPython\xe7\x9b\xb8\xe5\x85\xb3\xe4\xb8\xbb\xe9\xa2\x98\xe6\x9b\xb4\xe6\x96\xb0'
    util.send_email(title, body, MNPY_RECEIVER)


def task():
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(1)
    mps = ManongPython.query.filter(and_(ManongPython.create_time>yesterday, ManongPython.create_time<today)).all()
    print '=============', len(mps)
    body = ''
    for mp in mps:
        body += MNPY_SNIPPET % (mp.url, mp.title)
    notify(body)

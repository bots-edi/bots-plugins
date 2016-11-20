import datetime

plugins = [
{'plugintype': 'routes', 'idroute': u'x12_xml2850', 'seq': 1, 'notindefaultrun': False, 'tochannel': u'order_out', 'frommessagetype': u'order01', 'translateind': True, 'fromchannel': u'order_in', 'active': False, 'fromeditype': u'xml'},
{'starttls': False, 'archivepath': u'', 'ftpaccount': u'', 'syslock': False, 'askmdn': u'no', 'inorout': u'out', 'port': 0, 'parameters': u'', 'charset': u'ascii', 'filename': u'*.x12', 'secret': u'', 'apop': False, 'type': u'file', 'username': u'', 'idchannel': u'order_out', 'mdnchannel': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'path': u'botssys/outfile/x12_xml2850', 'plugintype': 'channel', 'lockname': u'', 'remove': False, 'sendmdn': u'no'},
{'starttls': False, 'archivepath': u'', 'ftpaccount': u'', 'syslock': False, 'askmdn': u'no', 'inorout': u'in', 'port': 0, 'parameters': u'', 'charset': u'utf-8', 'filename': u'*.xml', 'secret': u'', 'apop': False, 'type': u'file', 'username': u'', 'idchannel': u'order_in', 'mdnchannel': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'path': u'botssys/infile/x12_xml2850', 'plugintype': 'channel', 'lockname': u'', 'remove': False, 'sendmdn': u'no'},
{'plugintype': 'translate', 'frommessagetype': u'order01', 'toeditype': u'x12', 'frompartner': u'', 'topartner': u'', 'active': True, 'alt': u'', 'fromeditype': u'xml', 'tscript': u'x12_xml2850', 'tomessagetype': u'850004010'},
]

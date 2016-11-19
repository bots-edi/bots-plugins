import datetime

plugins = [
{'plugintype': 'routes', 'idroute': u'837to837', 'seq': 1, 'notindefaultrun': False, 'tochannel': u'x12837_out', 'frommessagetype': u'x12', 'translateind': True, 'fromchannel': u'x12837_in', 'active': False, 'alt': u'', 'fromeditype': u'x12'},
{'starttls': False, 'archivepath': u'', 'ftpaccount': u'', 'syslock': False, 'askmdn': u'no', 'inorout': u'in', 'port': 0, 'parameters': u'', 'charset': u'us-ascii', 'filename': u'*.x12', 'secret': u'', 'apop': False, 'type': u'file', 'username': u'', 'idchannel': u'x12837_in', 'mdnchannel': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'path': u'botssys/infile/837', 'plugintype': 'channel', 'lockname': u'', 'remove': False, 'sendmdn': u'no'},
{'starttls': False, 'archivepath': u'', 'ftpaccount': u'', 'syslock': False, 'askmdn': u'no', 'inorout': u'out', 'port': 0, 'parameters': u'', 'charset': u'us-ascii', 'filename': u'*.x12', 'secret': u'', 'apop': False, 'type': u'file', 'username': u'', 'idchannel': u'x12837_out', 'mdnchannel': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'path': u'botssys/outfile/837', 'plugintype': 'channel', 'lockname': u'', 'remove': False, 'sendmdn': u'no'},
{'plugintype': 'translate', 'frommessagetype': u'837004010X098A1', 'toeditype': u'x12', 'frompartner': u'', 'topartner': u'', 'active': True, 'alt': u'', 'fromeditype': u'x12', 'tscript': u'x12_837_4010_2_x12_837_5010', 'tomessagetype': u'837005010X222'},
]

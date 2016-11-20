import datetime

plugins = [
{'plugintype': 'routes', 'idroute': u'fixed810_2_x12', 'seq': 9999, 'translateind': True, 'tochannel': u'810_out_file', 'frommessagetype': u'fixed_810', 'notindefaultrun': False, 'toeditype': u'x12', 'fromchannel': u'810_in_file', 'active': False, 'alt': u'', 'fromeditype': u'fixed'},
{'starttls': False, 'archivepath': u'', 'ftpaccount': u'', 'syslock': False, 'askmdn': u'no', 'inorout': u'in', 'port': 0, 'parameters': u'', 'charset': u'us-ascii', 'filename': u'*.inh', 'secret': u'', 'apop': False, 'type': u'file', 'username': u'', 'idchannel': u'810_in_file', 'mdnchannel': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'path': u'botssys/infile/fixed810_2_x12', 'plugintype': 'channel', 'lockname': u'', 'remove': False, 'sendmdn': u'no'},
{'starttls': False, 'archivepath': u'', 'ftpaccount': u'', 'syslock': False, 'askmdn': u'no', 'inorout': u'out', 'port': 0, 'parameters': u'', 'charset': u'us-ascii', 'filename': u'810_out*.x12', 'secret': u'', 'apop': False, 'type': u'file', 'username': u'', 'idchannel': u'810_out_file', 'mdnchannel': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'path': u'botssys/outfile/fixed810_2_x12', 'plugintype': 'channel', 'lockname': u'', 'remove': False, 'sendmdn': u'no'},
{'plugintype': 'translate', 'frommessagetype': u'fixed_810', 'toeditype': u'x12', 'frompartner': u'', 'topartner': u'', 'active': True, 'alt': u'', 'fromeditype': u'fixed', 'tscript': u'fixed810_2_x12', 'tomessagetype': u'810004010'},
]

import datetime
version = '3.0.0rc'
plugins = [
{'plugintype': u'channel', 'apop': False, 'archivepath': u'', 'askmdn': u'', 'certfile': None, 'charset': u'utf-8', 'desc': u'', 'filename': u'', 'ftpaccount': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'idchannel': u'exportarticlesxml_in', 'inorout': u'in', 'keyfile': None, 'lockname': u'', 'mdnchannel': u'', 'parameters': u'', 'path': u'botssys/infile/demo_databasecommunication/demo_database.db', 'port': 0, 'remove': False, 'rsrv1': None, 'rsrv2': None, 'rsrv3': None, 'secret': u'', 'sendmdn': u'no', 'starttls': False, 'syslock': False, 'testpath': u'', 'type': u'db', 'username': u''},
{'plugintype': u'channel', 'apop': False, 'archivepath': u'', 'askmdn': u'', 'certfile': None, 'charset': u'utf-8', 'desc': u'', 'filename': u'article_*.xml', 'ftpaccount': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'idchannel': u'exportarticlesxml_out', 'inorout': u'out', 'keyfile': None, 'lockname': u'', 'mdnchannel': u'', 'parameters': u'', 'path': u'botssys/outfile/demo_databasecommunication', 'port': 0, 'remove': False, 'rsrv1': None, 'rsrv2': None, 'rsrv3': None, 'secret': u'', 'sendmdn': u'no', 'starttls': False, 'syslock': False, 'testpath': u'', 'type': u'file', 'username': u''},
{'plugintype': u'channel', 'apop': False, 'archivepath': u'', 'askmdn': u'', 'certfile': None, 'charset': u'utf-8', 'desc': u'', 'filename': u'*.xml', 'ftpaccount': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'idchannel': u'importarticlesxml_in', 'inorout': u'in', 'keyfile': None, 'lockname': u'', 'mdnchannel': u'', 'parameters': u'', 'path': u'botssys/infile/demo_databasecommunication', 'port': 0, 'remove': False, 'rsrv1': None, 'rsrv2': None, 'rsrv3': None, 'secret': u'', 'sendmdn': u'no', 'starttls': False, 'syslock': False, 'testpath': u'', 'type': u'file', 'username': u''},
{'plugintype': u'channel', 'apop': False, 'archivepath': u'', 'askmdn': u'', 'certfile': None, 'charset': u'utf-8', 'desc': u'', 'filename': u'', 'ftpaccount': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'idchannel': u'importarticlesxml_out', 'inorout': u'out', 'keyfile': None, 'lockname': u'', 'mdnchannel': u'', 'parameters': u'', 'path': u'botssys/infile/demo_databasecommunication/demo_database.db', 'port': 0, 'remove': False, 'rsrv1': None, 'rsrv2': None, 'rsrv3': None, 'secret': u'', 'sendmdn': u'no', 'starttls': False, 'syslock': False, 'testpath': u'', 'type': u'db', 'username': u''},
{'plugintype': u'translate', 'active': True, 'alt': u'', 'desc': u'', 'fromeditype': u'db', 'frommessagetype': u'articles', 'frompartner': None, 'rsrv1': None, 'rsrv2': None, 'toeditype': u'xml', 'tomessagetype': u'articles', 'topartner': None, 'tscript': u'articlesdatabase2xml'},
{'plugintype': u'translate', 'active': True, 'alt': u'', 'desc': u'', 'fromeditype': u'xml', 'frommessagetype': u'articles', 'frompartner': None, 'rsrv1': None, 'rsrv2': None, 'toeditype': u'db', 'tomessagetype': u'articles', 'topartner': None, 'tscript': u'articlesxml2db'},
{'plugintype': u'routes', 'active': True, 'alt': u'', 'defer': False, 'desc': u'', 'fromchannel': u'exportarticlesxml_in', 'fromeditype': u'db', 'frommessagetype': u'articles', 'frompartner': None, 'frompartner_tochannel': None, 'idroute': u'exportarticlesxml', 'notindefaultrun': False, 'rsrv1': None, 'rsrv2': None, 'seq': 9999, 'testindicator': u'', 'tochannel': u'exportarticlesxml_out', 'toeditype': u'', 'tomessagetype': u'', 'topartner': None, 'topartner_tochannel': None, 'translateind': 1, 'zip_incoming': None, 'zip_outgoing': None},
{'plugintype': u'routes', 'active': True, 'alt': u'', 'defer': False, 'desc': u'', 'fromchannel': u'importarticlesxml_in', 'fromeditype': u'xml', 'frommessagetype': u'articles', 'frompartner': None, 'frompartner_tochannel': None, 'idroute': u'importarticlesxml', 'notindefaultrun': False, 'rsrv1': None, 'rsrv2': None, 'seq': 9999, 'testindicator': u'', 'tochannel': u'importarticlesxml_out', 'toeditype': u'', 'tomessagetype': u'', 'topartner': None, 'topartner_tochannel': None, 'translateind': 1, 'zip_incoming': None, 'zip_outgoing': None},
]

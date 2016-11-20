import datetime
version = 2
plugins = [
{'plugintype': u'channel', 'apop': False, 'archivepath': u'', 'askmdn': u'', 'certfile': None, 'charset': u'us-ascii', 'desc': u'', 'filename': u'*', 'ftpaccount': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'idchannel': u'inbound_in', 'inorout': u'in', 'keyfile': None, 'lockname': u'', 'mdnchannel': u'', 'parameters': u'', 'path': u'botssys/infile/x12_demo/inbound', 'port': 0, 'remove': False, 'rsrv1': None, 'rsrv2': None, 'rsrv3': None, 'secret': u'', 'sendmdn': u'', 'starttls': False, 'syslock': False, 'type': u'file', 'username': u''},
{'plugintype': u'channel', 'apop': False, 'archivepath': u'', 'askmdn': u'', 'certfile': None, 'charset': u'utf-8', 'desc': u'', 'filename': u'850_*.xml', 'ftpaccount': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'idchannel': u'inbound_out_850', 'inorout': u'out', 'keyfile': None, 'lockname': u'', 'mdnchannel': u'', 'parameters': u'', 'path': u'botssys/outfile/x12_demo/inbound_850', 'port': 0, 'remove': False, 'rsrv1': None, 'rsrv2': None, 'rsrv3': None, 'secret': u'', 'sendmdn': u'', 'starttls': False, 'syslock': False, 'type': u'file', 'username': u''},
{'plugintype': u'channel', 'apop': False, 'archivepath': u'', 'askmdn': u'', 'certfile': None, 'charset': u'us-ascii', 'desc': u'', 'filename': u'997_*.x12', 'ftpaccount': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'idchannel': u'inbound_out_997', 'inorout': u'out', 'keyfile': None, 'lockname': u'', 'mdnchannel': u'', 'parameters': u'', 'path': u'botssys/outfile/x12_demo/997', 'port': 0, 'remove': False, 'rsrv1': None, 'rsrv2': None, 'rsrv3': None, 'secret': u'', 'sendmdn': u'', 'starttls': False, 'syslock': False, 'type': u'file', 'username': u''},
{'plugintype': u'channel', 'apop': False, 'archivepath': u'', 'askmdn': u'', 'certfile': None, 'charset': u'utf-8', 'desc': u'', 'filename': u'*.xml', 'ftpaccount': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'idchannel': u'outbound_asn_in', 'inorout': u'in', 'keyfile': None, 'lockname': u'', 'mdnchannel': u'', 'parameters': u'', 'path': u'botssys/infile/x12_demo/asn', 'port': 0, 'remove': False, 'rsrv1': None, 'rsrv2': None, 'rsrv3': None, 'secret': u'', 'sendmdn': u'', 'starttls': False, 'syslock': False, 'type': u'file', 'username': u''},
{'plugintype': u'channel', 'apop': False, 'archivepath': u'', 'askmdn': u'', 'certfile': None, 'charset': u'us-ascii', 'desc': u'', 'filename': u'856_*.x12', 'ftpaccount': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'idchannel': u'outbound_asn_out', 'inorout': u'out', 'keyfile': None, 'lockname': u'', 'mdnchannel': u'', 'parameters': u'', 'path': u'botssys/outfile/x12_demo/outbound_856', 'port': 0, 'remove': False, 'rsrv1': None, 'rsrv2': None, 'rsrv3': None, 'secret': u'', 'sendmdn': u'', 'starttls': False, 'syslock': False, 'type': u'file', 'username': u''},
{'plugintype': u'channel', 'apop': False, 'archivepath': u'', 'askmdn': u'', 'certfile': None, 'charset': u'utf-8', 'desc': u'', 'filename': u'*.xml', 'ftpaccount': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'idchannel': u'outbound_invoice_in', 'inorout': u'in', 'keyfile': None, 'lockname': u'', 'mdnchannel': u'', 'parameters': u'', 'path': u'botssys/infile/x12_demo/invoice', 'port': 0, 'remove': False, 'rsrv1': None, 'rsrv2': None, 'rsrv3': None, 'secret': u'', 'sendmdn': u'', 'starttls': False, 'syslock': False, 'type': u'file', 'username': u''},
{'plugintype': u'channel', 'apop': False, 'archivepath': u'', 'askmdn': u'', 'certfile': None, 'charset': u'us-ascii', 'desc': u'', 'filename': u'810_*.x12', 'ftpaccount': u'', 'ftpactive': False, 'ftpbinary': False, 'host': u'', 'idchannel': u'outbound_invoice_out', 'inorout': u'out', 'keyfile': None, 'lockname': u'', 'mdnchannel': u'', 'parameters': u'', 'path': u'botssys/outfile/x12_demo/outbound_810', 'port': 0, 'remove': False, 'rsrv1': None, 'rsrv2': None, 'rsrv3': None, 'secret': u'', 'sendmdn': u'', 'starttls': False, 'syslock': False, 'type': u'file', 'username': u''},
{'plugintype': u'partner', 'active': True, 'address1': None, 'address2': None, 'address3': None, 'attr1': None, 'attr2': None, 'attr3': None, 'attr4': None, 'attr5': None, 'cc': u'', 'city': None, 'countrycode': None, 'countrysubdivision': None, 'desc': None, 'enddate': None, 'group': [], 'idpartner': u'BUYER_DIF_ASN', 'isgroup': False, 'mail': u'', 'name': u'buyer wants a different asn', 'name1': None, 'name2': None, 'name3': None, 'phone1': None, 'phone2': None, 'postalcode': None, 'rsrv1': None, 'rsrv2': None, 'startdate': None},
{'plugintype': u'translate', 'active': True, 'alt': u'', 'desc': u'', 'fromeditype': u'x12', 'frommessagetype': u'850004010', 'frompartner': None, 'rsrv1': None, 'rsrv2': None, 'toeditype': u'xml', 'tomessagetype': u'orders', 'topartner': None, 'tscript': u'orders_x122xml'},
{'plugintype': u'translate', 'active': True, 'alt': u'', 'desc': u'', 'fromeditype': u'x12', 'frommessagetype': u'850004010VICS', 'frompartner': None, 'rsrv1': None, 'rsrv2': None, 'toeditype': u'xml', 'tomessagetype': u'orders', 'topartner': None, 'tscript': u'orders_x122xml'},
{'plugintype': u'translate', 'active': True, 'alt': u'', 'desc': u'', 'fromeditype': u'x12', 'frommessagetype': u'997004010', 'frompartner': None, 'rsrv1': None, 'rsrv2': None, 'toeditype': u'xmlnocheck', 'tomessagetype': u'dummy', 'topartner': None, 'tscript': u'process997'},
{'plugintype': u'translate', 'active': True, 'alt': u'', 'desc': u'', 'fromeditype': u'xml', 'frommessagetype': u'asn', 'frompartner': None, 'rsrv1': None, 'rsrv2': None, 'toeditype': u'x12', 'tomessagetype': u'856004010', 'topartner': None, 'tscript': u'asn_xml2x12'},
{'plugintype': u'translate', 'active': True, 'alt': u'', 'desc': u'', 'fromeditype': u'xml', 'frommessagetype': u'asn', 'frompartner': None, 'rsrv1': None, 'rsrv2': None, 'toeditype': u'x12', 'tomessagetype': u'856004010', 'topartner': u'BUYER_DIF_ASN', 'tscript': u'asn_xml2x12_different'},
{'plugintype': u'translate', 'active': True, 'alt': u'', 'desc': u'', 'fromeditype': u'xml', 'frommessagetype': u'invoice', 'frompartner': None, 'rsrv1': None, 'rsrv2': None, 'toeditype': u'x12', 'tomessagetype': u'810004010', 'topartner': None, 'tscript': u'invoice_xml2x12'},
{'plugintype': u'routes', 'active': True, 'alt': u'', 'defer': False, 'desc': u'inbound is a composite route:\r\n- seq 1 just does the input. x12 is coming in, but several message types\r\n  will be coming in (eg 850, 997)\r\n- seq 100 just does the translation\r\n- seq 1000 and above out-communicate the different messagetypes \r\n  to seperate directories using filtering.\r\n\r\n', 'fromchannel': u'inbound_in', 'fromeditype': u'x12', 'frommessagetype': u'x12', 'frompartner': None, 'frompartner_tochannel': None, 'idroute': u'inbound', 'notindefaultrun': False, 'rsrv1': None, 'rsrv2': None, 'seq': 1, 'testindicator': u'', 'tochannel': None, 'toeditype': u'', 'tomessagetype': u'', 'topartner': None, 'topartner_tochannel': None, 'translateind': 0, 'zip_incoming': None, 'zip_outgoing': None},
{'plugintype': u'routes', 'active': True, 'alt': u'', 'defer': False, 'desc': u'', 'fromchannel': None, 'fromeditype': u'', 'frommessagetype': u'', 'frompartner': None, 'frompartner_tochannel': None, 'idroute': u'inbound', 'notindefaultrun': False, 'rsrv1': None, 'rsrv2': None, 'seq': 100, 'testindicator': u'', 'tochannel': None, 'toeditype': u'', 'tomessagetype': u'', 'topartner': None, 'topartner_tochannel': None, 'translateind': 1, 'zip_incoming': None, 'zip_outgoing': None},
{'plugintype': u'routes', 'active': True, 'alt': u'', 'defer': False, 'desc': u'', 'fromchannel': None, 'fromeditype': u'', 'frommessagetype': u'', 'frompartner': None, 'frompartner_tochannel': None, 'idroute': u'inbound', 'notindefaultrun': False, 'rsrv1': None, 'rsrv2': None, 'seq': 1000, 'testindicator': u'', 'tochannel': u'inbound_out_850', 'toeditype': u'xml', 'tomessagetype': u'orders', 'topartner': None, 'topartner_tochannel': None, 'translateind': 0, 'zip_incoming': None, 'zip_outgoing': None},
{'plugintype': u'routes', 'active': True, 'alt': u'', 'defer': False, 'desc': u'', 'fromchannel': None, 'fromeditype': u'', 'frommessagetype': u'', 'frompartner': None, 'frompartner_tochannel': None, 'idroute': u'inbound', 'notindefaultrun': False, 'rsrv1': None, 'rsrv2': None, 'seq': 1010, 'testindicator': u'', 'tochannel': u'inbound_out_997', 'toeditype': u'x12', 'tomessagetype': u'', 'topartner': None, 'topartner_tochannel': None, 'translateind': 0, 'zip_incoming': None, 'zip_outgoing': None},
{'plugintype': u'routes', 'active': False, 'alt': u'', 'defer': False, 'desc': u'', 'fromchannel': u'outbound_asn_in', 'fromeditype': u'xml', 'frommessagetype': u'asn', 'frompartner': None, 'frompartner_tochannel': None, 'idroute': u'outbound_asn', 'notindefaultrun': False, 'rsrv1': None, 'rsrv2': None, 'seq': 1, 'testindicator': u'', 'tochannel': u'outbound_asn_out', 'toeditype': u'', 'tomessagetype': u'', 'topartner': None, 'topartner_tochannel': None, 'translateind': 1, 'zip_incoming': None, 'zip_outgoing': None},
{'plugintype': u'routes', 'active': False, 'alt': u'', 'defer': False, 'desc': u'', 'fromchannel': u'outbound_invoice_in', 'fromeditype': u'xml', 'frommessagetype': u'invoice', 'frompartner': None, 'frompartner_tochannel': None, 'idroute': u'outbound_invoice', 'notindefaultrun': False, 'rsrv1': None, 'rsrv2': None, 'seq': 1, 'testindicator': u'', 'tochannel': u'outbound_invoice_out', 'toeditype': u'', 'tomessagetype': u'', 'topartner': None, 'topartner_tochannel': None, 'translateind': 1, 'zip_incoming': None, 'zip_outgoing': None},
{'plugintype': u'confirmrule', 'active': True, 'confirmtype': u'ask-x12-997', 'editype': u'', 'frompartner': None, 'idchannel': u'outbound_invoice_in', 'idroute': u'', 'messagetype': u'', 'negativerule': False, 'rsrv1': None, 'rsrv2': None, 'ruletype': u'channel', 'topartner': None},
{'plugintype': u'confirmrule', 'active': True, 'confirmtype': u'send-x12-997', 'editype': u'x12', 'frompartner': None, 'idchannel': None, 'idroute': u'', 'messagetype': u'850', 'negativerule': False, 'rsrv1': None, 'rsrv2': None, 'ruletype': u'messagetype', 'topartner': None},
]

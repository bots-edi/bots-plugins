# BOTS Grammar file for IDoc INVOIC02
# Generated with IDOC2BOTS by Mike Griffin
# 11:22 am Thursday, 12 February 2009
# 14/12/2009 added syntax, nextmessage and botskey query

from bots.botsconfig import *

syntax = {
          'checkcharsetin':'botsreplace',
         }

nextmessage = ({'BOTSID':'EDI_DC40'},)

structure=[
    {ID:'EDI_DC40',MIN:1,MAX:999,
        QUERIES:{
            'frompartner':  {'BOTSID':'EDI_DC40','SNDPRN':None},
            'topartner':    {'BOTSID':'EDI_DC40','RCVPRN':None},
            'testindicator':{'BOTSID':'EDI_DC40','TEST':None},
            'botskey':      ({'BOTSID':'EDI_DC40'},{'BOTSID':'E1EDK01'},{'BOTSID':'E1EDK02','QUALF':'009','BELNR':None}),
            },
        LEVEL:[
        {ID:'E1EDK01',MIN:1,MAX:99999,LEVEL:[
            {ID:'E1EDKA1',MIN:0,MAX:99},
            {ID:'E1EDK02',MIN:0,MAX:20},
            {ID:'E1EDK03',MIN:0,MAX:20},
            {ID:'E1EDK05',MIN:0,MAX:99},
            {ID:'E1EDK04',MIN:0,MAX:25},
            {ID:'E1EDK17',MIN:0,MAX:10},
            {ID:'E1EDK18',MIN:0,MAX:10},
            {ID:'E1EDK23',MIN:0,MAX:4},
            {ID:'E1EDK28',MIN:0,MAX:20},
            {ID:'E1EDK29',MIN:0,MAX:20},
            {ID:'E1EDKT1',MIN:0,MAX:99,LEVEL:[
                {ID:'E1EDKT2',MIN:0,MAX:999},
                ]},
            {ID:'E1EDK14',MIN:0,MAX:10},
            {ID:'E1EDP01',MIN:0,MAX:99999,LEVEL:[
                {ID:'E1EDP02',MIN:0,MAX:25},
                {ID:'E1EDP03',MIN:0,MAX:25},
                {ID:'E1EDP19',MIN:0,MAX:10},
                {ID:'E1EDP26',MIN:0,MAX:20},
                {ID:'E1EDPA1',MIN:0,MAX:20},
                {ID:'E1EDP05',MIN:0,MAX:99},
                {ID:'E1EDP04',MIN:0,MAX:25},
                {ID:'E1EDP28',MIN:0,MAX:9},
                {ID:'E1EDP08',MIN:0,MAX:99999},
                {ID:'E1EDP30',MIN:0,MAX:99},
                {ID:'E1EDPT1',MIN:0,MAX:99,LEVEL:[
                    {ID:'E1EDPT2',MIN:0,MAX:999},
                    ]},
                ]},
            {ID:'E1EDS01',MIN:0,MAX:30},
            ]},
        ]},
    ]

recorddefs={
    'EDI_DC40':[
        ['BOTSID','C',10,'AN'],      # 000001-000010 Name of Table Structure
        ['MANDT','C',3,'AN'],        # 000011-000013 Client
        ['DOCNUM','C',16,'AN'],      # 000014-000029 IDoc number
        ['DOCREL','C',4,'AN'],       # 000030-000033 SAP Release for IDoc
        ['STATUS','C',2,'AN'],       # 000034-000035 Status of IDoc
        ['DIRECT','C',1,'AN'],       # 000036-000036 Direction
        ['OUTMOD','C',1,'AN'],       # 000037-000037 Output mode
        ['EXPRSS','C',1,'AN'],       # 000038-000038 Overriding in inbound processing
        ['TEST','C',1,'AN'],         # 000039-000039 Test flag
        ['IDOCTYP','C',30,'AN'],     # 000040-000069 Name of basic type
        ['CIMTYP','C',30,'AN'],      # 000070-000099 Extension (defined by customer)
        ['MESTYP','C',30,'AN'],      # 000100-000129 Message type
        ['MESCOD','C',3,'AN'],       # 000130-000132 Message code
        ['MESFCT','C',3,'AN'],       # 000133-000135 Message function
        ['STD','C',1,'AN'],          # 000136-000136 EDI standard, flag
        ['STDVRS','C',6,'AN'],       # 000137-000142 EDI standard, version and release
        ['STDMES','C',6,'AN'],       # 000143-000148 EDI message type
        ['SNDPOR','C',10,'AN'],      # 000149-000158 Sender port (SAP System, external subsystem)
        ['SNDPRT','C',2,'AN'],       # 000159-000160 Partner type of sender
        ['SNDPFC','C',2,'AN'],       # 000161-000162 Partner Function of Sender
        ['SNDPRN','C',10,'AN'],      # 000163-000172 Partner Number of Sender
        ['SNDSAD','C',21,'AN'],      # 000173-000193 Sender address (SADR)
        ['SNDLAD','C',70,'AN'],      # 000194-000263 Logical address of sender
        ['RCVPOR','C',10,'AN'],      # 000264-000273 Receiver port
        ['RCVPRT','C',2,'AN'],       # 000274-000275 Partner Type of receiver
        ['RCVPFC','C',2,'AN'],       # 000276-000277 Partner function of recipient
        ['RCVPRN','C',10,'AN'],      # 000278-000287 Partner number of recipient
        ['RCVSAD','C',21,'AN'],      # 000288-000308 Recipient address (SADR)
        ['RCVLAD','C',70,'AN'],      # 000309-000378 Logical address of recipient
        ['CREDAT','C',8,'AN'],       # 000379-000386 Created on
        ['CRETIM','C',6,'AN'],       # 000387-000392 Created at
        ['REFINT','C',14,'AN'],      # 000393-000406 Transmission file (EDI Interchange)
        ['REFGRP','C',14,'AN'],      # 000407-000420 Message group (EDI Message Group)
        ['REFMES','C',14,'AN'],      # 000421-000434 Message (EDI Message)
        ['ARCKEY','C',70,'AN'],      # 000435-000504 Key for external message archive
        ['SERIAL','C',20,'AN'],      # 000505-000524 Serialization
        ],
    'E1EDK01':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['ACTION','C',3,'AN'],       # 000064-000066 Action code for the whole EDI message
        ['KZABS','C',1,'AN'],        # 000067-000067 Flag: order acknowledgment required
        ['CURCY','C',3,'AN'],        # 000068-000070 Currency
        ['HWAER','C',3,'AN'],        # 000071-000073 EDI local currency
        ['WKURS','C',12,'AN'],       # 000074-000085 Exchange rate
        ['ZTERM','C',17,'AN'],       # 000086-000102 Terms of payment key
        ['KUNDEUINR','C',20,'AN'],   # 000103-000122 VAT registration number
        ['EIGENUINR','C',20,'AN'],   # 000123-000142 VAT registration number
        ['BSART','C',4,'AN'],        # 000143-000146 Document type
        ['BELNR','C',35,'AN'],       # 000147-000181 IDOC document number
        ['NTGEW','C',18,'AN'],       # 000182-000199 Net weight
        ['BRGEW','C',18,'AN'],       # 000200-000217 Net weight
        ['GEWEI','C',3,'AN'],        # 000218-000220 Weight unit
        ['FKART_RL','C',4,'AN'],     # 000221-000224 Invoice list type
        ['ABLAD','C',25,'AN'],       # 000225-000249 Unloading Point
        ['BSTZD','C',4,'AN'],        # 000250-000253 Purchase order number supplement
        ['VSART','C',2,'AN'],        # 000254-000255 Shipping conditions
        ['VSART_BEZ','C',20,'AN'],   # 000256-000275 Description of the Shipping Type
        ['RECIPNT_NO','C',10,'AN'],  # 000276-000285 Number of recipient (for control via the ALE model)
        ['KZAZU','C',1,'AN'],        # 000286-000286 Order combination indicator
        ['AUTLF','C',1,'AN'],        # 000287-000287 Complete delivery defined for each sales order?
        ['AUGRU','C',3,'AN'],        # 000288-000290 Order reason (reason for the business transaction)
        ['AUGRU_BEZ','C',40,'AN'],   # 000291-000330 Description
        ['ABRVW','C',3,'AN'],        # 000331-000333 Usage indicator
        ['ABRVW_BEZ','C',20,'AN'],   # 000334-000353 Description
        ['FKTYP','C',1,'AN'],        # 000354-000354 Billing category
        ['LIFSK','C',2,'AN'],        # 000355-000356 Delivery block (document header)
        ['LIFSK_BEZ','C',20,'AN'],   # 000357-000376 Description
        ['EMPST','C',25,'AN'],       # 000377-000401 Receiving point
        ['ABTNR','C',4,'AN'],        # 000402-000405 Department number
        ['DELCO','C',3,'AN'],        # 000406-000408 Agreed delivery time
        ['WKURS_M','C',12,'AN'],     # 000409-000420 Indirectly quoted exchange rate in an IDoc segment
        ],
    'E1EDKA1':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['PARVW','C',3,'AN'],        # 000064-000066 Partner function (e.g. sold-to party, ship-to party, ...)
        ['PARTN','C',17,'AN'],       # 000067-000083 Partner number
        ['LIFNR','C',17,'AN'],       # 000084-000100 Vendor number at customer location
        ['NAME1','C',35,'AN'],       # 000101-000135 Name 1
        ['NAME2','C',35,'AN'],       # 000136-000170 Name 2
        ['NAME3','C',35,'AN'],       # 000171-000205 Name 3
        ['NAME4','C',35,'AN'],       # 000206-000240 Name 4
        ['STRAS','C',35,'AN'],       # 000241-000275 Street and house number 1
        ['STRS2','C',35,'AN'],       # 000276-000310 Street and house number 2
        ['PFACH','C',35,'AN'],       # 000311-000345 PO Box
        ['ORT01','C',35,'AN'],       # 000346-000380 City
        ['COUNC','C',9,'AN'],        # 000381-000389 County code
        ['PSTLZ','C',9,'AN'],        # 000390-000398 Postal code
        ['PSTL2','C',9,'AN'],        # 000399-000407 P.O. Box postal code
        ['LAND1','C',3,'AN'],        # 000408-000410 Country key
        ['ABLAD','C',35,'AN'],       # 000411-000445 Unloading Point
        ['PERNR','C',30,'AN'],       # 000446-000475 Contact person's personnel number
        ['PARNR','C',30,'AN'],       # 000476-000505 Contact person's number (not personnel number)
        ['TELF1','C',25,'AN'],       # 000506-000530 1st telephone number of contact person
        ['TELF2','C',25,'AN'],       # 000531-000555 2nd telephone number of contact person
        ['TELBX','C',25,'AN'],       # 000556-000580 Telebox number
        ['TELFX','C',25,'AN'],       # 000581-000605 Fax number
        ['TELTX','C',25,'AN'],       # 000606-000630 Teletex number
        ['TELX1','C',25,'AN'],       # 000631-000655 Telex number
        ['SPRAS','C',1,'AN'],        # 000656-000656 Language key
        ['ANRED','C',15,'AN'],       # 000657-000671 Form of Address
        ['ORT02','C',35,'AN'],       # 000672-000706 District
        ['HAUSN','C',6,'AN'],        # 000707-000712 House number
        ['STOCK','C',6,'AN'],        # 000713-000718 Floor
        ['REGIO','C',3,'AN'],        # 000719-000721 Region
        ['PARGE','C',1,'AN'],        # 000722-000722 Partner's gender
        ['ISOAL','C',2,'AN'],        # 000723-000724 Country ISO code
        ['ISONU','C',2,'AN'],        # 000725-000726 Country ISO code
        ['FCODE','C',20,'AN'],       # 000727-000746 Company key (France)
        ['IHREZ','C',30,'AN'],       # 000747-000776 Your reference (Partner)
        ['BNAME','C',35,'AN'],       # 000777-000811 IDoc user name
        ['PAORG','C',30,'AN'],       # 000812-000841 IDOC organization code
        ['ORGTX','C',35,'AN'],       # 000842-000876 IDoc organization code text
        ['PAGRU','C',30,'AN'],       # 000877-000906 IDoc group code
        ['KNREF','C',30,'AN'],       # 000907-000936 Customer description of partner (plant, storage location)
        ['ILNNR','C',70,'AN'],       # 000937-001006 Character field, length 70
        ['PFORT','C',35,'AN'],       # 001007-001041 PO Box city
        ['SPRAS_ISO','C',2,'AN'],    # 001042-001043 Language according to ISO 639
        ['TITLE','C',15,'AN'],       # 001044-001058 Title
        ],
    'E1EDK02':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['QUALF','C',3,'AN'],        # 000064-000066 IDOC qualifier reference document
        ['BELNR','C',35,'AN'],       # 000067-000101 IDOC document number
        ['POSNR','C',6,'AN'],        # 000102-000107 Item number
        ['DATUM','C',8,'AN'],        # 000108-000115 IDOC: Date
        ['UZEIT','C',6,'AN'],        # 000116-000121 IDOC: Time
        ],
    'E1EDK03':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['IDDAT','C',3,'AN'],        # 000064-000066 Qualifier for IDOC date segment
        ['DATUM','C',8,'AN'],        # 000067-000074 IDOC: Date
        ['UZEIT','C',6,'AN'],        # 000075-000080 IDOC: Time
        ],
    'E1EDK05':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['ALCKZ','C',3,'AN'],        # 000064-000066 Surcharge or discount indicator
        ['KSCHL','C',4,'AN'],        # 000067-000070 Condition type (coded)
        ['KOTXT','C',80,'AN'],       # 000071-000150 Condition text
        ['BETRG','C',18,'AN'],       # 000151-000168 Fixed surcharge/discount on total gross
        ['KPERC','C',8,'AN'],        # 000169-000176 Condition percentage rate
        ['KRATE','C',15,'AN'],       # 000177-000191 Condition record per unit
        ['UPRBS','C',9,'AN'],        # 000192-000200 Price unit
        ['MEAUN','C',3,'AN'],        # 000201-000203 Unit of measurement
        ['KOBTR','C',18,'AN'],       # 000204-000221 IDoc condition end amount
        ['MWSKZ','C',7,'AN'],        # 000222-000228 VAT indicator
        ['MSATZ','C',17,'AN'],       # 000229-000245 VAT rate
        ['KOEIN','C',3,'AN'],        # 000246-000248 Currency
        ],
    'E1EDK04':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['MWSKZ','C',7,'AN'],        # 000064-000070 VAT indicator
        ['MSATZ','C',17,'AN'],       # 000071-000087 VAT rate
        ['MWSBT','C',18,'AN'],       # 000088-000105 Value added tax amount
        ['TXJCD','C',15,'AN'],       # 000106-000120 Tax Jurisdiction
        ['KTEXT','C',50,'AN'],       # 000121-000170 Text Field
        ],
    'E1EDK17':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['QUALF','C',3,'AN'],        # 000064-000066 IDOC qualifier: Terms of delivery
        ['LKOND','C',3,'AN'],        # 000067-000069 IDOC delivery condition code
        ['LKTEXT','C',70,'AN'],      # 000070-000139 IDOC delivery condition text
        ],
    'E1EDK18':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['QUALF','C',3,'AN'],        # 000064-000066 IDOC qualifier: Terms of payment
        ['TAGE','C',8,'AN'],         # 000067-000074 IDOC Number of days
        ['PRZNT','C',8,'AN'],        # 000075-000082 IDOC percentage for terms of payment
        ['ZTERM_TXT','C',70,'AN'],   # 000083-000152 Text line
        ],
    'E1EDK23':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['QUALF','C',3,'AN'],        # 000064-000066 Qualifier currency
        ['WAERZ','C',3,'AN'],        # 000067-000069 Three-digit character field for IDocs
        ['WAERQ','C',3,'AN'],        # 000070-000072 Three-digit character field for IDocs
        ['KURS','C',12,'AN'],        # 000073-000084 Character Field of Length 12
        ['DATUM','C',8,'AN'],        # 000085-000092 IDOC: Date
        ['ZEIT','C',6,'AN'],         # 000093-000098 IDOC: Time
        ['KURS_M','C',12,'AN'],      # 000099-000110 Indirectly quoted exchange rate in an IDoc segment
        ],
    'E1EDK28':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['BCOUN','C',3,'AN'],        # 000064-000066 Country key
        ['BRNUM','C',17,'AN'],       # 000067-000083 Bank Key
        ['BNAME','C',70,'AN'],       # 000084-000153 Bank name
        ['BALOC','C',70,'AN'],       # 000154-000223 Location of bank
        ['ACNUM','C',30,'AN'],       # 000224-000253 Account number in bank data
        ['ACNAM','C',35,'AN'],       # 000254-000288 Account holder in bank data
        ],
    'E1EDK29':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['EXNUM','C',10,'AN'],       # 000064-000073 Number of foreign trade data in MM and SD documents
        ['ALAND','C',3,'AN'],        # 000074-000076 Departure country (country from which the goods are sent)
        ['EXPVZ','C',1,'AN'],        # 000077-000077 Mode of Transport for Foreign Trade
        ['ZOLLA','C',6,'AN'],        # 000078-000083 Customs office: Office of exit for foreign trade
        ['ZOLLB','C',6,'AN'],        # 000084-000089 Customs office: Office of destination for foreign trade
        ['ZOLL1','C',6,'AN'],        # 000090-000095 Customs office: Customs office 1 for foreign trade
        ['ZOLL2','C',6,'AN'],        # 000096-000101 Customs office: Customs office 2 for foreign trade
        ['ZOLL3','C',6,'AN'],        # 000102-000107 Customs office: Customs office 3 for foreign trade
        ['ZOLL4','C',6,'AN'],        # 000108-000113 Customs office: Customs office 4 for foreign trade
        ['ZOLL5','C',6,'AN'],        # 000114-000119 Customs office: Customs office 5 for foreign trade
        ['ZOLL6','C',6,'AN'],        # 000120-000125 Customs office: Customs office 6 for foreign trade
        ['KZGBE','C',30,'AN'],       # 000126-000155 Indicator for means of transport crossing the border
        ['KZABE','C',30,'AN'],       # 000156-000185 Indicator for the means of transport at departure
        ['STGBE','C',3,'AN'],        # 000186-000188 Origin of Means of Transport when Crossing the Border
        ['STABE','C',3,'AN'],        # 000189-000191 Country of Origin of the Means of Transport at Departure
        ['CONTA','C',1,'AN'],        # 000192-000192 ID: Goods cross border in a container
        ['GRWCU','C',5,'AN'],        # 000193-000197 Currency of statistical values for foreign trade
        ['GRWRT','C',18,'AN'],       # 000198-000215 Total value of sum segment
        ['LAND1','C',3,'AN'],        # 000216-000218 Country Key
        ['LANDX','C',15,'AN'],       # 000219-000233 Country Name
        ['LANDA','C',3,'AN'],        # 000234-000236 Alternative Country Key
        ['XEGLD','C',1,'AN'],        # 000237-000237 Indicator: European Union Member?
        ['FREIH','C',1,'AN'],        # 000238-000238 Indicator: Free Trade Area for Legal Control
        ['EWRCO','C',1,'AN'],        # 000239-000239 ID: European Economic Area (rel. for export control)
        ['USC05','C',5,'AN'],        # 000240-000244 USA: Five-Digit Country Code (SED: Schedule C Code)
        ['JAP05','C',5,'AN'],        # 000245-000249 Japan: Five digit country code (MITI customs declaration)
        ['ALANX','C',15,'AN'],       # 000250-000264 Country of dispatch - Description
        ['ALANA','C',3,'AN'],        # 000265-000267 Alternative country key for country of dispatch/export
        ['LASTA','C',3,'AN'],        # 000268-000270 Alt. key to nationality of means of transport (departarture)
        ['LASTG','C',3,'AN'],        # 000271-000273 Alt. key for nationality of means of transport at border
        ['ALSCH','C',3,'AN'],        # 000274-000276 Alternative country key for sold-to party
        ['ALSRE','C',5,'AN'],        # 000277-000281 Currency code by country directory
        ['LADEO','C',15,'AN'],       # 000282-000296 Place of loading
        ['IEVER','C',1,'AN'],        # 000297-000297 Domestic Mode of Transport for Foreign Trade
        ['BANR01','C',16,'AN'],      # 000298-000313 FT-EDI: Declarations to the authorities - ID no. 01
        ['BANR02','C',3,'AN'],       # 000314-000316 FT-EDI: Declarations to the authorities: ID no.
        ['BANR03','C',7,'AN'],       # 000317-000323 Customs number of exporter
        ['BANR04','C',7,'AN'],       # 000324-000330 Customs number of exporter
        ['BANR05','C',7,'AN'],       # 000331-000337 Customs number of exporter
        ['BANR06','C',7,'AN'],       # 000338-000344 Customs number of exporter
        ['BANR07','C',7,'AN'],       # 000345-000351 Customs number of exporter
        ['BANR08','C',7,'AN'],       # 000352-000358 Customs number of exporter
        ['BANR09','C',3,'AN'],       # 000359-000361 FT-EDI: Declarations to the authorities: ID no.
        ['BANR10','C',8,'AN'],       # 000362-000369 FT-EDI: Declarations to the authorities - ID no. 10
        ['WZOCU','C',5,'AN'],        # 000370-000374 Currency of customs values for import procg in foreign trade
        ['EXPVZTX','C',20,'AN'],     # 000375-000394 Description
        ['ZOLLATX','C',30,'AN'],     # 000395-000424 Description
        ['ZOLLBTX','C',30,'AN'],     # 000425-000454 Description
        ['STGBETX','C',15,'AN'],     # 000455-000469 Country Name
        ['STABETX','C',15,'AN'],     # 000470-000484 Country Name
        ['FREIHTX','C',20,'AN'],     # 000485-000504 Description
        ['LADEL','C',40,'AN'],       # 000505-000544 Place of loading/unloading for foreign trade
        ['TEXT1','C',40,'AN'],       # 000545-000584 Comments: Text for foreign trade processing
        ['TEXT2','C',40,'AN'],       # 000585-000624 Comments: Text for foreign trade processing
        ['TEXT3','C',40,'AN'],       # 000625-000664 Comments: Text for foreign trade processing
        ['GBNUM','C',20,'AN'],       # 000665-000684 Foreign Trade:Customs declaration list no. for Foreign Trade
        ['REGNR','C',20,'AN'],       # 000685-000704 Registration number for import processing in foreign trade
        ['AUSFU','C',10,'AN'],       # 000705-000714 Exporter for import processing in foreign trade
        ['IEVER_TX','C',20,'AN'],    # 000715-000734 Description
        ['LAZL1','C',3,'AN'],        # 000735-000737 Customs office: Country of customs office for foreign trade
        ['LAZL2','C',3,'AN'],        # 000738-000740 Customs office: Country of customs office for foreign trade
        ['LAZL3','C',3,'AN'],        # 000741-000743 Customs office: Country of customs office for foreign trade
        ['LAZL4','C',3,'AN'],        # 000744-000746 Customs office: Country of customs office for foreign trade
        ['LAZL5','C',3,'AN'],        # 000747-000749 Customs office: Country of customs office for foreign trade
        ['LAZL6','C',3,'AN'],        # 000750-000752 Customs office: Country of customs office for foreign trade
        ['AZOLL','C',6,'AN'],        # 000753-000758 Customs office: Export customs office for foreign trade
        ['AZOLLTX','C',30,'AN'],     # 000759-000788 Description
        ['BFMAR','C',6,'AN'],        # 000789-000794 Foreign Trade: Type of means of transport
        ['FTVBD','C',1,'AN'],        # 000795-000795 Association Indicator for Foreign Trade
        ['CUDCL','C',3,'AN'],        # 000796-000798 Customs declaration type for customs processing in FT
        ['FTUPD','C',1,'AN'],        # 000799-000799 Data service update indicator - Foreign Trade
        ],
    'E1EDKT1':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['TDID','C',4,'AN'],         # 000064-000067 Text ID
        ['TSSPRAS','C',3,'AN'],      # 000068-000070 Language Key
        ['TSSPRAS_ISO','C',2,'AN'],  # 000071-000072 Language according to ISO 639
        ['TDOBJECT','C',10,'AN'],    # 000073-000082 Texts: application object
        ['TDOBNAME','C',70,'AN'],    # 000083-000152 Name
        ],
    'E1EDKT2':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['TDLINE','C',70,'AN'],      # 000064-000133 Text line
        ['TDFORMAT','C',2,'AN'],     # 000134-000135 Tag column
        ],
    'E1EDK14':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['QUALF','C',3,'AN'],        # 000064-000066 IDOC qualifer organization
        ['ORGID','C',35,'AN'],       # 000067-000101 IDOC organization
        ],
    'E1EDP01':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['POSEX','C',6,'AN'],        # 000064-000069 Item number
        ['ACTION','C',3,'AN'],       # 000070-000072 Action code for the item
        ['PSTYP','C',1,'AN'],        # 000073-000073 Item Category
        ['KZABS','C',1,'AN'],        # 000074-000074 Flag: order acknowledgment required
        ['MENGE','C',15,'AN'],       # 000075-000089 Quantity
        ['MENEE','C',3,'AN'],        # 000090-000092 Unit of measure
        ['BMNG2','C',15,'AN'],       # 000093-000107 Quantity in price unit
        ['PMENE','C',3,'AN'],        # 000108-000110 Price unit of measure
        ['ABFTZ','C',7,'AN'],        # 000111-000117 Agreed cumulative quantity
        ['VPREI','C',15,'AN'],       # 000118-000132 Price (net)
        ['PEINH','C',9,'AN'],        # 000133-000141 Price unit
        ['NETWR','C',18,'AN'],       # 000142-000159 Item value (net)
        ['ANETW','C',18,'AN'],       # 000160-000177 Absolute net value of item
        ['SKFBP','C',18,'AN'],       # 000178-000195 Amount qualifying for cash discount
        ['NTGEW','C',18,'AN'],       # 000196-000213 Net weight
        ['GEWEI','C',3,'AN'],        # 000214-000216 Weight unit
        ['EINKZ','C',1,'AN'],        # 000217-000217 Flag: More than one schedule line for the item
        ['CURCY','C',3,'AN'],        # 000218-000220 Currency
        ['PREIS','C',18,'AN'],       # 000221-000238 Gross price
        ['MATKL','C',9,'AN'],        # 000239-000247 IDOC material class
        ['UEPOS','C',6,'AN'],        # 000248-000253 Higher-Level Item in BOM Structures
        ['GRKOR','C',3,'AN'],        # 000254-000256 Delivery group (items delivered together)
        ['EVERS','C',7,'AN'],        # 000257-000263 Shipping instructions
        ['BPUMN','C',6,'AN'],        # 000264-000269 Denominator for conv. of order price unit into order unit
        ['BPUMZ','C',6,'AN'],        # 000270-000275 Numerator for conversion of order price unit into order unit
        ['ABGRU','C',2,'AN'],        # 000276-000277 Reason for rejection of quotations and sales orders
        ['ABGRT','C',40,'AN'],       # 000278-000317 Description
        ['ANTLF','C',1,'AN'],        # 000318-000318 Maximum number of partial deliveries allowed per item
        ['FIXMG','C',1,'AN'],        # 000319-000319 Delivery date and quantity fixed
        ['KZAZU','C',1,'AN'],        # 000320-000320 Order combination indicator
        ['BRGEW','C',18,'AN'],       # 000321-000338 Total weight
        ['PSTYV','C',4,'AN'],        # 000339-000342 Sales document item category
        ['EMPST','C',25,'AN'],       # 000343-000367 Receiving point
        ['ABTNR','C',4,'AN'],        # 000368-000371 Department number
        ['ABRVW','C',3,'AN'],        # 000372-000374 Usage indicator
        ['WERKS','C',4,'AN'],        # 000375-000378 Plant
        ['LPRIO','C',2,'AN'],        # 000379-000380 Delivery Priority
        ['LPRIO_BEZ','C',20,'AN'],   # 000381-000400 Description
        ['ROUTE','C',6,'AN'],        # 000401-000406 Route
        ['ROUTE_BEZ','C',40,'AN'],   # 000407-000446 Description
        ['LGORT','C',4,'AN'],        # 000447-000450 Storage location
        ['VSTEL','C',4,'AN'],        # 000451-000454 Shipping Point/Receiving Point
        ['DELCO','C',3,'AN'],        # 000455-000457 Agreed delivery time
        ['MATNR','C',35,'AN'],       # 000458-000492 IDOC material ID
        ['VALTG','C',2,'AN'],        # 000493-000494 Additional value days
        ['HIPOS','C',6,'AN'],        # 000495-000500 Superior item in an item hierarchy
        ['HIEVW','C',1,'AN'],        # 000501-000501 Use of Hierarchy Item
        ['POSGUID','C',22,'AN'],     # 000502-000523 ATP: Encryption of DELNR and DELPS
        ],
    'E1EDP02':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['QUALF','C',3,'AN'],        # 000064-000066 IDOC qualifier reference document
        ['BELNR','C',35,'AN'],       # 000067-000101 IDOC document number
        ['ZEILE','C',6,'AN'],        # 000102-000107 Item number
        ['DATUM','C',8,'AN'],        # 000108-000115 IDOC: Date
        ['UZEIT','C',6,'AN'],        # 000116-000121 IDOC: Time
        ['BSARK','C',35,'AN'],       # 000122-000156 IDOC organization
        ['IHREZ','C',30,'AN'],       # 000157-000186 Your reference (Partner)
        ],
    'E1EDP03':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['IDDAT','C',3,'AN'],        # 000064-000066 Qualifier for IDOC date segment
        ['DATUM','C',8,'AN'],        # 000067-000074 Date
        ['UZEIT','C',6,'AN'],        # 000075-000080 Time
        ],
    'E1EDP19':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['QUALF','C',3,'AN'],        # 000064-000066 IDOC object identification such as material no.,customer
        ['IDTNR','C',35,'AN'],       # 000067-000101 IDOC material ID
        ['KTEXT','C',70,'AN'],       # 000102-000171 IDOC short text
        ['MFRPN','C',42,'AN'],       # 000172-000213 Manufacturer part number
        ['MFRNR','C',10,'AN'],       # 000214-000223 Manufacturer number
        ],
    'E1EDP26':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['QUALF','C',3,'AN'],        # 000064-000066 Qualifier amount
        ['BETRG','C',18,'AN'],       # 000067-000084 Total value of sum segment
        ],
    'E1EDPA1':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['PARVW','C',3,'AN'],        # 000064-000066 Partner function (e.g. sold-to party, ship-to party, ...)
        ['PARTN','C',17,'AN'],       # 000067-000083 Partner number
        ['LIFNR','C',17,'AN'],       # 000084-000100 Vendor number at customer location
        ['NAME1','C',35,'AN'],       # 000101-000135 Name 1
        ['NAME2','C',35,'AN'],       # 000136-000170 Name 2
        ['NAME3','C',35,'AN'],       # 000171-000205 Name 3
        ['NAME4','C',35,'AN'],       # 000206-000240 Name 4
        ['STRAS','C',35,'AN'],       # 000241-000275 Street and house number 1
        ['STRS2','C',35,'AN'],       # 000276-000310 Street and house number 2
        ['PFACH','C',35,'AN'],       # 000311-000345 PO Box
        ['ORT01','C',35,'AN'],       # 000346-000380 City
        ['COUNC','C',9,'AN'],        # 000381-000389 County code
        ['PSTLZ','C',9,'AN'],        # 000390-000398 Postal code
        ['PSTL2','C',9,'AN'],        # 000399-000407 P.O. Box postal code
        ['LAND1','C',3,'AN'],        # 000408-000410 Country key
        ['ABLAD','C',35,'AN'],       # 000411-000445 Unloading Point
        ['PERNR','C',30,'AN'],       # 000446-000475 Contact person's personnel number
        ['PARNR','C',30,'AN'],       # 000476-000505 Contact person's number (not personnel number)
        ['TELF1','C',25,'AN'],       # 000506-000530 1st telephone number of contact person
        ['TELF2','C',25,'AN'],       # 000531-000555 2nd telephone number of contact person
        ['TELBX','C',25,'AN'],       # 000556-000580 Telebox number
        ['TELFX','C',25,'AN'],       # 000581-000605 Fax number
        ['TELTX','C',25,'AN'],       # 000606-000630 Teletex number
        ['TELX1','C',25,'AN'],       # 000631-000655 Telex number
        ['SPRAS','C',1,'AN'],        # 000656-000656 Language key
        ['ANRED','C',15,'AN'],       # 000657-000671 Form of Address
        ['ORT02','C',35,'AN'],       # 000672-000706 District
        ['HAUSN','C',6,'AN'],        # 000707-000712 House number
        ['STOCK','C',6,'AN'],        # 000713-000718 Floor
        ['REGIO','C',3,'AN'],        # 000719-000721 Region
        ['PARGE','C',1,'AN'],        # 000722-000722 Partner's gender
        ['ISOAL','C',2,'AN'],        # 000723-000724 Country ISO code
        ['ISONU','C',2,'AN'],        # 000725-000726 Country ISO code
        ['FCODE','C',20,'AN'],       # 000727-000746 Company key (France)
        ['IHREZ','C',30,'AN'],       # 000747-000776 Your reference (Partner)
        ['BNAME','C',35,'AN'],       # 000777-000811 IDoc user name
        ['PAORG','C',30,'AN'],       # 000812-000841 IDOC organization code
        ['ORGTX','C',35,'AN'],       # 000842-000876 IDoc organization code text
        ['PAGRU','C',30,'AN'],       # 000877-000906 IDoc group code
        ['KNREF','C',30,'AN'],       # 000907-000936 Customer description of partner (plant, storage location)
        ['ILNNR','C',70,'AN'],       # 000937-001006 Character field, length 70
        ['PFORT','C',35,'AN'],       # 001007-001041 PO Box city
        ['SPRAS_ISO','C',2,'AN'],    # 001042-001043 Language according to ISO 639
        ['TITLE','C',15,'AN'],       # 001044-001058 Title
        ],
    'E1EDP05':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['ALCKZ','C',3,'AN'],        # 000064-000066 Surcharge or discount indicator
        ['KSCHL','C',4,'AN'],        # 000067-000070 Condition type (coded)
        ['KOTXT','C',80,'AN'],       # 000071-000150 Condition text
        ['BETRG','C',18,'AN'],       # 000151-000168 Fixed surcharge/discount on total gross
        ['KPERC','C',8,'AN'],        # 000169-000176 Condition percentage rate
        ['KRATE','C',15,'AN'],       # 000177-000191 Condition record per unit
        ['UPRBS','C',9,'AN'],        # 000192-000200 Price unit
        ['MEAUN','C',3,'AN'],        # 000201-000203 Unit of measurement
        ['KOBTR','C',18,'AN'],       # 000204-000221 IDoc condition end amount
        ['MENGE','C',15,'AN'],       # 000222-000236 Price scale quantity (SPEC2000)
        ['PREIS','C',15,'AN'],       # 000237-000251 Price by unit of measure (SPEC2000)
        ['MWSKZ','C',7,'AN'],        # 000252-000258 VAT indicator
        ['MSATZ','C',17,'AN'],       # 000259-000275 VAT rate
        ['KOEIN','C',3,'AN'],        # 000276-000278 Currency
        ['CURTP','C',2,'AN'],        # 000279-000280 Currency type and valuation view
        ['KOBAS','C',18,'AN'],       # 000281-000298 Base value to which condition refers
        ],
    'E1EDP04':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['MWSKZ','C',7,'AN'],        # 000064-000070 VAT indicator
        ['MSATZ','C',17,'AN'],       # 000071-000087 VAT rate
        ['MWSBT','C',18,'AN'],       # 000088-000105 Value added tax amount
        ['TXJCD','C',15,'AN'],       # 000106-000120 Tax Jurisdiction
        ['KTEXT','C',50,'AN'],       # 000121-000170 Text Field
        ],
    'E1EDP28':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['EXNUM','C',10,'AN'],       # 000064-000073 Number of foreign trade data in MM and SD documents
        ['EXPOS','C',6,'AN'],        # 000074-000079 Internal item number for foreign trade data in MM and SD
        ['STAWN','C',17,'AN'],       # 000080-000096 Commodity code / Import code number for foreign trade
        ['EXPRF','C',5,'AN'],        # 000097-000101 Export/Import procedure for foreign trade (5 digits)
        ['EXART','C',2,'AN'],        # 000102-000103 Business Transaction Type for Foreign Trade
        ['HERKL','C',3,'AN'],        # 000104-000106 Country of origin of the material
        ['HERKR','C',3,'AN'],        # 000107-000109 Region of origin of material (non-preferential origin)
        ['HERTA','C',3,'AN'],        # 000110-000112 Alternative country key for country of origin
        ['HERTI','C',15,'AN'],       # 000113-000127 Description of country of export/dispatch
        ['STXT1','C',40,'AN'],       # 000128-000167 Description of commodity code - First line
        ['STXT2','C',40,'AN'],       # 000168-000207 Description of commodity code - Second line
        ['STXT3','C',40,'AN'],       # 000208-000247 Description of commodity code - Third line
        ['STXT4','C',40,'AN'],       # 000248-000287 Description of commodity code - Fourth line
        ['STXT5','C',40,'AN'],       # 000288-000327 Description of commodity code - Fifth line
        ['STXT6','C',40,'AN'],       # 000328-000367 Description of commodity code - Sixth line
        ['STXT7','C',40,'AN'],       # 000368-000407 Description of commodity code - Seventh line
        ['BEMAS','C',5,'AN'],        # 000408-000412 Supplementary unit
        ['PREFE','C',1,'AN'],        # 000413-000413 Preference indicator in export/import
        ['BOLNR','C',35,'AN'],       # 000414-000448 Bill of lading
        ['TRATY','C',4,'AN'],        # 000449-000452 Means-of-Transport Type
        ['TRAID','C',20,'AN'],       # 000453-000472 Means of Transport ID
        ['BRULO','C',18,'AN'],       # 000473-000490 Total weight
        ['NETLO','C',18,'AN'],       # 000491-000508 Net weight
        ['VEMEH','C',3,'AN'],        # 000509-000511 Base Unit of Measure of the Quantity to be Packed (VEMNG)
        ['HERBL','C',2,'AN'],        # 000512-000513 State of manufacture
        ['BMGEW','C',18,'AN'],       # 000514-000531 Net weight
        ['TEXT1','C',40,'AN'],       # 000532-000571 Comments: Text for foreign trade processing
        ['TEXT2','C',40,'AN'],       # 000572-000611 Comments: Text for foreign trade processing
        ['TEXT3','C',40,'AN'],       # 000612-000651 Comments: Text for foreign trade processing
        ['COIMP','C',17,'AN'],       # 000652-000668 Code number for import processing in foreign trade
        ['COADI','C',6,'AN'],        # 000669-000674 Anti-dumping code for import processing in foreign trade
        ['COKON','C',6,'AN'],        # 000675-000680 Customs quota code for import processing in foreign trade
        ['COPHA','C',6,'AN'],        # 000681-000686 Pharmaceutical products code (Foreign Trade)
        ['CASNR','C',15,'AN'],       # 000687-000701 FMR category
        ['VERLD','C',3,'AN'],        # 000702-000704 Country of dispatch for Foreign Trade
        ['VERLD_TX','C',15,'AN'],    # 000705-000719 Country Name
        ['HANLD','C',3,'AN'],        # 000720-000722 Trading country for foreign trade
        ['HANLD_TX','C',15,'AN'],    # 000723-000737 Country Name
        ['EXPRF_TX','C',30,'AN'],    # 000738-000767 Description
        ['EXART_TX','C',30,'AN'],    # 000768-000797 Description
        ['GBNUM','C',20,'AN'],       # 000798-000817 Foreign Trade:Customs declaration list no. for Foreign Trade
        ['REGNR','C',20,'AN'],       # 000818-000837 Registration number for import processing in foreign trade
        ['HERSE','C',10,'AN'],       # 000838-000847 Manufacturer number for import processing in foreign trade
        ['HERKR_TX','C',20,'AN'],    # 000848-000867 Description
        ['COBLD','C',17,'AN'],       # 000868-000884 Import code no. in destination country for foreign trade
        ['EIOKA','C',1,'AN'],        # 000885-000885 EDI: Export/Import customs tariff number for foreign trade
        ['VERFA','C',8,'AN'],        # 000886-000893 Export/Import Procedure for Foreign Trade
        ['PRENC','C',1,'AN'],        # 000894-000894 Exemption certificate: Indicator for legal control
        ['PRENO','C',8,'AN'],        # 000895-000902 Exemption certificate number for legal control
        ['PREND','C',8,'AN'],        # 000903-000910 Exemption certificate: Issue date of exemption certificate
        ['BESMA','C',3,'AN'],        # 000911-000913 Supplementary unit
        ['IMPMA','C',3,'AN'],        # 000914-000916 Second unit of measurement
        ['KTNUM','C',10,'AN'],       # 000917-000926 Quota or Ceiling Number for Import Processing
        ['PLNUM','C',10,'AN'],       # 000927-000936 Quota or Ceiling Number for Import Processing
        ['WKREG','C',3,'AN'],        # 000937-000939 Region in which plant is located
        ['IMGEW','C',18,'AN'],       # 000940-000957 Net weight
        ],
    'E1EDP08':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['HLNUM','C',12,'AN'],       # 000064-000075 Hierarchy number
        ['PARENT','C',12,'AN'],      # 000076-000087 Hierarchical parent ID
        ['LEVEL','C',12,'AN'],       # 000088-000099 Pack/subpack level ID
        ['EXIDV','C',45,'AN'],       # 000100-000144 External shipping unit ID
        ['VENUM','C',10,'AN'],       # 000145-000154 Internal Handling Unit Number
        ['VEMEH','C',3,'AN'],        # 000155-000157 Base Unit of Measure of the Quantity to be Packed (VEMNG)
        ['PCKAR','C',35,'AN'],       # 000158-000192 Packing type
        ['PCKNR','C',35,'AN'],       # 000193-000227 Customer number of shipping unit
        ['ANZAR','C',15,'AN'],       # 000228-000242 Number of products per shipping unit
        ['VBELN','C',35,'AN'],       # 000243-000277 Delivery
        ['POSNR','C',30,'AN'],       # 000278-000307 Delivery item
        ['BTGEW','C',18,'AN'],       # 000308-000325 Total weight
        ['NTGEW','C',18,'AN'],       # 000326-000343 Net weight
        ['TARAG','C',18,'AN'],       # 000344-000361 Tare weight of shipping unit
        ['GEWEI','C',3,'AN'],        # 000362-000364 Weight unit
        ['BTVOL','C',18,'AN'],       # 000365-000382 Total volume of shipping unit
        ['NTVOL','C',18,'AN'],       # 000383-000400 Loading volume of shipping unit
        ['TAVOL','C',18,'AN'],       # 000401-000418 Tare volume of shipping unit
        ['VOLEH','C',3,'AN'],        # 000419-000421 Volume unit
        ['LAENG','C',18,'AN'],       # 000422-000439 Length
        ['BREIT','C',18,'AN'],       # 000440-000457 Width
        ['HOEHE','C',18,'AN'],       # 000458-000475 Height
        ['MEABM','C',3,'AN'],        # 000476-000478 Unit for length/width/height
        ['MEINS','C',3,'AN'],        # 000479-000481 Base unit of measure
        ['VSTEL','C',17,'AN'],       # 000482-000498 Shipping point
        ['LSTEL','C',17,'AN'],       # 000499-000515 Loading point
        ['PKNRS','C',1,'AN'],        # 000516-000516 Shipment number key for VDA/Odette
        ],
    'E1EDP30':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['QUALF','C',3,'AN'],        # 000064-000066 IDOC qualifier reference document
        ['IVKON','C',30,'AN'],       # 000067-000096 30 Characters
        ],
    'E1EDPT1':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['TDID','C',4,'AN'],         # 000064-000067 Text ID
        ['TSSPRAS','C',3,'AN'],      # 000068-000070 Language Key
        ['TSSPRAS_ISO','C',2,'AN'],  # 000071-000072 Language according to ISO 639
        ],
    'E1EDPT2':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['TDLINE','C',70,'AN'],      # 000064-000133 Text line
        ['TDFORMAT','C',2,'AN'],     # 000134-000135 Tag column
        ],
    'E1EDS01':[
        ['BOTSID','C',30,'AN'],      # 000001-000030 Segment (external name)
        ['MANDT','C',3,'AN'],        # 000031-000033 Client
        ['DOCNUM','C',16,'AN'],      # 000034-000049 IDoc number
        ['SEGNUM','C',6,'AN'],       # 000050-000055 Segment Number
        ['PSGNUM','C',6,'AN'],       # 000056-000061 Number of superior parent segment
        ['HLEVEL','C',2,'AN'],       # 000062-000063 Hierarchy level of SAP segment
        ['SUMID','C',3,'AN'],        # 000064-000066 Qualifier for totals segment for shipping notification
        ['SUMME','C',18,'AN'],       # 000067-000084 Total value of sum segment
        ['SUNIT','C',3,'AN'],        # 000085-000087 Total value unit for totals segment in the shipping notif.
        ['WAERQ','C',3,'AN'],        # 000088-000090 Currency
        ],
    }

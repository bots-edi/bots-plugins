from bots.botsconfig import *

syntax = { 
        'indented': True,
        }

structure=    [
    {ID:'message',MIN:1,MAX:1,
    QUERIES:{
        'frompartner':  {'BOTSID':'message','sender':None},
        'topartner':    {'BOTSID':'message','receiver':None},
        #~ 'testindicator':{'BOTSID':'message','testindicator':None},
        },
    LEVEL:[
        {ID:'partys',MIN:1,MAX:1,LEVEL:[
            {ID:'party',MIN:1,MAX:99},
            ]},
        {ID:'cpss',MIN:1,MAX:1,LEVEL:[
            {ID:'cps',MIN:1,MAX:9999,LEVEL:[
                {ID:'pacs',MIN:0,MAX:1,LEVEL:[
                    {ID:'pac',MIN:1,MAX:9999,LEVEL:[
                        {ID:'hans',MIN:0,MAX:1,LEVEL:[
                            {ID:'han',MIN:1,MAX:99},
                            ]},
                        ]},
                    ]},
                {ID:'lines',MIN:0,MAX:1,LEVEL:[
                    {ID:'line',MIN:1,MAX:99999,LEVEL:[
                        {ID:'hans',MIN:0,MAX:1,LEVEL:[
                            {ID:'han',MIN:1,MAX:99},
                            ]},
                        ]},
                    ]},
                ]},
            ]},
        ]},
    ]

recorddefs = {
    'envelope':[
            ['BOTSID','M',255,'A'],
          ],
    'message':[
            ['BOTSID','M',255,'A'],
            ['sender', 'M', 35, 'AN'],  #
            ['receiver', 'M', 35, 'AN'],    #EAN adrescode geadresseerde
            ['testindicator', 'C', 3, 'AN'],     #Indicatie test
            ['docsrt', 'C', 3, 'AN'],
            ['docnum', 'C', 17, 'AN'],  #Verzendberichtnummer 
            ['docdtm', 'C', 35, 'AN'],  #Berichtdatum 
            ['despatchdtm', 'C', 35, 'AN'],
            ['deldtm', 'C', 35, 'AN'],      #Geplande afleverdatum
            ['earldeldtm', 'C', 35, 'AN'],  #Vroegste afleverdatum
            ['latedeldtm', 'C', 35, 'AN'],  #Laatste afleverdatum
            ['askeddeldtm', 'C', 35, 'AN'], #Gevraagde afleverdatum
            ['byordnum', 'C', 17, 'AN'],    #Ordernummer afnemer
            ['suordnum', 'C', 17, 'AN'],
            ['suorddtm', 'C', 35, 'AN'],
          ],
    'partys':[
            ['BOTSID','M',255,'A'],
          ],
    'party':[
            ['BOTSID','M',255,'A'],
            ['qual', 'C', 17, 'AN'],            #party type: BY=buyer, DO=delivery place, SU=Supplier, IV=invoice address
            ['gln', 'C', 13, 'AN'],             #GLN number identifying the party
            ['name1', 'C', 70, 'AN'],
            ['name2', 'C', 70, 'AN'],
            ['address1', 'C', 70, 'AN'],
            ['address2', 'C', 70, 'AN'],
            ['address3', 'C', 70, 'AN'],
            ['city', 'C', 70, 'AN'],
            ['state', 'C', 35, 'AN'],
            ['pcode', 'C', 17, 'AN'],
            ['country', 'C', 3, 'AN'],
            ['vatnum', 'C', 17, 'AN'],          #vat  number
            ['internalID', 'C', 17, 'AN'],
            ['externalID', 'C', 17, 'AN'],
            ['iban', 'C', 17, 'AN'],
            ['bic', 'C', 17, 'AN'],
          ],
    'lines':[
            ['BOTSID','M',255,'A'],
          ],
    'line':[
            ['BOTSID','M',255,'A'],
            ['num', 'M', 6, 'AN'],      #Regelnummer
            ['gtin', 'C', 14, 'AN'],    #EAN-artikelcode
            ['ordqua', 'C', 20, 'R'],
            ['ordunit', 'C', 3, 'AN'],
            ['delqua', 'C', 20, 'R'],   #Aantal geleverd
            ['freequa', 'C', 20, 'R'],
            ['suart', 'C', 17, 'AN'],
            ['byart', 'C', 17, 'AN'],
            ['desc', 'C', 35, 'AN'],
            ['productiondtm', 'C', 35, 'AN'],
            ['bestbeforedtm', 'C', 35, 'AN'],   #THT-datum
            ['expirydtm', 'C', 35, 'AN'],
            ['batchnum', 'C', 17, 'AN'],     #Batchnummer
            ['batchnumpac', 'C', 17, 'AN'],
            ['serialnum', 'C', 17, 'AN'],
            ['netweight', 'C', 20, 'R'],
            ['brutweight', 'C', 20, 'R'],
            ['brutvolume', 'C', 20, 'R'],
          ],
    'pacs':[
            ['BOTSID','M',255,'A'],
          ],
    'pac':[
            ['BOTSID','M',255,'A'],
            ['qua', 'C', 8, 'AN'],  #Aantal verzendeenheden
            ['iso', 'C', 3, 'AN'],  #ISO-code soort verzendeenheid
            ['gtin', 'C', 14, 'AN'],    #EAN artikelcode soort verzendeenheid
            ['sscc', 'C', 20, 'AN'],
            ['brutweight', 'C', 20, 'R'],
            ['brutvolume', 'C', 20, 'R'],
            ['width', 'C', 20, 'R'],
            ['length', 'C', 20, 'R'],
            ['height', 'C', 20, 'R'],
            ['textpalletlabel', 'C', 35, 'AN'],
          ],
    'cpss':[
            ['BOTSID','M',255,'A'],
          ],
    'cps':[
            ['BOTSID','M',255,'A'],
            ['line', 'C', 17, 'AN'],
            ['subline', 'C', 17, 'AN'],
          ],
    'hans':[
            ['BOTSID','M',255,'A'],
          ],
    'han':[
            ['BOTSID','M',255,'A'],
            ['instruction', 'C', 3, 'AN'],
            ['adr', 'C', 3, 'AN'],
          ],
     }
 

from bots.botsconfig import *

syntax = { 
        'indented': True,
        }

structure = [
    {ID:'message',MIN:1,MAX:1,
    QUERIES:{
        'frompartner':  {'BOTSID':'message','sender':None},
        'topartner':    {'BOTSID':'message','receiver':None},
        #~ 'testindicator':{'BOTSID':'message','testindicator':None},
        },
    LEVEL:[
        {ID:'subs',MIN:0,MAX:1,LEVEL:[
            {ID:'sub',MIN:1,MAX:9},
            ]},
        {ID:'alcs',MIN:0,MAX:1,LEVEL:[
            {ID:'alc',MIN:1,MAX:99},
            ]},
        {ID:'partys',MIN:0,MAX:1,LEVEL:[
            {ID:'party',MIN:1,MAX:99},
            ]},
        {ID:'lines',MIN:0,MAX:1,LEVEL:[
            {ID:'line',MIN:1,MAX:99999,LEVEL:[
                {ID:'alcs',MIN:0,MAX:1,LEVEL:[
                    {ID:'alc',MIN:1,MAX:99},
                    ]},
                ]},
            ]},
        ]
    }
]
    

recorddefs = {
    'message':[
            ['BOTSID','M',255,'A'],
            ['sender', 'M', 35, 'AN'],
            ['receiver', 'M', 35, 'AN'],
            ['testindicator', 'C', 3, 'AN'],
            ['docsrt', 'C', 3, 'AN'],
            ['docnum', 'M', 35, 'AN'],
            ['docdtm', 'C', 35, 'AN'],
            ['deldtm', 'C', 35, 'AN'],
            ['currency', 'C', 3, 'AN'],
            ['byordnum', 'C', 17, 'AN'],    #Order number 
            ['byorddtm', 'C', 35, 'AN'],
            ['suordnum', 'C', 17, 'AN'],
            ['suorddtum', 'C', 35, 'AN'],
            ['sudesnum', 'C', 17, 'AN'],    #delivery not number 
            ['sudesdtm', 'C', 35, 'AN'],
            ['oriinvoicnum', 'C', 17, 'AN'],    #original invoice (theat is corrected/changed
            ['netmon', 'C', 20, 'R'],   #total net amount (add net line amounts)
            ['alcmon', 'C', 20, 'R'],   #total amount invoice charges/allowances
            ['vatmon', 'C', 20, 'R'],   #total amount vat
            ['vatbasemon', 'C', 20, 'R'],   #base amoutn for vat
            ['invmon', 'C', 20, 'R'],   #invoice amount
            ['vatper', 'C', 20, 'R'],   #vat percentage
            ['vatrate', 'C', 17, 'A'],   #E (exempt) or S (standard)
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
            ['linenum', 'C', 6, 'AN'],
            ['gtin', 'C', 14, 'AN'],
            ['suart', 'C', 35, 'AN'],
            ['byart', 'C', 35, 'AN'],
            ['ordqua', 'C', 20, 'R'],
            ['ordunit', 'C', 3, 'AN'],
            ['desc', 'C', 70, 'AN'],
            ['freequa', 'C', 20, 'R'],
            ['invqua', 'C', 20, 'R'],   #invoice quantity
            ['delqua', 'C', 20, 'R'],   #delivered quantity
            ['delunit', 'C', 3, 'AN'],
            ['pricebrut', 'C', 20, 'R'],
            ['pricenet', 'C', 20, 'R'],    #net price
            ['priunit', 'C', 3, 'AN'],
            ['netmon', 'C', 20, 'R'],   #Net line amount (net_price * invoiced quantity)
            ['vatper', 'C', 20, 'R'],   #vat percentage
            ['vatrate', 'C', 17, 'A'],   #E (exempt) or S (standard)
          ],
    'alcs':[
            ['BOTSID','M',255,'A'],
          ],
    'alc':[
            ['BOTSID','M',255,'A'],
            ['sign', 'C', 3, 'AN'],
            ['srt', 'C', 3, 'AN'],
            ['mon', 'C', 20, 'R'],
            ['basemon', 'C', 20, 'R'],
            ['per', 'C', 20, 'R'],
            ['calculationsequence', 'C', 17, 'AN'],
            ['vatper', 'C', 20, 'R'],   #vat percentage
            ['vatrate', 'C', 17, 'A'],   #E (exempt) or S (standard)
          ],
    'subs':[
            ['BOTSID','M',255,'A'],
          ],
    'sub':[
            ['BOTSID','M',255,'A'],
            ['vatper', 'C', 20, 'R'],   #vat percentage
            ['vatrate', 'C', 3, 'AN'],   #E (exempt) or S (standard)
            ['vatbasemon', 'C', 20, 'R'],   #BTW-grondslagbedrag
            ['vatmon', 'C', 20, 'R'],   #BTW-bedrag
          ],
     }
 

from bots.botsconfig import *

syntax = { 
        'indented':True,
        }

structure = [
    {ID:'message',MIN:1,MAX:1,
    QUERIES:{
        'frompartner':  {'BOTSID':'message','sender':None},
        'topartner':    {'BOTSID':'message','receiver':None},
        'testindicator':{'BOTSID':'message','testindicator':None},
        },
    LEVEL:[
        {ID:'partys',MIN:0,MAX:1,LEVEL:[
            {ID:'party',MIN:1,MAX:99},
            ]},
        {ID:'orders',MIN:0,MAX:1,LEVEL:[
            {ID:'order',MIN:1,MAX:99999,LEVEL:[
                {ID:'lines',MIN:0,MAX:1,LEVEL:[
                    {ID:'line',MIN:1,MAX:99999},
                    ]},
                ]},
            ]},
        ]},
    ]

recorddefs = {
    'message':[
            ['BOTSID','M',255,'A'],
            ['sender', 'M', 35, 'AN'],
            ['receiver', 'M', 35, 'AN'],
            ['testindicator', 'C', 3, 'AN'],
            ['docnum', 'M', 35, 'AN'],
            ['docdtm', 'C', 35, 'AN'],
            ['doctime', 'C', 35, 'AN'],
            ['deldtm', 'C', 35, 'AN'],
            ['shipdtm', 'C', 35, 'AN'],
            ['scac', 'C', 4, 'AN'],
            ['bol', 'C', 35, 'AN'],
            ['carrierreferencenumber', 'C', 35, 'AN'],
          ],
    'partys':[
            ['BOTSID','M',255,'A'],
          ],
    'party':[
            ['BOTSID','M',255,'A'],
            ['qual', 'C', 3, 'AN'],
            ['gln', 'C', 13, 'AN'],
            ['DUNS', 'C', 13, 'AN'],
            ['internalID', 'C', 17, 'AN'],
            ['externalID', 'C', 17, 'AN'],
            ['name1', 'C', 70, 'AN'],
            ['name2', 'C', 70, 'AN'],
            ['address1', 'C', 70, 'AN'],
            ['address2', 'C', 70, 'AN'],
            ['city', 'C', 70, 'AN'],
            ['pcode', 'C', 17, 'AN'],
            ['state', 'C', 35, 'AN'],
            ['country', 'C', 3, 'AN'],
          ],
    'orders':[
            ['BOTSID','M',255,'A'],
          ],
    'order':[
            ['BOTSID','M',255,'A'],
            ['ordernumber', 'C', 35, 'AN'],
            ['orderdtm', 'C', 35, 'AN'],
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
            ['delqua', 'C', 20, 'R'],
            ['ordqua', 'C', 20, 'R'],
            ['desc', 'C', 70, 'AN'],
            ['sscc', 'C', 35, 'AN'],        #per line is the sscc of the package it is in indicated. In mapping this is rearrangent in HL levels shipment-order-pack-line item
          ],
     }
 

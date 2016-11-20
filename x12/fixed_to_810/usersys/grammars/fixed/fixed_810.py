from bots.botsconfig import *

syntax = { 
        'charset'     : 'iso-8859-1',
        'checkfixedrecordtooshort': True,
        }

nextmessage = ({'BOTSID':'HEA'},)

structure=    [
    {ID:'HEA',MIN:1,MAX:10000,
        QUERIES:{
            'frompartner':  {'BOTSID':'HEA','EANZENDER':None},
            'topartner':    {'BOTSID':'HEA','EANONTVANGER':None},
            'topartnerq':   {'BOTSID':'HEA','PARTNERQUA':None},
            'reference':    {'BOTSID':'HEA','INVOICE':None},
            'testindicator':{'BOTSID':'HEA','TEST':None}},
        LEVEL:[
            {ID:'LIN',MIN:0,MAX:10000},
            ]},
    ]

recorddefs = {
    'HEA':[
            ['BOTSID','C',3,'A'],    #pos 1
            ['SOORT', 'C', 1, 'A'],    #pos 4
            ['TEST', 'C', 1, 'AN'],    #pos 5
            ['EANZENDER', 'C', 11, 'AN'],    #pos 6
            ['PARTNERQUA', 'C', 2, 'AN'],    #pos 17
            ['EANONTVANGER', 'C', 13, 'AN'],    #pos 19
            ['ORDERNUMMER', 'C', 29, 'AN'],    #pos 32
            ['ORDERDATUM', 'C', 10, 'AN'],    #pos 61
            ['INVOICE', 'C', 21, 'AN'],    #pos 71
            ['SHIPMETHOD', 'C', 12, 'AN'],    #pos 92
            ['SHIPACCOUNT', 'C', 12, 'AN'],    #pos 104
            ['PODATE', 'C', 10, 'AN'],    #pos 116
            ['SHIPTONAME', 'C', 22, 'AN'],    #pos 126
            ['SHIPTOADDRESS1', 'C', 25, 'AN'],    #pos 148
            ['SHIPTOADDRESS2', 'C', 20, 'AN'],    #pos 173
            ['SHIPTOADDRESS3', 'C', 20, 'AN'],    #pos 193
            ['CITY', 'C', 15, 'AN'],    #pos 213
            ['STATE', 'C', 2, 'AN'],    #pos 228
            ['ZIP', 'C', 10, 'AN'],    #pos 230
            ['COUNTRY', 'C', 1, 'AN'],    #pos 240
          ],
    'LIN':[
            ['BOTSID','C',3,'A'],    #pos 1
            ['FILLER3', 'C', 2, 'AN'],    #pos 4
            ['ISBN', 'C', 13, 'AN'],    #pos 6
            ['FILLER4', 'C', 9, 'AN'],    #pos 19
            ['QUANTITY', 'C', 4, 'N'],    #pos 28
            ['FILLER5', 'C', 24, 'AN'],    #pos 32
            ['LISTPRICE', 'C', 5.2, 'N'],    #pos 56
            ['FORMAT', 'C', 4, 'AN'],    #pos 61
            ['FILLER6', 'C', 6, 'AN'],    #pos 65
            ['TITLE', 'C', 22, 'AN'],    #pos 71
            ['FILLER7', 'C', 148, 'AN'],  #pos 133
          ],
    }

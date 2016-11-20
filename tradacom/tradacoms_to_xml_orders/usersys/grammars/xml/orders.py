from bots.botsconfig import *

nextmessage = ({'BOTSID':'envelope'},)

syntax = { 
        'indented':True,               #False: xml output is one string (no cr/lf); True: xml output is indented/human readable
        }

structure=    [
{ID:'envelope',MIN:1,MAX:1,
    QUERIES:{
        'frompartner':  ({'BOTSID':'envelope'},{'BOTSID':'message','sender':None}),
        'topartner':    ({'BOTSID':'envelope'},{'BOTSID':'message','receiver':None}),
        },
    LEVEL:[
    {ID:'message',MIN:1,MAX:9999,
    QUERIES:{
        'frompartner':  {'BOTSID':'message','sender':None},
        'topartner':    {'BOTSID':'message','receiver':None},
        'referenceunb': {'BOTSID':'message','envid':None},
        'intdtm':       {'BOTSID':'message','envdtm':None},
        'testindicator':{'BOTSID':'message','test':None},
        },
    LEVEL:[
        {ID:'partys',MIN:0,MAX:1,LEVEL:[
            {ID:'party',MIN:1,MAX:999},
            ]},
        {ID:'txts',MIN:0,MAX:1,LEVEL:[
            {ID:'txt',MIN:1,MAX:999},
            ]},
        {ID:'bilas',MIN:0,MAX:1,LEVEL:[
            {ID:'bila',MIN:1,MAX:999},
            ]},
        {ID:'lines',MIN:0,MAX:1,LEVEL:[
            {ID:'line',MIN:1,MAX:99999,LEVEL:[
                {ID:'pris',MIN:0,MAX:1,LEVEL:[
                    {ID:'pri',MIN:1,MAX:999},
                    ]},
                {ID:'alcs',MIN:0,MAX:1,LEVEL:[
                    {ID:'alc',MIN:1,MAX:999},
                    ]},
                {ID:'txts',MIN:0,MAX:1,LEVEL:[
                    {ID:'txt',MIN:1,MAX:999},
                    ]},
                {ID:'bilas',MIN:0,MAX:1,LEVEL:[
                    {ID:'bila',MIN:1,MAX:999},
                    ]},
                {ID:'ucs',MIN:0,MAX:1,LEVEL:[
                    {ID:'uc',MIN:1,MAX:9999},
                    ]},
                ]},
            ]},
        ]},
    ]}
]

recorddefs = {
    'envelope':[
            ['BOTSID','M',255,'A'],
          ],
    'message':[
            ['BOTSID','M',255,'A'],
            ['sender', 'M', 35, 'AN'],
            ['senderqua', 'C', 3, 'AN'],    #qualifier for sender
            ['sendername', 'C', 35, 'AN'],    #tradacoms
            ['receiver', 'M', 35, 'AN'],
            ['receiverque', 'C', 35, 'AN'], #qualifier for receiver
            ['receivername', 'C', 35, 'AN'],    #tradacoms
            ['envid', 'C', 14, 'AN'],   #id of envelope
            ['envdtm', 'C', 35, 'AN'],  #including time. Format: CCJJMMDDHHMM(SS). 
            ['applref', 'C', 35, 'AN'],  #application reference
            ['priority', 'C', 1, 'AN'],
            ['test', 'C', 3, 'AN'],     #indicate test/production
            ['orgeditype', 'M', 35, 'AN'],    #editype originally received
            ['orgmessagetype', 'M', 35, 'AN'],    #type of message that was orginally received
            ['type', 'M', 35, 'AN'],    #type of xml message
            ['version', 'M', 35, 'AN'], #version of xml message...just in case...
            ['docsrt', 'C', 4, 'AN'],   #coded 'subtype' of the message. Eg rush order, credit invoice.  
            ['mesfunc', 'C', 12, 'AN'],  #coded messagefunction/sub-sub-type. edifact tradacoms
            ['classification', 'C', 3, 'AN'],  #coded order classification  tradacoms
            ['orcd', 'C', 3, 'AN'],  #coded order code  tradacoms
            ['mesnum', 'C', 17, 'AN'],  #ID of message (not of document); anly used in EDI. Tradacoms: sequential per trading partner, messagetype
            ['docnum', 'C', 17, 'AN'],  #like invoice number, order number. Internal ID.
            ['docnumvv', 'C', 17, 'AN'],  #order number of supplier.
            ['messrtbil', 'C', 35, 'AN'],
            ['docack', 'C', 3, 'AN'],   #inforamtion about document acknowledgement
            ['docdtm', 'C', 35, 'AN'],  #format EEJJMMDD(HHMM(SS))
            ['docdtmvv', 'C', 35, 'AN'],  #format EEJJMMDD(HHMM(SS))
            ['deldtm', 'C', 35, 'AN'],      #delivery date/time; 
            ['earldeldtm', 'C', 35, 'AN'],  #earliest delivery date/time
            ['latedeldtm', 'C', 35, 'AN'],  #latest delivery date/time
            ['deltimefrom', 'C', 35, 'AN'],  #delivery time from; format UUMM(SS)
            ['deltimetill', 'C', 35, 'AN'],  #delivery time till; format UUMM(SS)
            ['hauldtm', 'C', 35, 'AN'],     #date/ime for backhauling
            ['scenariocode', 'C', 3, 'AN'], 
            ['fullorderind', 'C', 3, 'AN'],
            ['newshopind', 'C', 3, 'AN'],   #order for new shop
            ['nullind', 'C', 3, 'AN'],  #null-orders: no order lines/no delivery expected
            ['rushind', 'C', 3, 'AN'],  #rush order
            ['haulind', 'C', 3, 'AN'],  #backhauling; goods are hauled by buyer
            ['dutyfreeind', 'C', 3, 'AN'],
            ['pdnum', 'C', 17, 'AN'],       #promotional deal number
            ['blanketnum', 'C', 17, 'AN'],  #blanket order number
            ['contractnum', 'C', 17, 'AN'], #contact number
            ['projectnum', 'C', 17, 'AN'],  #project number
            ['customernum', 'C', 17, 'AN'],
            ['currency', 'C', 3, 'AN'],
            ['payduedtm', 'C', 35, 'AN'],
            ['paydiscqua', 'C', 3, 'AN'],
          ],
    'partys':[
            ['BOTSID','M',255,'A'],
          ],
    'party':[
            ['BOTSID','M',255,'A'],
            ['qual', 'C', 17, 'AN'],
            ['gln', 'C', 13, 'AN'],
            ['name', 'C', 40, 'AN'],
            ['addressline1', 'C', 35, 'AN'],
            ['addressline2', 'C', 35, 'AN'],
            ['addressline3', 'C', 35, 'AN'],
            ['addressline4', 'C', 35, 'AN'],
            ['street', 'C', 35, 'AN'],
            ['city', 'C', 35, 'AN'],
            ['pcode', 'C', 9, 'AN'],
            ['country', 'C', 3, 'AN'],
            ['bilnum', 'C', 17, 'AN'],
            ['vatnum', 'C', 17, 'AN'],
            ['intcustomernum', 'C', 17, 'AN'],
            ['namecontact', 'C', 35, 'AN'],
            ['phonecontact', 'C', 35, 'AN'],
            ['iban', 'C', 17, 'AN'],
            ['bic', 'C', 17, 'AN'],
          ],
    'txts':[
            ['BOTSID','M',255,'A'],
          ],
    'txt':[
            ['BOTSID','M',255,'A'],
            ['qual', 'C', 17, 'AN'],
            ['val', 'C', 70, 'AN'],
          ],
    'bilas':[
            ['BOTSID','M',255,'A'],
          ],
    'bila':[
            ['BOTSID','M',255,'A'],
            ['qual', 'M', 17, 'AN'],
            ['val', 'C', 40, 'AN'],
          ],
    'lines':[
            ['BOTSID','M',255,'A'],
          ],
    'line':[
            ['BOTSID','M',255,'A'],
            ['num', 'M', 6, 'AN'],
            ['gtin', 'C', 14, 'AN'],
            ['suart', 'C', 17, 'AN'],
            ['byart', 'C', 17, 'AN'],
            ['gtincu', 'C', 14, 'AN'],
            ['numbergtincu', 'C', 14, 'AN'],
            ['ordqua', 'C', 20, 'R'],
            ['ordunit', 'C', 3, 'AN'],
            ['desc', 'C', 40, 'AN'],
            ['contractnum', 'C',17, 'AN'],
            ['customernum', 'C', 17, 'AN'],
            ['pdnum', 'C', 17, 'AN'],
            ['deldtm', 'C', 35, 'AN'],
            ['earldeldtm', 'C', 35, 'AN'],
            ['latedeldtm', 'C', 35, 'AN'],
            ['seize', 'C', 35, 'AN'],
            ['colour', 'C', 35, 'AN'],
            ['colourcodelist', 'C', 35, 'AN'],
            ['stylecode', 'C', 35, 'AN'],
            ['minshelflifedtm', 'C', 35, 'AN'],
            ['minshelflifefrmt', 'C', 35, 'AN'],
            ['length', 'C', 20, 'R'],
            ['width', 'C', 20, 'R'],
            ['height', 'C', 20, 'R'],
            ['europeanwastecatalogue', 'C', 20, 'AN'],
            ['exactdeliveryind', 'C', 3, 'AN'],
            ['numoflayers', 'C', 20, 'R'],
            ['numofunitsperlayer', 'C', 20, 'R'],
            ['vatper', 'C', 20, 'R'],
            ['netmon', 'C', 20, 'R'],
          ],
    'pris':[
            ['BOTSID','M',255,'A'],
          ],
    'pri':[
            ['BOTSID','M',255,'A'],
            ['qual', 'C', 3, 'AN'],
            ['price', 'C', 20, 'R'],
            ['type', 'C', 3, 'AN'],
            ['qua', 'C', 20, 'R'],
            ['unit', 'C', 3, 'AN'],
            ['currency', 'C', 3, 'AN'],
          ],
    'alcs':[
            ['BOTSID','M',255,'A'],
          ],
    'alc':[
            ['BOTSID','M',255,'A'],
            ['sign', 'C', 3, 'AN'],
            ['mon', 'C', 20, 'R'],
            ['per', 'C', 20, 'R'],
            ['calculationsequence', 'C', 17, 'AN'],
          ],
    'ucs':[
            ['BOTSID','M',255,'A'],
          ],
    'uc':[
            ['BOTSID','M',255,'A'],
            ['gln', 'C', 35, 'AN'],
            ['ordqua', 'C', 20, 'R'],
          ],
     }
 

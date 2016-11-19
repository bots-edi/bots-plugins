from bots.botsconfig import *

#syntax: parameters for translation. 
syntax = { 
        'charset'     : 'us-ascii',
        }

#structure: the sequence of the records, and min/max repeats. Records can be 'nested'
structure=    [
    {ID:'HEA',MIN:1,MAX:10000,LEVEL:[       #LEVEL is used to indicate that the 'LIN' record is nested under the 'HEA' record
        {ID:'LIN',MIN:0,MAX:10000},         #line record
        ]},
    ]
    

#the fields in each record. 'BOTSID' is the record tag.
recorddefs = {
    'HEA':[                                         #header record
            ['BOTSID','C',3,'A'],
            ['MESSAGETYPE', 'M', 20, 'AN'],         #field 'MESSAGETYPE' is Mandatory, amx 20 positions, and alphanumeric
            ['SENDER', 'C', (13,13), 'N'],         #field 'SENDER' is Conditional, min 13, max 13 and Numeric
            ['RECEIVER', 'C', 13, 'AN'],         
            ['ORDERNUMBER', 'C', 17, 'AN'],         
            ['ORDERDATE', 'C', 12, 'AN'],          
            ['ORDERTYPE', 'C', 3, 'AN'],          
            ['BUYER_ID', 'C', 13, 'AN'],         
            ['SUPPLIER_ID', 'C', 13, 'AN'],         
            ['DELIVERYPLACE_ID', 'C', 13, 'AN'],         
            ['DELIVERY_DATE', 'C', 12, 'AN'],          
          ],
    'LIN':[                                         #line record
            ['BOTSID','C',3,'A'],
            ['LINENUMBER', 'C', 6, 'N'],         
            ['ARTICLE_GTIN', 'C', 14, 'AN'],         
            ['DESCRIPTION', 'C', 35, 'AN'],         
            ['QUANTITY', 'C', 16.3, 'N'],           #quantity is ALWAYS 16 positions; it is written with 3 decimals and included the decimal sign;
          ],
    }
     

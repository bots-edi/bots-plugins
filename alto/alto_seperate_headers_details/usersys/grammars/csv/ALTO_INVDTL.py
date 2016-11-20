# Grammar for Alto Invoice Detail
# Mike Griffin 25/02/2010

from bots.botsconfig import *

syntax = {
        'field_sep':',',
        'quote_char':'"',
        'charset':"us-ascii",
        'merge':True,
        'noBOTSID':True
        }

structure = [
    {ID:'DTL',MIN:1,MAX:99999}
    ]

nextmessageblock = ({'BOTSID':'DTL','INVNUM':None})

recorddefs = {
    'DTL':[
            ['BOTSID','C', 3, 'A'],
            ['INVNUM', 'C', 10, 'A'], # Invoice number
            ['INVLIN', 'C', 4, 'A'],  # Line number
            ['INVQTY', 'C', 10, 'R'], # Quantity
            ['PRCPER', 'C', 15, 'R'], # Price per 1
            ['TOTAMT', 'C', 15, 'R'], # Total amount exc GST
            ['MATNUM', 'C', 15, 'A'], # Material number
          ],
     }

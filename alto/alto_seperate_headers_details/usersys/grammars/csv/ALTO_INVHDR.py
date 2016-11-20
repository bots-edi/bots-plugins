# Grammar for Alto Invoice Header
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
    {ID:'HDR',MIN:1,MAX:99999}
    ]

nextmessageblock = ({'BOTSID':'HDR','INVNUM':None})

recorddefs = {
    'HDR':[
            ['BOTSID','C', 3, 'A'],
            ['INVNUM', 'C', 10, 'A'],    # Invoice number
            ['BCHNUM', 'C', 10, 'A'],    # Batch number
            ['DATEFMT', 'C', 10, 'A'],   # Date format (CCYYMMDD)
            ['BCHDATE', 'C', 8, 'A'],    # Batch date
            ['INVDATE', 'C', 8, 'A'],    # Invoice date
            ['ORDNUM', 'C', 10, 'A'],    # Purchase order number
            ['TOTEXCGST', 'C', 15, 'R'], # Total amount exc GST
            ['TOTGSTAMT', 'C', 15, 'R'], # Total GST amount
            ['TOTINCGST', 'C', 15, 'R'], # Total amount inc GST
          ],
     }

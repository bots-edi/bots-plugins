from bots.botsconfig import *

syntax = { 
        'field_sep': ';',
        'quote_char':'"',
        'decimaal':',',
        'noBOTSID':True,
        'charset':'iso-8859-1',
        }

structure=    [
    {ID:'SLS',MIN:1,MAX:10000},
    ]

recorddefs = {
    'SLS':[
            ['BOTSID','M',3,'A'],
            ['SLSRPTDATUM', 'C', 12, 'AN'],
            ['EANFILIAAL', 'C', 35, 'AN'],
            ['EANARTIKEL', 'C', 14, 'AN'],
            ['AANTAL', 'C', 16.0, 'N'],
            ['PRICE', 'C', 16.3, 'N'],
          ],
    }

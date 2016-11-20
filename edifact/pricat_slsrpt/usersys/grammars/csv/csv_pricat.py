from bots.botsconfig import *

syntax = { 
        'field_sep': ';',
        'quote_char':'"',
        'decimaal':',',
        'noBOTSID':True,
        'skip_firstline':True,
        'charset':'iso-8859-1',
        }


structure=    [
    {ID:'PRI',MIN:1,MAX:10000},
    ]
    
nextmessageblock = ({'BOTSID':'PRI','NEP1':None})

recorddefs = {
    'PRI':[
            ['BOTSID','C',3,'A'],
            ['EANARTIKEL', 'C', 35, 'AN'],
            ['SUARTIKEL', 'C', 35, 'AN'],
            ['OMSCHRIJVING', 'C', 35, 'AN'],
            ['MAAT', 'C', 35, 'AN'],
            ['KLEUR', 'C', 35, 'AN'],
            ['BUYERPRODUCTGROUP', 'C', 35, 'AN'],
            ['VERKPRI', 'C', 16, 'R'],
            ['DATUMVANAF', 'C', 35, 'AN'],
            ['PROPRI', 'C', 16, 'R'],
            ['DATUMTOT', 'C', 35, 'AN'],
            ['NEP1', 'C', 35, 'AN'],    #excel seems to put another (empty) field after the last one....
            ['NEP2', 'C', 35, 'AN'],    #excel seems to put another (empty) field after the last one....
          ],
    }

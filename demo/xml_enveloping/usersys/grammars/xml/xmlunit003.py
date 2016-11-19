from bots.botsconfig import *

syntax = {
        'indented':True,               #False: xml output is one string (no cr/lf); True: xml output is indented/human readable
        'charset':'utf-8',
        'merge': True,
        'envelope': 'myxmlenvelopunit003',
        }


structure=    [
{ID:'HEA',MIN:1,MAX:10000,LEVEL:[
        {ID:'LIN',MIN:0,MAX:10000},
        ]},
]

nextmessage = ({'BOTSID':'HEA'},)

    
recorddefs = {
    'HEA':[
            ['BOTSID','C',3,'A'],
            ['SOORT', 'C', 20, 'AN'],          
            ['EANZENDER', 'C', 13, 'AN'],         
            ['EANONTVANGER', 'C', 13, 'AN'],         
            ['TEST', 'C', 1, 'AN'],         
            ['FACTUURNUMMER', 'C', 17, 'AN'],         
            ['FACTUURDATUM', 'C', 8, 'AN'],          
            ['SOORTFACTUUR', 'C', 3, 'AN'],          
            ['EANAFNEMER', 'C', 13, 'AN'],         
            ['BTWAFNEMER', 'C', 17, 'AN'],         
            ['EANLEVERANCIER', 'C', 13, 'AN'],         
            ['BTWLEVERANCIER', 'C', 17, 'AN'],         
            ['EANAFLEVER', 'C', 13, 'AN'],         
            ['EANFACTUUR', 'C', 13, 'AN'],         
            ['VALUTA', 'C', 3, 'AN'],          
            ['ORDERNUMMERAFNEMER', 'C', 17, 'AN'],         
            ['HEA__RECORDATTRIBUTE', 'C', 17, 'AN'],         #is an xml attribute for the HEA-entity (record)
            ['FACTUURDATUM__FIELDATTRIBUTE', 'C', 17, 'AN'],         #is an xml attribute for the FACTUURDATUM-entity(field)
            ['XXXDATUM', 'C', 8, 'AN'],          
            ['XXXDATUM__FIELDATTRIBUTE', 'C', 17, 'AN'],         #is an xml attribute for the FACTUURDATUM-entity(field)
            ['TOTAALREGEL', 'C', 20.3, 'N'],       
            ['TOTAALBTW', 'C', 20.3, 'N'],       
            ['TOTAALFACTUUR', 'C', 20.3, 'N'],       
          ],
    'LIN':[
            ['BOTSID','C',3,'A'],
            ['REGEL', 'C', 6, 'N'],         
            ['ARTIKEL', 'C', 14, 'AN'],         
            ['GEFACTAANTAL', 'C', 16.3, 'N'],      
            ['GELEVERDAANTAL', 'C', 16.3, 'N'],        
            ['NETTOREGELBEDRAG', 'C', 20.3, 'N'],       
            ['PRIJS', 'C', 20.4, 'N'],       
            ['AANTALPRIJSBASIS', 'C', 16.3, 'N'],      
            ['EENHEIDPRIJSBASIS', 'C', 3, 'AN'],          
            ['BTWTARIEF', 'C', 3, 'AN'],          
            ['BTWPERCENTAGE', 'C', 12.4, 'N'],       
          ],
     }

from bots.botsconfig import *

syntax = { 
        'charset'     : 'iso-8859-1',
        'checkfixedrecordtooshort': True,
        'checkfixedrecordtoolong': True,
        }

structure=    [
{ID:'HEA',MIN:1,MAX:10000,
    QUERIES:{
        'frompartner':  {'BOTSID':'HEA','EANZENDER':None},
        'topartner':    {'BOTSID':'HEA','EANONTVANGER':None},
        'reference':    {'BOTSID':'HEA','FACTUURNUMMER':None},
        'testindicator':{'BOTSID':'HEA','TEST':None}},
    LEVEL:[
        {ID:'HAL',MIN:0,MAX:10},
        {ID:'LIN',MIN:1,MAX:10000,
            LEVEL:[
                {ID:'LAL',MIN:0,MAX:10},
                ]},
        {ID:'TOT',MIN:1,MAX:1},
        ]},
]

nextmessage = ({'BOTSID':'HEA'},)

    
recorddefs = {
    'HEA':[             #invoice header
            ['BOTSID','C',3,'A'],
            ['SOORT', 'C', 20, 'AN'],         
            ['EANZENDER', 'C', 13, 'AN'],       #ILN sender  
            ['EANONTVANGER', 'C', 13, 'AN'],         #ILN receiver
            ['TEST', 'C', 1, 'AN'],         #test indicator (0 or 1)
            ['FACTUURNUMMER', 'C', 17, 'AN'],         #invoice number
            ['FACTUURDATUM', 'C', 8, 'AN'],          #invoice date
            ['INDICATIEONTVANGSTBEVESTIGING', 'C', 3, 'AN'],   #
            ['SOORTFACTUUR', 'C', 3, 'AN'],          #kind of invoic (debit, credit)
            ['EANAFNEMER', 'C', 13, 'AN'],         #iln buyer
            ['BTWAFNEMER', 'C', 17, 'AN'],         #vat number buyer
            ['EANLEVERANCIER', 'C', 13, 'AN'],         #iln supplier
            ['BTWLEVERANCIER', 'C', 17, 'AN'],         #iln suppkier
            ['EANAFLEVER', 'C', 13, 'AN'],         #iln delivery place
            ['EANHAALADRES', 'C', 13, 'AN'],         #iln pickup address
            ['EANEINDBESTEMMING', 'C', 13, 'AN'],         #iln ultimate consignee
            ['EANFACTUUR', 'C', 13, 'AN'],         #iln receiver of invoice
            ['BTWFACTUUR', 'C', 17, 'AN'],         
            ['EANBONTVANGER', 'C', 13, 'AN'],         
            ['LEVERDATUM', 'C', 8, 'AN'],          #delivery date
            ['ACCIJNSVRIJ', 'C', 3, 'AN'],          
            ['VALUTA', 'C', 3, 'AN'],          #currency
            ['VERZENDBERICHTNUMMER', 'C', 17, 'AN'],         #despatch advice number
            ['ORDERNUMMERAFNEMER', 'C', 17, 'AN'],         #order number
            ['CORFACTUURNUMMER', 'C', 17, 'AN'],         #invoice number of orginal invoic
            ['DAGNAFACTUUR1', 'C', 3, 'N'],         #days for payment reduction 1
            ['PERCENTKORTING1', 'C', 12.4, 'N'],      #percentage payment reduction 1
            ['DAGNAFACTUUR2', 'C', 3, 'N'],         #(etc)
            ['PERCENTKORTING2', 'C', 12.4, 'N'],      
            ['DAGNAFACTUUR3', 'C', 3, 'N'],         
            ['PERCENTKORTING3', 'C', 12.4, 'N'],      
          ],
    'HAL':[             #charge allowance at invoice level
            ['BOTSID','C',3,'A'],
            ['KORTINGTOESLAG', 'C', 3, 'AN'],          #charge or allowance
            ['SOORTKORTING', 'C', 3, 'AN'],          #sort of charge/allowance
            ['KORTINGSBEDRAG', 'C', 20.3, 'N'],      #c/a amount
            ['BTWTARIEF', 'C', 3, 'AN'],          #c/a percentage
            ['BTWPERCENTAGE', 'C', 12.4, 'N'],       #vat percantage
          ],
    'LIN':[             #invoice line
            ['BOTSID','C',3,'A'],
            ['REGEL', 'C', 6, 'N'],         #line number
            ['ARTIKEL', 'C', 14, 'AN'],         #EAN article number
            ['PROMOTIECODE', 'C', 17, 'AN'],        #promotional variance
            ['ARTIKELOMSCHRIJVING', 'C', 35, 'AN'],         #description
            ['GEFACTAANTAL', 'C', 16.3, 'N'],      #quantity invoiced
            ['GELEVERDAANTAL', 'C', 16.3, 'N'],        #quantity delevered
            ['NETTOREGELBEDRAG', 'C', 20.3, 'N'],       #net lin amount
            ['PRIJS', 'C', 20.4, 'N'],       #price
            ['AANTALPRIJSBASIS', 'C', 16.3, 'N'],      #quantity price base
            ['EENHEIDPRIJSBASIS', 'C', 3, 'AN'],          #unit price base
            ['BTWTARIEF', 'C', 3, 'AN'],          #vat rate
            ['BTWPERCENTAGE', 'C', 12.4, 'N'],       #vate percentage
          ],
    'LAL':[         #charge/alownace line level
            ['BOTSID','C',3,'A'],
            ['KORTINGTOESLAG', 'C', 3, 'AN'],          #charge or allowance
            ['SOORTKORTING', 'C', 3, 'AN'],          #sort of charge/allowance
            ['KORTINGSBEDRAG', 'C', 20.3, 'N'],      #c/a amount
            ['BTWTARIEF', 'C', 3, 'AN'],          #c/a percentage
            ['BTWPERCENTAGE', 'C', 12.4, 'N'],        #vat percantage
          ],
    'TOT':[
            ['BOTSID','C',3,'A'],
            ['TOTAALREGEL', 'C', 20.3, 'N'],       #total net line amount
            ['TOTAALFACTUURKORTING', 'C', 20.3, 'N'],      #total invoice charge/allowance
            ['TOTAALBTW', 'C', 20.3, 'N'],       #total vat amount
            ['TOTAALFACTUUR', 'C', 20.3, 'N'],       #invoice amount
            ['GRONDSLAGBETKORTING', 'C', 20.3, 'N'],        #base amount payemtn reduction
            ['BTWTARIEF1', 'C', 3, 'AN'],          #vat rate 1
            ['BTWPERCENTAGE1', 'C', 12.4, 'N'],       #vate percentage 1
            ['BTWGRONDSLAG1', 'C', 20.3, 'N'],      #base amount vat1
            ['BTWBEDRAG1', 'C', 20.3, 'N'],       #vat amount 1
            ['BTWTARIEF2', 'C', 3, 'AN'],          #(etc, up to 4 vat's)
            ['BTWPERCENTAGE2', 'C', 12.4, 'N'],       
            ['BTWGRONDSLAG2', 'C', 20.3, 'N'],      
            ['BTWBEDRAG2', 'C', 20.3, 'N'],       
            ['BTWTARIEF3', 'C', 3, 'AN'],          
            ['BTWPERCENTAGE3', 'C', 12.4, 'N'],       
            ['BTWGRONDSLAG3', 'C', 20.3, 'N'],      
            ['BTWBEDRAG3', 'C', 20.3, 'N'],       
            ['BTWTARIEF4', 'C', 3, 'AN'],          
            ['BTWPERCENTAGE4', 'C', 12.4, 'N'],       
            ['BTWGRONDSLAG4', 'C', 20.3, 'N'],      
            ['BTWBEDRAG4', 'C', 20.3, 'N'],       
          ],
     }

from bots.botsconfig import *

from syntaxfixed import syntax

structure=    [
    {ID:'HEA',MIN:1,MAX:10000,
        QUERIES:{
            'frompartner':  {'BOTSID':'HEA','EANZENDER':None},
            'topartner':    {'BOTSID':'HEA','EANONTVANGER':None},
            'reference':    {'BOTSID':'HEA','BERICHTNUMMER':None},
            'testindicator':{'BOTSID':'HEA','TEST':None}},
        LEVEL:[
            {ID:'LIN',MIN:0,MAX:10000},
            ]},
    ]
    
nextmessage = ({'BOTSID':'HEA'},)

recorddefs = {
    'HEA':[
            ['BOTSID','C',3,'A'],               #1
            ['SOORT', 'C', 20, 'AN'],           #4         
            ['EANZENDER', 'C', 13, 'AN'],       #24         
            ['EANONTVANGER', 'C', 13, 'AN'],    #37      
            ['TEST', 'C', 1, 'AN'],             #50
            ['BERICHTNUMMER', 'C', 17, 'AN'],   #51
            ['BERICHTDATUM', 'C', 12, 'AN'],    #68   
            ['ORDERNUMMERAFNEMER', 'C', 17, 'AN'], #80        
            ['INDICATIEONTVANGSTBEVESTIGING', 'C', 3, 'AN'],    #97
            ['EANAFNEMER', 'C', 13, 'AN'],      #100
            ['EANLEVERANCIER', 'C', 13, 'AN'],  #113   
            ['EANAFLEVER', 'C', 13, 'AN'],      #126
            ['EANHAALADRES', 'C', 13, 'AN'],    #139 
            ['EANEINDBESTEMMING', 'C', 13, 'AN'],   #152      
            ['LEVERDATUM', 'C', 12, 'AN'],      #165
            ['BACKHAULING', 'C', 3, 'AN'],      #177
          ],                                    #180
    'LIN':[
            ['BOTSID','C',3,'A'],
            ['REGEL', 'C', 6, 'N'],         
            ['ARTIKEL', 'C', 14, 'AN'],         
            ['ARTIKELOMSCHRIJVING', 'C', 35, 'AN'],         
            ['AANTAL', 'C', 16.3, 'N'],      
          ],
    }
     

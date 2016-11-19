from bots.botsconfig import *

from syntaxfixed import syntax

nextmessage = ({'BOTSID':'HEA'},)

structure=    [
    {ID:'HEA',MIN:1,MAX:10000,
        QUERIES:{
            'frompartner':  {'BOTSID':'HEA','EANZENDER':None},
            'topartner':    {'BOTSID':'HEA','EANONTVANGER':None},
            'reference':    {'BOTSID':'HEA','ORDERNUMMER':None},
            'testindicator':{'BOTSID':'HEA','TEST':None}},
        LEVEL:[
            {ID:'LIN',MIN:0,MAX:10000},
            ]},
    ]

recorddefs = {
    'HEA':[
            ['BOTSID','C',3,'A'],    #pos 1
            ['SOORT', 'C', 20, 'A'],    #pos 4
            ['EANZENDER', 'C', 13, 'AN'],    #pos 24
            ['EANONTVANGER', 'C', 13, 'AN'],    #pos 59
            ['TEST', 'C', 1, 'AN'],    #pos 94
            ['ORDERNUMMER', 'C', 17, 'AN'],    #pos 95
            ['ORDERDATUM', 'C', 12, 'AN'],    #pos 112
            ['INDICATIEONTVANGSTBEVESTIGING', 'C', 3, 'AN'],    #pos 124
            ['SOORTORDER', 'C', 3, 'AN'],    #pos 127
            ['EANAFNEMER', 'C', 13, 'AN'],    #pos 
            ['EANLEVERANCIER', 'C', 13, 'AN'],    #pos 
            ['EANAFLEVER', 'C', 13, 'AN'],    #pos 
            ['EANHAALADRES', 'C', 13, 'AN'],    #pos 
            ['EANEINDBESTEMMING', 'C', 13, 'AN'],    #pos 
            ['EANFACTUUR', 'C', 13, 'AN'],    #pos 
            ['LEVERDATUM', 'C', 12, 'AN'],    #pos 
            ['VLEVERDATUM', 'C', 12, 'AN'],    #pos 
            ['LLEVERDATUM', 'C', 12, 'AN'],    #pos 
            ['GEIMPROVISEERD', 'C', 3, 'AN'],    #pos 
            ['ACCIJNSVRIJ', 'C', 3, 'AN'],    #pos 
            ['NULORDER', 'C', 3, 'AN'],    #pos 
            ['BACKHAULING', 'C', 3, 'AN'],    #pos 
            ['SPOEDORDER', 'C', 3, 'AN'],    #pos 
            ['WINKELINSTALLATIE', 'C', 3, 'AN'],    #pos 
            ['RAAMORDERNUMMER', 'C', 17, 'AN'],    #pos 
            ['ACTIENUMMER', 'C', 17, 'AN'],    #pos 
          ],
    'LIN':[
            ['BOTSID','C',3,'A'],    #pos 1
            ['REGEL', 'C', 6, 'N'],    #pos 4
            ['ARTIKEL', 'C', 14, 'AN'],    #pos 10
            ['PROMOTIECODE', 'C', 52, 'AN'],    #pos 24
            ['BESTELDAANTAL', 'C', 16.3, 'N'],    #pos 76
            ['ARTIKELOMSCHRIJVING', 'C', 80, 'AN'],    #pos 92-172
          ],
    }

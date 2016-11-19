from bots.botsconfig import *
from enveloperecords import recorddefs
from edifactsyntax3 import syntax

nextmessage = ({'BOTSID':'UNB'},{'BOTSID':'UNH'})
nextmessage2 = ({'BOTSID':'UNB'},{'BOTSID':'UNG'},{'BOTSID':'UNH'})

#works both with/without grouping (UNG-UNE)
#an interchange either consists of message or groups
#by placing UNH-UNT before UNG-UNE no collision will occur
structure = [
    {ID:'UNB',MIN:0,MAX:99999,    
        QUERIES:{
            'frompartner':  {'BOTSID':'UNB','S002.0004':None},
            'topartner':    {'BOTSID':'UNB','S003.0010':None},
            'testindicator':{'BOTSID':'UNB','0035':None}
            },
        LEVEL:		
            [
            {ID:'UNH',MIN:0,MAX:99999,
                QUERIES:{
                    'reference':   {'BOTSID':'UNH','0062':None},
                    },
                SUBTRANSLATION:[
                    {'BOTSID':'UNH','S009.0065':None},
                    {'BOTSID':'UNH','S009.0052':None},
                    {'BOTSID':'UNH','S009.0054':None},
                    {'BOTSID':'UNH','S009.0051':None},
                    {'BOTSID':'UNH','S009.0057':None},
                    ]},
            #note; no UNT in this envelope structure. This is not needed
            #message definitions have a UNT record.
            {ID:'UNG',MIN:0,MAX:99999,
                LEVEL:		
                    [
                    {ID:'UNH',MIN:0,MAX:99999,
                        QUERIES:{
                            'reference':   {'BOTSID':'UNH','0062':None},
                            },
                        SUBTRANSLATION:[
                            {'BOTSID':'UNH','S009.0065':None},
                            {'BOTSID':'UNH','S009.0052':None},
                            {'BOTSID':'UNH','S009.0054':None},
                            {'BOTSID':'UNH','S009.0051':None},
                            {'BOTSID':'UNH','S009.0057':None},
                            ]},
                    {ID:'UNE',MIN:1,MAX:1}
                    ]
                },
            {ID:'UNZ',MIN:1,MAX:1}
            ]
        }
    ]

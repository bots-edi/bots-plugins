from bots.botsconfig import *
from enveloperecords import recorddefs
from x12syntax import syntax

nextmessage = ({'BOTSID':'ISA'},{'BOTSID':'GS'},{'BOTSID':'ST'})

structure = [
    {ID:'ISA',MIN:0,MAX:99999,    
        QUERIES:{
            'frompartner':  {'BOTSID':'ISA','ISA06':None},
            'topartner':    {'BOTSID':'ISA','ISA08':None},
            'testindicator':{'BOTSID':'ISA','ISA15':None},
            },
        LEVEL:
            [
            {ID:'TA1',MIN:0,MAX:99999},
            {ID:'GS',MIN:0,MAX:99999,
                QUERIES:{
                    'version':   {'BOTSID':'GS','GS08':None},
                    },
                LEVEL:
                    [
                    {ID:'ST',MIN:0,MAX:99999,
                        QUERIES:{
                            'reference':   {'BOTSID':'ST','ST02':None},
                            },
                        SUBTRANSLATION:[
                            {'BOTSID':'ST','ST01':None},
                            ]},
                    {ID:'GE',MIN:1,MAX:1},
                    ]
                },
            {ID:'IEA',MIN:1,MAX:1}
            ]
        }
    ]

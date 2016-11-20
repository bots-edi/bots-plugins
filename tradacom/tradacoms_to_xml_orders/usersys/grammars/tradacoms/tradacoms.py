from bots.botsconfig import *
from enveloperecords import recorddefs
from tradacomssyntax import syntax

nextmessage = ({'BOTSID':'STX'},)

structure = [
    {ID:'STX',MIN:0,MAX:99999,
        QUERIES:{
            'frompartner':  {'BOTSID':'STX','FROM.01':None},
            'topartner':    {'BOTSID':'STX','UNTO.01':None},
            },
        LEVEL:
            [
            {ID:'MHD',MIN:0,MAX:99999,
                SUBTRANSLATION:[
                    {'BOTSID':'MHD','TYPE.01':None},
                    {'BOTSID':'MHD','TYPE.02':None},
                    ]},
            {ID:'END',MIN:1,MAX:1}
            ]
        }
    ]

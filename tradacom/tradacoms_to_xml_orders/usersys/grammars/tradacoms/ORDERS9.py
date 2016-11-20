from bots.botsconfig import *
from records_9 import recorddefs
from tradacomssyntax import syntax

structure = [
{ID:'MHD',MIN:1,MAX:1,LEVEL:[
    {ID:'CLO',MIN:1,MAX:1},
    {ID:'ORD',MIN:1,MAX:1},
    {ID:'DIN',MIN:0,MAX:1},
    {ID:'DNA',MIN:0,MAX:99999},
    {ID:'OLD',MIN:1,MAX:99999,LEVEL:[
        {ID:'DNB',MIN:0,MAX:99999},
        ]},
    {ID:'OTR',MIN:1,MAX:1},
    {ID:'MTR',MIN:1,MAX:1},
    ]
}]

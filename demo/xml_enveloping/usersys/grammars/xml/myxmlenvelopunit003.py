from bots.botsconfig import *

syntax = {
        'indented':True,               #False: xml output is one string (no cr/lf); True: xml output is indented/human readable
        'charset':'utf-8',
        'merge': True,
        'envelope': 'myxmlenvelopunit003',
        }

structure=    [
{ID:'root003',MIN:1,MAX:10000,
    LEVEL:[
        {ID:'{http://www.w3.org/2001/XInclude}include',MIN:0,MAX:10000},
        ]},
]

recorddefs = {
    'root003':[
            ['BOTSID','C',7,'A'],
            ['sender','C',35,'A'],
            ['receiver','C',35,'A'],
          ],
    '{http://www.w3.org/2001/XInclude}include':[
            ['BOTSID','C',40,'A'],
            ['{http://www.w3.org/2001/XInclude}include__parse', 'C', 256, 'AN'],          
            ['{http://www.w3.org/2001/XInclude}include__href', 'C', 256, 'AN'],          
          ],
     }

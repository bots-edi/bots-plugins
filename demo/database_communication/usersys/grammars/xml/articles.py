from bots.botsconfig import *

syntax = { 
        'indented':True,               #False: xml output is one string (no cr/lf); True: xml output is indented/human readable
        }

structure=    [
{ID:'articles',MIN:1,MAX:1,LEVEL:[
    {ID:'article',MIN:0,MAX:9999},
    ]}
]

recorddefs = {
    'articles':[
            ['BOTSID','M',255,'A'],
          ],
    'article':[
            ['BOTSID','M',255,'A'],
            ['ccodeid', 'M', 35, 'AN'],
            ['leftcode', 'M', 35, 'AN'],
            ['rightcode', 'M', 35, 'AN'],
            ['attr1', 'C', 35, 'AN'],
            ['attr2', 'C', 35, 'AN'],
            ['attr3', 'C', 35, 'AN'],
            ['attr4', 'C', 35, 'AN'],
            ['attr5', 'C', 35, 'AN'],
            ['attr6', 'C', 35, 'AN'],
            ['attr7', 'C', 35, 'AN'],
            ['attr8', 'C', 35, 'AN'],
          ],
      }
 

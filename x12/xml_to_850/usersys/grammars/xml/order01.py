from bots.botsconfig import *

nextmessage = ({'BOTSID':'envelope'},{'BOTSID':'header'})


structure=    [
{ID:'envelope',MIN:1,MAX:1,LEVEL:[
    {ID:'header',MIN:1,MAX:99999,
        QUERIES:{
            'frompartner':  {'BOTSID':'header','SENDER':None},
            'topartner':    {'BOTSID':'header','RECEIVER':None},
            'testindicator':{'BOTSID':'header','TESTINDICATOR':None},
            },
        LEVEL:[
        {ID:'lines',MIN:0,MAX:1,LEVEL:[
            {ID:'line',MIN:1,MAX:99999},
            ]},
        ]},
    ]}
]

recorddefs = {
   'envelope':[
            ['BOTSID','M',256,'A'],
          ],
   'header':[
            ['BOTSID','M',256,'A'],
            ['SENDER','C', 256,'AN'],
            ['RECEIVER','C', 256,'AN'],
            ['TESTINDICATOR','C', 256,'AN'],
            ['PONUMBER','C', 256,'AN'],
            ['PORELEASENUMBER','C', 256,'AN'],
            ['PODATE','C', 256,'AN'],
            ['POREFERENCE','C', 256,'AN'],
            ['CONTACTNAME','C', 256,'AN'],
            ['CONTACTPHONE','C', 256,'AN'],
            ['CONTACTEMAIL','C', 256,'AN'],
            ['FREETEXT','C', 256,'AN'],
            ['STID','C', 256,'AN'],
            ['STNAME','C', 256,'AN'],
            ['STADDNAME','C', 256,'AN'],
            ['STSTREET','C', 256,'AN'],
            ['STCITY','C', 256,'AN'],
            ['STSTATE','C', 256,'AN'],
            ['STZIPCODE','C', 256,'AN'],
          ],
    'lines':[
            ['BOTSID','M',256,'A'],
          ],
    'line':[
            ['BOTSID','M',256,'A'],
            ['LINENUMBER','C',256,'A'],
            ['QTY','C',15,'R'],
            ['UNIT','C',256,'A'],
            ['UNITPRICE','C',15,'R'],
            ['VENDORITEMNUMBER','C',256,'A'],
            ['BUYERITEMNUMBER','C',256,'A'],
            ['POSHIPNUMBER','C',256,'A'],
            ['DESCRIPTION','C',256,'A'],
          ],
    }
 

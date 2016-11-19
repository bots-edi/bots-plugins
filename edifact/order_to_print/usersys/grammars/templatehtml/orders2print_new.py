from bots.botsconfig import *

syntax = {
        'merge':		True,
        'template':   'edifax.html',			#template (genshi-file) to use
        'envelope-template':   'edifaxenvelope.html',			#template (genshi-file) to use
        'has_structure':True,   #is True, read structure, recorddef, check these
        'print_as_row':[['Orderheader', 'Lines']],  #to indicate what should be printed as a table with 1 row per record (instead of 1 record->1 table)
        'contenttype':'text/html',
       }


structure=    [
    {ID:'Orderheader',MIN:1,MAX:10000,LEVEL:[
        {ID:'Lines',MIN:0,MAX:10000},
        ]},
    ]
    

recorddefs = {
    'Orderheader':[
            ['BOTSID','C',256,'A'],
            ['Sender', 'C', 13, 'AN'],         
            ['Receiver', 'C', 13, 'AN'],         
            ['Order type', 'C', 3, 'AN'],          
            ['Order number', 'C', 17, 'AN'],         
            ['Order date', 'C', 12, 'AN'],          
            ['Buyer', 'C', 13, 'AN'],         
            ['Supplier', 'C', 13, 'AN'],         
            ['Delivery place', 'C', 13, 'AN'],         
            ['Haul address', 'C', 13, 'AN'],         
            ['Final destination', 'C', 13, 'AN'],         
            ['Invoice address', 'C', 13, 'AN'],         
            ['Delivery date', 'C', 12, 'AN'],          
            ['Earliest delivery date', 'C', 12, 'AN'],          
            ['Latest delivery date', 'C', 12, 'AN'],          
          ],
    'Lines':[
            ['BOTSID','C',256,'A'],
            ['Line number', 'C', 6, 'N'],         
            ['Item number', 'C', 14, 'AN'],         
            ['Quantity', 'C', 16.3, 'N'],      
            ['Description', 'C', 35, 'AN'],         
          ],
    }
     

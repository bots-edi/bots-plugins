
#~syntax = { 
#~        'field_sep'  : ')',
#~        'version'    :  '00401',
#~        }


syntax = {
#seperators
          'sfield_sep':'>', #sub field seperator
          'field_sep':'*', #field seperator
          'record_sep':"~", #record/segment seperator 'add_crlfafterrecord_sep':'', #value \r\n gives nicer formatting but is not always accepted.
          'version'    :  '00401',
#partner specific values for x12 envelopes 'version' : '00401', #ISA version to use.
          'ISA07' : 'ZZ', #communication qualifier sender 'ISA07' : 'ZZ', 
          'ISA15' : 'T', #communication qualifier reciever 'ISA15' : 'P', #test-indicator: T=test, P=production 
          }

syntax = {
    #seperators
    'sfield_sep':'>',   #sub field seperator
    'field_sep':'*',    #field seperator
    'record_sep':"~",   #record/segment seperator
    'add_crlfafterrecord_sep':'',   #value \r\n gives nicer formatting but is not always accepted.
    #partner specific values for x12 envelopes
    'version'  : '00401',  #ISA version to use.
    'ISA05'    : 'ZZ',     #communication qualifier sender
    'ISA06'    : 'S000000',#sender in ISA envelope
    'ISA07'    : '33',     #communication qualifier reciever
    'ISA08'    : '54771',  #receiver in ISA envelope
    'ISA11'    : 'U',      
    'ISA15'    : 'P',  #test-indicator: T=test, P=production
    'GS02'     : 'CUSTOM',#sender in GS envelope
    'GS03'     : '54771',  #receiver in GS envelope
    }

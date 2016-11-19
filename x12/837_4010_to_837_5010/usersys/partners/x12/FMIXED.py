syntax = {
    #seperators
    'sfield_sep':'>',   #sub field seperator
    'field_sep':'*',    #field seperator
    'record_sep':"~",   #record/segment seperator
    'add_crlfafterrecord_sep':'',   #value \r\n gives nicer formatting but is not always accepted.
    #partner specific values for x12 envelopes
    'version'  : '00501',  #ISA version to use.
    'ISA05'    : 'ZZ',     #communication qualifier sender
    'ISA06'    : 'CUSTOM',#sender in ISA envelope
    'ISA07'    : 'ZZ',     #communication qualifier reciever
    'ISA08'    : 'FMIXED',  #receiver in ISA envelope
    'ISA11'    : 'C',      
    'ISA15'    : 'P',  #test-indicator: T=test, P=production
    'GS02'     : '0000',#sender in GS envelope
    'GS03'     : 'FMIXED',  #receiver in GS envelope
    }

syntax = {
    #seperators
    'sfield_sep':'>',   #sub field seperator
    'field_sep':'*',    #field seperator
    'record_sep':"~",   #record/segment seperator
    'add_crlfafterrecord_sep':'',   #value \r\n gives nicer formatting but is not always accepted.
    #partner specific values for x12 envelopes
    'version'  : '00401',  #ISA version to use.
    'ISA05'    : 'ZZ',     #communication qualifier sender
    'ISA06'    : '0000002',#sender in ISA envelope
    'ISA07'    : 'ZZ',     #communication qualifier reciever
    'ISA08'    : '12052',  #receiver in ISA envelope
    'ISA11'    : 'U',      
    'ISA15'    : 'P',  #test-indicator: T=test, P=production
    'GS02'     : '0000001',#sender in GS envelope
    'GS03'     : '12052',  #receiver in GS envelope
    }

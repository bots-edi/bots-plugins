import bots.botslib as botslib

def lookup_partnerID(partnerID,qual):
    #if caching do lookup in cache.
    for row in botslib.query(u'''SELECT rightcode, attr1
                                FROM ccode
                                WHERE ccodeid_id = %(ccodeid)s
                                AND leftcode = %(leftcode)s''',
                                {'ccodeid':'x12_partner','leftcode':partnerID}):
        ediID = row['rightcode']
        qual = row['attr1']
        break
    else:
        ediID = partnerID
    #if caching: put in cache
    return ediID,qual
    

def ta_infocontent(ta_info):
    ''' the partnerID as used in bots is used to do lookups;
        lookup gives ediID and qual for use in x12.  
    '''
    ta_info['frompartner'], ta_info['ISA05'] = lookup_partnerID(ta_info['frompartner'],ta_info['ISA05'])
    ta_info['topartner'], ta_info['ISA07'] = lookup_partnerID(ta_info['topartner'],ta_info['ISA07'])
    
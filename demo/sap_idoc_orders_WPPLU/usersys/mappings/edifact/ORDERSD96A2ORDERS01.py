#mapping-script

def main(inn,out):
    out.ta_info['MANDT'] = '032'
    out.put({'BOTSID':'EDI_DC40','SNDPRN':inn.ta_info['frompartner']})
    out.put({'BOTSID':'EDI_DC40','RCVPRN':inn.ta_info['topartner']})
    docnr = inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':None})
    out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E2EDK01003','BELNR':docnr})
    inn.ta_info['botskey'] = docnr
    out.ta_info['botskey'] = docnr
    out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDK03','IDDAT':'012','DATUM':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2380':None})})
    out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDP20','EDATU':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'63','C507.2380':None})})
        
    out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDKA1002','PARVW':'AG','PARTN':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY','C082.3039':None})})
    out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDKA1002','PARVW':'LF','ILNNR':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3039':None})})
    out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDKA1002','PARVW':'WE','LIFNR':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'DP','C082.3039':None})})
    out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDK02','QUALF':'007','BELNR':inn.get({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'AAK','C506.1154':None})})
        
    idocsoortorder = inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':None})
    if idocsoortorder== '230':
        IHREZ = 'AC'
    elif idocsoortorder== '352':
        IHREZ = inn.get({'BOTSID':'UNH'},{'BOTSID':'FTX','4451':'ZZZ','C107.3055':'92','C107.4441':None})
    elif idocsoortorder== '220':
        if inn.get({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'PD','C506.1154':None}):
            IHREZ = ''
        else:
            IHREZ = 'A'
    else:
        raise exception('Geen valide code in BGM.soort order: %s.'%idocsoortorder)
    out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDKA1002','PARVW':'AG','IHREZ': IHREZ})
    
    LEVERDATUM = inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'2','C507.2380':None}) 
    for lin in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'LIN'}):
        lou = out.putloop({'BOTSID':'EDI_DC40'},{'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDP01003'})
        lou.put({'BOTSID':'E2EDP01003','POSEX':lin.get({'BOTSID':'LIN','1082':None})})
        lou.put({'BOTSID':'E2EDP01003'},{'BOTSID':'E2EDP19001','QUALF':'001','IDTNR':lin.get({'BOTSID':'LIN','C212.7140':None})})
        lou.put({'BOTSID':'E2EDP01003','MENGE':lin.get({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'21','C186.6060':None})})
        lou.put({'BOTSID':'E2EDP01003'},{'BOTSID':'E2EDP20','EDATU':LEVERDATUM})

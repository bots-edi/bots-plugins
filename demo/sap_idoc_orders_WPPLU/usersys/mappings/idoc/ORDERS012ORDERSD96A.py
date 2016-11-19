#mapping-script

def main(inn,out):
    out.put({'BOTSID':'UNH','0062':out.ta_info['reference'],'S009.0065':'ORDERS','S009.0052':'D','S009.0054':'96A','S009.0051':'UN','S009.0057':'EAN008'})
    out.put({'BOTSID':'UNH'},{'BOTSID':'UNS','0081':'S'})
    out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':inn.get({'BOTSID':'E2EDK01003','BELNR':None})})
        
    idocsoortorder = inn.get({'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDKA1002','PARVW':'AG','IHREZ':None})
    if idocsoortorder is None:  #not there, or empty string
        soortorder = '220'
    elif idocsoortorder.isdigit():
        soortorder = '352'
        out.put({'BOTSID':'UNH'},{'BOTSID':'FTX','4451':'ZZZ','C107.3055':'92','C107.4441':idocsoortorder}) 
    elif idocsoortorder == 'A':
        soortorder = '220'
        out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'PD','C506.1154':'99'})
    elif idocsoortorder == 'AC':
        soortorder = '230'
    else:
        raise exception('Geen valide code in IHREZ waar PARVW = "AG".')
    out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':soortorder})
    out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'AAK','C506.1154':inn.get({'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDK02','BELNR':None,'QUALF':'007'})})

    out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY','C082.3055':'9','C082.3039':inn.get({'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDKA1002','PARVW':'AG','PARTN':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3055':'9','C082.3039':inn.get({'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDKA1002','PARVW':'LF','ILNNR':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'DP','C082.3055':'9','C082.3039':inn.get({'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDKA1002','PARVW':'WE','LIFNR':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2379':'102','C507.2380':inn.get({'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDK03','DATUM':None,'IDDAT':'012'})})
    LEVERDATUM = inn.get({'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDP01003'},{'BOTSID':'E2EDP20','EDATU':None}) 
    if LEVERDATUM:
        if len(LEVERDATUM) == 8:
            FLEVERDATUM = '102'
        else:
            FLEVERDATUM = '203'
        out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'2','C507.2380':LEVERDATUM,'C507.2379':FLEVERDATUM})
    LLEVERDATUM = inn.get({'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDK02','DATUM':None,'QUALF':'020'})
    if LLEVERDATUM:
        if len(LLEVERDATUM) == 8:
            FLEVERDATUM = '102'
        else:
            FLEVERDATUM = '203'
        out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'63','C507.2380':LLEVERDATUM,'C507.2379':FLEVERDATUM})

    for regel in inn.getloop({'BOTSID':'E2EDK01003'},{'BOTSID':'E2EDP01003'}):
        lou = out.putloop({'BOTSID':'UNH'},{'BOTSID':'LIN'})
        lou.put({'BOTSID':'LIN','1082':regel.get({'BOTSID':'E2EDP01003','POSEX':None})})
        lou.put({'BOTSID':'LIN','C212.7143':'IN','C212.7140':regel.get({'BOTSID':'E2EDP01003'},{'BOTSID':'E2EDP19001','QUALF':'001','IDTNR':None})})
        lou.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'21','C186.6060':regel.get({'BOTSID':'E2EDP01003','MENGE':None})})

    out.put({'BOTSID':'UNH'},{'BOTSID':'UNT','0074':out.getcount()+1,'0062':out.ta_info['reference']})  #last line (counts the segments produced in out-message, add 1 for UNT itself)

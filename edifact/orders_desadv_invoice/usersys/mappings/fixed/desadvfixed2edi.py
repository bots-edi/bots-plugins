#mapping-script
import time

def main(inn,out):
    out.put({'BOTSID':'UNH','0062':out.ta_info['reference'],'S009.0065':'DESADV','S009.0052':'D','S009.0054':'96A','S009.0051':'UN','S009.0057':'EAN005'})
    out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':inn.get({'BOTSID':'HEA','BERICHTNUMMER':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':'351','1225':'9'})
    out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'ON','C506.1154':inn.get({'BOTSID':'HEA','ORDERNUMMERAFNEMER':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'ZZZ','C506.1154':'EANNL1'})
    out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY','C082.3055':'9','C082.3039':inn.get({'BOTSID':'HEA','EANAFNEMER':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3055':'9','C082.3039':inn.get({'BOTSID':'HEA','EANLEVERANCIER':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'DP','C082.3055':'9','C082.3039':inn.get({'BOTSID':'HEA','EANAFLEVER':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SF','C082.3055':'9','C082.3039':inn.get({'BOTSID':'HEA','EANHAALADRES':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'UC','C082.3055':'9','C082.3039':inn.get({'BOTSID':'HEA','EANEINDBESTEMMING':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2379':'102','C507.2380':time.strftime('%Y%m%d')})
    LEVERDATUM = inn.get({'BOTSID':'HEA','LEVERDATUM':None})
    if LEVERDATUM:
        if len(LEVERDATUM) == 8:
            FLEVERDATUM = '102'
        else:
            FLEVERDATUM = '203'
        out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'17','C507.2380':LEVERDATUM,'C507.2379':FLEVERDATUM})
    if inn.get({'BOTSID':'HEA','BACKHAULING':None}):
        out.put({'BOTSID':'UNH'},{'BOTSID':'TOD','4055':'4'})

    atleastoneline=True
    for regel in inn.getloop({'BOTSID':'HEA'},{'BOTSID':'LIN'}):
        if atleastoneline:
            atleastoneline = False
            out.put({'BOTSID':'UNH'},{'BOTSID':'CPS','7164':'1'})
        lou = out.putloop({'BOTSID':'UNH'},{'BOTSID':'CPS'},{'BOTSID':'LIN'})
        lou.put({'BOTSID':'LIN','1082':regel.get({'BOTSID':'LIN','REGEL':None})})
        lou.put({'BOTSID':'LIN','C212.7143':'EN','C212.7140':regel.get({'BOTSID':'LIN','ARTIKEL':None})})
        lou.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'12','C186.6060':regel.get({'BOTSID':'LIN','AANTAL':None})})
        lou.put({'BOTSID':'LIN'},{'BOTSID':'IMD','C960.4294':regel.get({'BOTSID':'LIN','ARTIKELOMSCHRIJVING':None})})

    out.put({'BOTSID':'UNH'},{'BOTSID':'UNT','0074':out.getcount()+1,'0062':out.ta_info['reference']})  #last line (counts the segments produced in out-out

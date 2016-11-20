#mapping-script
import time
import bots.transform as transform

def main(inn,out):
    #~ print 'in WPLUU2pricat'
    for edidc in inn.getloop({'BOTSID':'EDI_DC40'}):
        #~ lou = out.putloop({'BOTSID':'UNH'},{'BOTSID':'PGI'},{'BOTSID':'LIN'})
        out.put({'BOTSID':'UNH','0062':out.ta_info['reference'],'S009.0065':'PRICAT','S009.0052':'D','S009.0054':'96A','S009.0051':'UN','S009.0057':'EAN005'})
        out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':'9','1004':edidc.get({'BOTSID':'EDI_DC40','DOCNUM':None})})
        out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2379':'102','C507.2380':transform.strftime('%Y%m%d')})
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY','C082.3055':'9','C082.3039':inn.ta_info['frompartner']})
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3055':'9','C082.3039':inn.ta_info['topartner']})
        out.put({'BOTSID':'UNH'},{'BOTSID':'CUX','C504#1.6347':'2','C504#1.6343':'8','C504#1.6345':edidc.get({'BOTSID':'EDI_DC40'},{'BOTSID':'E2WPA01'},{'BOTSID':'E2WPA04'},{'BOTSID':'E2WPA05002','CURRENCY':None})})
        out.put({'BOTSID':'UNH'},{'BOTSID':'PGI','5379':'2'})
        linecounter=0
        for artikel in edidc.getloop({'BOTSID':'EDI_DC40'},{'BOTSID':'E2WPA01'}):
            lou = out.putloop({'BOTSID':'UNH'},{'BOTSID':'PGI'},{'BOTSID':'LIN'})
            linecounter += 1
            lou.put({'BOTSID':'LIN','1082':linecounter})
            artikelcode = artikel.get({'BOTSID':'E2WPA01','HAUPTEAN':None})[:10]
            artikelcode = transform.addeancheckdigit('16'+artikelcode)
            lou.put({'BOTSID':'LIN','C212.7143':'EN','C212.7140':artikelcode})
            lou.put({'BOTSID':'LIN'},{'BOTSID':'PIA','4347':'5','C212#1.7143':'SA','C212#1.7140':artikel.get({'BOTSID':'E2WPA01','ARTIKELNR':None})})
            lou.put({'BOTSID':'LIN'},{'BOTSID':'PIA','4347':'1','C212#1.7143':'GU','C212#1.7140':artikel.get({'BOTSID':'E2WPA01'},{'BOTSID':'E2WPA02002','WARENGR':None})})
            lou.put({'BOTSID':'LIN'},{'BOTSID':'IMD','7077':'A','C273.7008#1':artikel.get({'BOTSID':'E2WPA01'},{'BOTSID':'E2WPA03','QUALARTTXT':'LTXT','TEXT':None})[:35]})
            lou.put({'BOTSID':'LIN'},{'BOTSID':'DTM','C507.2005':'157','C507.2379':'102','C507.2380':artikel.get({'BOTSID':'E2WPA01','AKTIVDATUM':None})})
            lou.put({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'NTP','C509.5387':'SRP','C509.5118':artikel.get({'BOTSID':'E2WPA01'},{'BOTSID':'E2WPA04','KONDART':'VKP0'},{'BOTSID':'E2WPA05002','KONDWERT':None})})

        out.put({'BOTSID':'UNH'},{'BOTSID':'UNT','0074':out.getcount()+1,'0062':out.ta_info['reference']})  #last line (counts the segments produced in out-message, add 1 for UNT itself)

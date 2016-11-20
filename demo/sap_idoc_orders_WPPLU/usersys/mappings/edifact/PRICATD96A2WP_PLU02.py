#mapping-script

def main(inn,out):
    out.ta_info['MANDT'] = '010'
    out.put({'BOTSID':'EDI_DC40','SNDPRN':inn.ta_info['frompartner']})
    out.put({'BOTSID':'EDI_DC40','RCVPRN':inn.ta_info['topartner']})

    for artikel in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'PGI'},{'BOTSID':'LIN'}):
        lou = out.putloop({'BOTSID':'EDI_DC40'},{'BOTSID':'E2WPA01'})
        artikelcode = artikel.get({'BOTSID':'LIN','C212.7143':'EN','C212.7140':None})[2:12]
        lou.put({'BOTSID':'E2WPA01','HAUPTEAN':artikelcode+ '00000000'})
        lou.put({'BOTSID':'E2WPA01','ARTIKELNR':artikel.get({'BOTSID':'LIN'},{'BOTSID':'PIA','4347':'5','C212#1.7143':'SA','C212#1.7140':None})})
        lou.put({'BOTSID':'E2WPA01','AKTIVDATUM':artikel.get({'BOTSID':'LIN'},{'BOTSID':'DTM','C507.2005':'157','C507.2379':'102','C507.2380':None})})
        lou.put({'BOTSID':'E2WPA01'},{'BOTSID':'E2WPA04'},{'BOTSID':'E2WPA05002','CURRENCY':inn.get({'BOTSID':'UNH'},{'BOTSID':'CUX','C504#1.6347':'2','C504#1.6343':'8','C504#1.6345':None})})
        lou.put({'BOTSID':'E2WPA01'},{'BOTSID':'E2WPA02002','WARENGR':artikel.get({'BOTSID':'LIN'},{'BOTSID':'PIA','4347':'1','C212#1.7143':'GU','C212#1.7140':None})})
        lou.put({'BOTSID':'E2WPA01'},{'BOTSID':'E2WPA03','QUALARTTXT':'LTXT','TEXT':artikel.get({'BOTSID':'LIN'},{'BOTSID':'IMD','7077':'A','C273.7008#1':None})})
        lou.put({'BOTSID':'E2WPA01'},{'BOTSID':'E2WPA04','KONDART':'VKP0'},{'BOTSID':'E2WPA05002','KONDWERT':artikel.get({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'NTP','C509.5387':'SRP','C509.5118':None})})


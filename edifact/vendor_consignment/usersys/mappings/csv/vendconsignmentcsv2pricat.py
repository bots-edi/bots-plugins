#mapping-script
import time
import bots.transform as transform

def main(inn,out):
    out.ta_info['frompartner']='8717612000008'
    out.ta_info['topartner']='8711793000000'
    out.put({'BOTSID':'UNH','0062':out.ta_info['reference'],'S009.0065':'PRICAT','S009.0052':'D','S009.0054':'96A','S009.0051':'UN','S009.0057':'EAN006'})
    out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':'9','1004':out.ta_info['reference']})
    out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2379':'102','C507.2380':time.strftime('%Y%m%d')})
    out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'CT','C506.1154':'1'})
    out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY','C082.3055':'9','C082.3039':out.ta_info['topartner']})
    out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3055':'9','C082.3039':out.ta_info['frompartner']})
    out.put({'BOTSID':'UNH'},{'BOTSID':'CUX','C504#1.6347':'2','C504#1.6343':'8','C504#1.6345':'EUR'})
    out.put({'BOTSID':'UNH'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','C243.5278':'19','5305':'S'})
    out.put({'BOTSID':'UNH'},{'BOTSID':'PGI','5379':'2'})
    linecounter=0
    for artikel in inn.getloop({'BOTSID':'PRI'}):
        EANARTIKEL = artikel.get({'BOTSID':'PRI','EANARTIKEL':None})
        SUARTIKEL = artikel.get({'BOTSID':'PRI','SUARTIKEL':None})
        OMSCHRIJVING = artikel.get({'BOTSID':'PRI','OMSCHRIJVING':None})
        VERKOOPPRIJS = artikel.get({'BOTSID':'PRI','VERKPRI':None})
        if not (EANARTIKEL and SUARTIKEL and OMSCHRIJVING and VERKOOPPRIJS):
            continue
        lou = out.putloop({'BOTSID':'UNH'},{'BOTSID':'PGI'},{'BOTSID':'LIN'})
        linecounter += 1
        lou.put({'BOTSID':'LIN','1082':linecounter,'1229':'1','C212.7143':'EN','C212.7140':EANARTIKEL})
        lou.put({'BOTSID':'LIN'},{'BOTSID':'PIA','4347':'5','C212#1.7143':'SA','C212#1.7140':SUARTIKEL})
        lou.put({'BOTSID':'LIN'},{'BOTSID':'IMD','7077':'A','C273.7008#1':OMSCHRIJVING[:35]})
        MAAT = artikel.get({'BOTSID':'PRI','MAAT':None})
        if MAAT:
            lou.put({'BOTSID':'LIN'},{'BOTSID':'IMD','7077':'C','7081':'98','C273.7009':MAAT[:35]})
        KLEUR = artikel.get({'BOTSID':'PRI','KLEUR':None})
        if KLEUR:
            lou.put({'BOTSID':'LIN'},{'BOTSID':'IMD','7077':'C','7081':'35','C273.7009':KLEUR[:35]})
        BUYERPRODUCTGROUP = artikel.get({'BOTSID':'PRI','BUYERPRODUCTGROUP':None})
        if BUYERPRODUCTGROUP:
            lou.put({'BOTSID':'LIN'},{'BOTSID':'PIA','4347':'1','C212#1.7143':'GB','C212#1.7140':BUYERPRODUCTGROUP[:35]})
        DATUMVANAF = artikel.get({'BOTSID':'PRI','DATUMVANAF':None})
        if DATUMVANAF:
            DATUMVANAF = time.strftime('%Y%m%d',time.strptime(DATUMVANAF.strip()[:10],'%d-%m-%Y'))
            lou.put({'BOTSID':'LIN'},{'BOTSID':'DTM','C507.2005':'157','C507.2379':'102','C507.2380':DATUMVANAF})
        DATUMTOT = artikel.get({'BOTSID':'PRI','DATUMTOT':None})
        PROMOTIEPRIJS = artikel.getnozero({'BOTSID':'PRI','PROPRI':None})
        if DATUMTOT and PROMOTIEPRIJS:
            lou.put({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'NTP','C509.5387':'PRP','C509.5118':PROMOTIEPRIJS})
            DATUMTOT = time.strftime('%Y%m%d',time.strptime(DATUMTOT.strip()[:10],'%d-%m-%Y'))
            lou.put({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'NTP'},{'BOTSID':'DTM','C507.2005':'206','C507.2379':'102','C507.2380':DATUMTOT})
            
        #~ lou.put({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'AAA','C509.5375':'CT','C509.5118':1})
        lou.put({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'NTP','C509.5387':'RTP','C509.5118':VERKOOPPRIJS})

    out.put({'BOTSID':'UNH'},{'BOTSID':'UNT','0074':out.getcount()+1,'0062':out.ta_info['reference']})  #last line (counts the segments produced in out-message, add 1 for UNT itself)

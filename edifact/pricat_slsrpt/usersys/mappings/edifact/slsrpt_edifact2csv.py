#mapping-script
import bots.transform as transform

def main(inn,out):
    for lin in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'LOC'}):
        EANFILIAAL = lin.get({'BOTSID':'LOC','3227':'162','C517.3225':None})
        SLSRPTDATUM = lin.get({'BOTSID':'LOC','3227':'162'},{'BOTSID':'DTM','C507.2005':'356','C507.2380':None})
        for li2 in lin.getloop({'BOTSID':'LOC'},{'BOTSID':'LIN'}):
            lou = out.putloop({'BOTSID':'SLS'})
            lou.put({'BOTSID':'SLS','EANFILIAAL':EANFILIAAL})
            lou.put({'BOTSID':'SLS','SLSRPTDATUM':SLSRPTDATUM})
            lou.put({'BOTSID':'SLS','EANARTIKEL':li2.get({'BOTSID':'LIN','C212.7140':None})})
            lou.put({'BOTSID':'SLS','AANTAL':li2.get({'BOTSID':'LIN'},{'BOTSID':'QTY', 'C186.6063':'153','C186.6060':None})})
            lou.put({'BOTSID':'SLS','PRICE':li2.get({'BOTSID':'LIN'},{'BOTSID':'PRI', 'C509.5125':'NTP','C509.5118':None})})

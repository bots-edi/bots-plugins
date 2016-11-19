#mapping-script

def main(inn,out):
    EANZENDER = inn.ta_info['frompartner']
    EANONTVANGER = inn.ta_info['topartner']
    TEST = inn.ta_info['testindicator']
    ORDERNUMMER = inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':None})
    out.ta_info['reference'] = ORDERNUMMER
    SOORTORDER = inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':None})
    ORDERDATUM = inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2380':None})
    LEVERDATUM = inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'2','C507.2380':None})
    VLEVERDATUM = inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'64','C507.2380':None})
    LLEVERDATUM = inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'63','C507.2380':None})
    RAAMORDERNUMMER = inn.get({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'BO','C506.1154':None})
    ACTIENUMMER = inn.get({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'PD','C506.1154':None})
    EANAFNEMER = inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY','C082.3039':None})
    EANLEVERANCIER = inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3039':None})
    EANAFLEVER = inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'DP','C082.3039':None})
    EANHAALADRES = inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SF','C082.3039':None})
    EANEINDBESTEMMING = inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'UC','C082.3039':None})
    EANFACTUUR = inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'IV','C082.3039':None})

    for lin in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'LIN'}):
        lou = out.putloop({'BOTSID':'HEA'})     #this is needed; it takes care of initialising a new HEA-record
        lou.put({'BOTSID':'HEA','EANZENDER':EANZENDER})
        lou.put({'BOTSID':'HEA','EANONTVANGER':EANONTVANGER})
        lou.put({'BOTSID':'HEA','TEST':TEST})
        lou.put({'BOTSID':'HEA','SOORT':'ORDERSD96AUNEAN008'})
        lou.put({'BOTSID':'HEA','ORDERNUMMER':ORDERNUMMER})
        lou.put({'BOTSID':'HEA','SOORTORDER':SOORTORDER})
        lou.put({'BOTSID':'HEA','ORDERDATUM':ORDERDATUM})
        lou.put({'BOTSID':'HEA','LEVERDATUM':LEVERDATUM})
        lou.put({'BOTSID':'HEA','VLEVERDATUM':VLEVERDATUM})
        lou.put({'BOTSID':'HEA','LLEVERDATUM':LLEVERDATUM})
        lou.put({'BOTSID':'HEA','RAAMORDERNUMMER':RAAMORDERNUMMER})
        lou.put({'BOTSID':'HEA','ACTIENUMMER':ACTIENUMMER})
        lou.put({'BOTSID':'HEA','EANAFNEMER':EANAFNEMER})
        lou.put({'BOTSID':'HEA','EANLEVERANCIER':EANLEVERANCIER})
        lou.put({'BOTSID':'HEA','EANAFLEVER':EANAFLEVER})
        lou.put({'BOTSID':'HEA','EANHAALADRES':EANHAALADRES})
        lou.put({'BOTSID':'HEA','EANEINDBESTEMMING':EANEINDBESTEMMING})
        lou.put({'BOTSID':'HEA','EANFACTUUR':EANFACTUUR})
        lou.put({'BOTSID':'HEA','REGEL':lin.get({'BOTSID':'LIN','1082':None})})
        lou.put({'BOTSID':'HEA','ARTIKEL':lin.get({'BOTSID':'LIN','C212.7140':None})})
        lou.put({'BOTSID':'HEA','BESTELDAANTAL':lin.get({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'21','C186.6060':None})})
        lou.put({'BOTSID':'HEA','PROMOTIECODE':lin.get({'BOTSID':'LIN'},{'BOTSID':'RFF','C506.1153':'PD','C506.1154':None})})
        lou.put({'BOTSID':'HEA','ARTIKELOMSCHRIJVING':lin.get({'BOTSID':'LIN'},{'BOTSID':'IMD','C960.4294':None})})

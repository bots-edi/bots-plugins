#mapping-script
import bots.transform as transform

def main(inn,out):
    #process the lines in a loop (of course)
    headerwritten = False
    for lin in inn.getloop({'BOTSID':'HEA'}):
        if not headerwritten:
            out.ta_info['frompartner'] = lin.get({'BOTSID':'HEA','EANZENDER':None})
            out.ta_info['topartner'] = lin.get({'BOTSID':'HEA','EANONTVANGER':None})
            out.put({'BOTSID':'UNH','0062':out.ta_info['reference'],'S009.0065':'ORDERS','S009.0052':'D','S009.0054':'96A','S009.0051':'UN','S009.0057':'EAN008'})
            out.put({'BOTSID':'UNH'},{'BOTSID':'UNS','0081':'S'})
            out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':lin.get({'BOTSID':'HEA','ORDERNUMMER':None})})
            out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':lin.get({'BOTSID':'HEA','SOORTORDER':None})})
            out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'BO','C506.1154':lin.get({'BOTSID':'HEA','RAAMORDERNUMMER':None})})
            out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'PD','C506.1154':lin.get({'BOTSID':'HEA','ACTIENUMMER':None})})
            out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY','C082.3055':'9','C082.3039':lin.get({'BOTSID':'HEA','EANAFNEMER':None})})
            out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3055':'9','C082.3039':lin.get({'BOTSID':'HEA','EANLEVERANCIER':None})})
            out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'DP','C082.3055':'9','C082.3039':lin.get({'BOTSID':'HEA','EANAFLEVER':None})})
            out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SF','C082.3055':'9','C082.3039':lin.get({'BOTSID':'HEA','EANHAALADRES':None})})
            out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'UC','C082.3055':'9','C082.3039':lin.get({'BOTSID':'HEA','EANEINDBESTEMMING':None})})
            out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'IV','C082.3055':'9','C082.3039':lin.get({'BOTSID':'HEA','EANFACTUUR':None})})
                
            out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2379':'102','C507.2380':transform.strftime('%Y%m%d')})
            date = lin.get({'BOTSID':'HEA','LEVERDATUM':None})
            out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'2','C507.2379':transform.dateformat(date),'C507.2380':date})
            date = lin.get({'BOTSID':'HEA','VLEVERDATUM':None})
            out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'64','C507.2379':transform.dateformat(date),'C507.2380':date})
            date = lin.get({'BOTSID':'HEA','LLEVERDATUM':None})
            out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'63','C507.2379':transform.dateformat(date),'C507.2380':date})
                
            headerwritten = True

        lou = out.putloop({'BOTSID':'UNH'},{'BOTSID':'LIN'})
        lou.put({'BOTSID':'LIN','1082':lin.get({'BOTSID':'HEA','REGEL':None})})
        lou.put({'BOTSID':'LIN','C212.7143':'EN','C212.7140':lin.get({'BOTSID':'HEA','ARTIKEL':None})})
        lou.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'21','C186.6060':lin.get({'BOTSID':'HEA','BESTELDAANTAL':None})})
        lou.put({'BOTSID':'LIN'},{'BOTSID':'RFF','C506.1153':'PD','C506.1154':lin.get({'BOTSID':'HEA','PROMOTIECODE':None})})
        lou.put({'BOTSID':'LIN'},{'BOTSID':'IMD','C273.7008#1':lin.get({'BOTSID':'HEA','ARTIKELOMSCHRIJVING':None})})

    out.put({'BOTSID':'UNH'},{'BOTSID':'UNT','0074':out.getcount()+1,'0062':out.ta_info['reference']})  #last line (counts the segments produced in out-message

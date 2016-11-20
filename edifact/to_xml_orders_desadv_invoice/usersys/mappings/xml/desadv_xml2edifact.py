#mapping-script
import bots.transform as transform


def main(inn,out):
    out.put({'BOTSID':'UNH','0062':out.ta_info['reference'],'S009.0065':'DESADV','S009.0052':'D','S009.0054':'96A','S009.0051':'UN','S009.0057':'EAN005'})
    
    out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':inn.get({'BOTSID':'message','docsrt':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':inn.get({'BOTSID':'message','docnum':None})})
        
    date = inn.get({'BOTSID':'message','docdtm':None})
    out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2379':transform.dateformat(date),'C507.2380':date})
    date = inn.get({'BOTSID':'message','deldtm':None})
    out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'17','C507.2379':transform.dateformat(date),'C507.2380':date})
    date = inn.get({'BOTSID':'message','earldeldtm':None})
    out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'64','C507.2379':transform.dateformat(date),'C507.2380':date})
    date = inn.get({'BOTSID':'message','latedeldtm':None})
    out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'63','C507.2379':transform.dateformat(date),'C507.2380':date})
    date = inn.get({'BOTSID':'message','despatchdtm':None})
    out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'11','C507.2379':transform.dateformat(date),'C507.2380':date})
    date = inn.get({'BOTSID':'message','askeddeldtm':None})
    out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'2','C507.2379':transform.dateformat(date),'C507.2380':date})

    out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'ON','C506.1154':inn.get({'BOTSID':'message','byordnum':None})})
    if out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'VN','C506.1154':inn.get({'BOTSID':'message','suordnum':None})}):
        date = inn.get({'BOTSID':'message','suorddtm':None})
        out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'VN'},{'BOTSID':'DTM','C507.2005':'171','C507.2379':transform.dateformat(date),'C507.2380':date})
    
    for party in inn.getloop({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party'}):
        nad = out.putloop({'BOTSID':'UNH'},{'BOTSID':'NAD'})
        nad.put({'BOTSID':'NAD','3035':party.get({'BOTSID':'party','qual':None})})
        nad.put({'BOTSID':'NAD','C082.3055':'9','C082.3039':party.get({'BOTSID':'party','gln':None})})
        nad.put({'BOTSID':'NAD','C080.3036#1':party.get({'BOTSID':'party','name1':None})})
        nad.put({'BOTSID':'NAD','C080.3036#2':party.get({'BOTSID':'party','name2':None})})
        nad.put({'BOTSID':'NAD','C059.3042#1':party.get({'BOTSID':'party','address1':None})})
        nad.put({'BOTSID':'NAD','C059.3042#2':party.get({'BOTSID':'party','address2':None})})
        nad.put({'BOTSID':'NAD','C059.3042#3':party.get({'BOTSID':'party','address3':None})})
        nad.put({'BOTSID':'NAD','3164':party.get({'BOTSID':'party','city':None})})
        nad.put({'BOTSID':'NAD','3251':party.get({'BOTSID':'party','pcode':None})})
        nad.put({'BOTSID':'NAD','3207':party.get({'BOTSID':'party','country':None})})
        nad.put({'BOTSID':'NAD'},{'BOTSID':'RFF','C506.1153':'VA','C506.1154':party.get({'BOTSID':'party','vatnum':None})})
        nad.put({'BOTSID':'NAD'},{'BOTSID':'RFF','C506.1153':'API','C506.1154':party.get({'BOTSID':'party','externalID':None})})
        nad.put({'BOTSID':'NAD'},{'BOTSID':'RFF','C506.1153':'IT','C506.1154':party.get({'BOTSID':'party','internalID':None})})
        
        
    for cps in inn.getloop({'BOTSID':'message'},{'BOTSID':'cpss'},{'BOTSID':'cps'}):
        verzendregel  = out.putloop({'BOTSID':'UNH'},{'BOTSID':'CPS'})
        cpsline = cps.get({'BOTSID':'cps','line':None}) or '1'
        verzendregel.put({'BOTSID':'CPS','7164':cpsline})
        verzendregel.put({'BOTSID':'CPS','7166':cps.get({'BOTSID':'cps','subline':None})})

        for pac in cps.getloop({'BOTSID':'cps'},{'BOTSID':'pacs'},{'BOTSID':'pac'}):
            verpakking = verzendregel.putloop({'BOTSID':'CPS'},{'BOTSID':'PAC'})
            verpakking.put({'BOTSID':'PAC','7224':pac.get({'BOTSID':'pac','qua':None})})
            verpakking.put({'BOTSID':'PAC','C202.7065':pac.get({'BOTSID':'pac','iso':None})})
            verpakking.put({'BOTSID':'PAC'},{'BOTSID':'PCI','4233':'17'},{'BOTSID':'GIN','7405':'EU','C208#1.7402#1':pac.get({'BOTSID':'pac','gtin':None})})
            verpakking.put({'BOTSID':'PAC'},{'BOTSID':'PCI','4233':'33E'},{'BOTSID':'GIN','7405':'BJ','C208#1.7402#1':pac.get({'BOTSID':'pac','sscc':None})})
            verpakking.put({'BOTSID':'PAC'},{'BOTSID':'MEA','6311':'PD','C502.6313':'AAD','C174.6411':'KGM','C174.6314':pac.get({'BOTSID':'pac','brutweight':None})})
            #~ verpakking.put({'BOTSID':'PAC'},{'BOTSID':'MEA','6311':'PD','C502.6313':'AAD','C174.6411':'KGM','C174.6314':pac.get({'BOTSID':'pac','brutweight':None})})   #DE: per pac
            verpakking.put({'BOTSID':'PAC'},{'BOTSID':'MEA','6311':'PD','C502.6313':'AAW','C174.6411':'LTR','C174.6314':pac.get({'BOTSID':'pac','brutvolume':None})})
            verpakking.put({'BOTSID':'PAC'},{'BOTSID':'MEA','6311':'PD','C502.6313':'WD','C174.6411':'MTR','C174.6314':pac.get({'BOTSID':'pac','width':None})})
            verpakking.put({'BOTSID':'PAC'},{'BOTSID':'MEA','6311':'PD','C502.6313':'LN','C174.6411':'MTR','C174.6314':pac.get({'BOTSID':'pac','length':None})})
            verpakking.put({'BOTSID':'PAC'},{'BOTSID':'MEA','6311':'PD','C502.6313':'HT','C174.6411':'MTR','C174.6314':pac.get({'BOTSID':'pac','height':None})})
                
        for lin in cps.getloop({'BOTSID':'cps'},{'BOTSID':'lines'},{'BOTSID':'line'}):
            regel = verzendregel.putloop({'BOTSID':'CPS'},{'BOTSID':'LIN'})
            regel.put({'BOTSID':'LIN','1082':lin.get({'BOTSID':'line','num':None})})
            regel.put({'BOTSID':'LIN','C212.7143':'EN','C212.7140':lin.get({'BOTSID':'line','gtin':None})})
            regel.put({'BOTSID':'LIN'},{'BOTSID':'PIA','4347':'1','C212#1.7143':'SA','C212#1.7140':lin.get({'BOTSID':'line','suart':None})})
            regel.put({'BOTSID':'LIN'},{'BOTSID':'PIA','4347':'1','C212#1.7143':'IN','C212#1.7140':lin.get({'BOTSID':'line','byart':None})})
            regel.put({'BOTSID':'LIN'},{'BOTSID':'PIA','4347':'1','C212#1.7143':'NB','C212#1.7140':lin.get({'BOTSID':'line','batchnum':None})})
            regel.put({'BOTSID':'LIN'},{'BOTSID':'PIA','4347':'1','C212#1.7143':'SN','C212#1.7140':lin.get({'BOTSID':'line','serialnum':None})})
            regel.put({'BOTSID':'LIN'},{'BOTSID':'IMD','7077':'F','C273.7008#1':lin.get({'BOTSID':'line','desc':None})})
            regel.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'12','C186.6060':lin.get({'BOTSID':'line','delqua':None})})
            regel.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'21','C186.6411':lin.get({'BOTSID':'line','ordunit':None})})
            regel.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'192','C186.6060':lin.get({'BOTSID':'line','freequa':None})})
            regel.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'21','C186.6060':lin.get({'BOTSID':'line','ordqua':None})})
            regel.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'21','C186.6411':lin.get({'BOTSID':'line','ordunit':None})})
            date = lin.get({'BOTSID':'line','productiondtm':None})
            regel.put({'BOTSID':'LIN'},{'BOTSID':'DTM','C507.2005':'94','C507.2379':transform.dateformat(date),'C507.2380':date})
            date = lin.get({'BOTSID':'line','expirydtm':None})
            regel.put({'BOTSID':'LIN'},{'BOTSID':'PCI','4233':'17'},{'BOTSID':'DTM','C507.2005':'36','C507.2379':transform.dateformat(date),'C507.2380':date})
            date = lin.get({'BOTSID':'line','bestbeforedtm':None})
            regel.put({'BOTSID':'LIN'},{'BOTSID':'PCI','4233':'17'},{'BOTSID':'DTM','C507.2005':'23E','C507.2379':transform.dateformat(date),'C507.2380':date})
            regel.put({'BOTSID':'LIN'},{'BOTSID':'PCI','4233':'17'},{'BOTSID':'DTM','C507.2005':'361','C507.2379':transform.dateformat(date),'C507.2380':date})
            regel.put({'BOTSID':'LIN'},{'BOTSID':'PCI','4233':'36E'},{'BOTSID':'GIN','7405':'BX','C208#1.7402#1':lin.get({'BOTSID':'line','batchnumpac':None})})
    
    out.put({'BOTSID':'UNH'},{'BOTSID':'UNT','0074':out.getcount()+1,'0062':out.ta_info['reference']})  #last line (counts the segments produced in out-message)

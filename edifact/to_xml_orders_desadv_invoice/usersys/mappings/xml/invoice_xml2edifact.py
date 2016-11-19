#mapping-script
import bots.transform as transform


def main(inn,out):
    out.put({'BOTSID':'UNH','0062':out.ta_info['reference'],'S009.0065':'INVOIC','S009.0052':'D','S009.0054':'96A','S009.0051':'UN','S009.0057':'EAN008'})
    
    out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':inn.get({'BOTSID':'message','docsrt':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':inn.get({'BOTSID':'message','docnum':None})})
        
    date = inn.get({'BOTSID':'message','docdtm':None})
    out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2379':transform.dateformat(date),'C507.2380':date})
    date = inn.get({'BOTSID':'message','deldtm':None})
    out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'35','C507.2379':transform.dateformat(date),'C507.2380':date})

    out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'ON','C506.1154':inn.get({'BOTSID':'message','byordnum':None})})
    if out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'VN','C506.1154':inn.get({'BOTSID':'message','suordnum':None})}):
        date = inn.get({'BOTSID':'message','suorddtum':None})
        out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'VN'},{'BOTSID':'DTM','C507.2005':'171','C507.2379':transform.dateformat(date),'C507.2380':date})
    out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'AAK','C506.1154':inn.get({'BOTSID':'message','sudesnum':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'IV','C506.1154':inn.get({'BOTSID':'message','oriinvoicnum':None})})

    out.put({'BOTSID':'UNH'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','5305':inn.get({'BOTSID':'message','vatrate':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','C243.5278':inn.get({'BOTSID':'message','vatper':None})})
    
    out.put({'BOTSID':'UNH'},{'BOTSID':'CUX','C504#1.6347':'2','C504#1.6343':'4','C504#1.6345':inn.get({'BOTSID':'message','currency':None})})
    
    
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
       

    for falc in inn.getloop({'BOTSID':'message'},{'BOTSID':'alcs'},{'BOTSID':'alc'}):
        alc = out.putloop({'BOTSID':'UNH'},{'BOTSID':'ALC'})
        alc.put({'BOTSID':'ALC','5463':falc.get({'BOTSID':'alc','sign':None})})
        alc.put({'BOTSID':'ALC','C214.7161':falc.get({'BOTSID':'alc','srt':None})})
        alc.put({'BOTSID':'ALC','1227':falc.get({'BOTSID':'alc','calculationsequence':None})})
        alc.put({'BOTSID':'ALC'},{'BOTSID':'MOA','C516.5025':'8','C516.5004':falc.get({'BOTSID':'alc','mon':None})})
        alc.put({'BOTSID':'ALC'},{'BOTSID':'MOA','C516.5025':'25','C516.5004':falc.get({'BOTSID':'alc','basemon':None})})
        alc.put({'BOTSID':'ALC'},{'BOTSID':'PCD','C501.5245':'1','C501.5482':falc.get({'BOTSID':'alc','per':None})})
        alc.put({'BOTSID':'ALC'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','5305':falc.get({'BOTSID':'alc','vatrate':None})})
        alc.put({'BOTSID':'ALC'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','C243.5278':falc.get({'BOTSID':'alc','vatper':None})})


    for lin in inn.getloop({'BOTSID':'message'},{'BOTSID':'lines'},{'BOTSID':'line'}):
        regel = out.putloop({'BOTSID':'UNH'},{'BOTSID':'LIN'})
        regel.put({'BOTSID':'LIN','1082':lin.get({'BOTSID':'line','linenum':None})})
        regel.put({'BOTSID':'LIN','C212.7143':'EN','C212.7140':lin.get({'BOTSID':'line','gtin':None})})
        
        regel.put({'BOTSID':'LIN'},{'BOTSID':'PIA','4347':'1','C212#1.7143':'SA','C212#1.7140':lin.get({'BOTSID':'line','suart':None})})
        regel.put({'BOTSID':'LIN'},{'BOTSID':'PIA','4347':'1','C212#1.7143':'BP','C212#1.7140':lin.get({'BOTSID':'line','byart':None})})
            
        regel.put({'BOTSID':'LIN'},{'BOTSID':'IMD','7077':'F','C273.7008#1':lin.get({'BOTSID':'line','desc':None})})
        
        delunit = lin.get({'BOTSID':'line','delunit':None}) or 'PCE'
        regel.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'12','C186.6411':delunit,'C186.6060':lin.get({'BOTSID':'line','delqua':None})})
        regel.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'192','C186.6411':delunit,'C186.6060':lin.get({'BOTSID':'line','freequa':None})})
            
        priunit = lin.get({'BOTSID':'line','priunit':None}) or 'PCE'
        regel.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'47','C186.6411':priunit,'C186.6060':lin.get({'BOTSID':'line','invqua':None})})
        regel.put({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'AAB','C509.6411':priunit,'C509.5284':'1','C509.5118':lin.get({'BOTSID':'line','pricebrut':None})})
        regel.put({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'AAA','C509.6411':priunit,'C509.5284':'1','C509.5118':lin.get({'BOTSID':'line','pricenet':None})})
            
        regel.put({'BOTSID':'LIN'},{'BOTSID':'MOA','C516.5025':'203','C516.5004':lin.get({'BOTSID':'line','netmon':None})})

        regel.put({'BOTSID':'LIN'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','5305':lin.get({'BOTSID':'line','vatrate':None})})
        regel.put({'BOTSID':'LIN'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','C243.5278':lin.get({'BOTSID':'line','vatper':None})})

        for lalc in lin.getloop({'BOTSID':'line'},{'BOTSID':'alcs'},{'BOTSID':'alc'}):
            alc = regel.putloop({'BOTSID':'LIN'},{'BOTSID':'ALC'})
            alc.put({'BOTSID':'ALC','5463':lalc.get({'BOTSID':'alc','sign':None})})
            alc.put({'BOTSID':'ALC','C214.7161':lalc.get({'BOTSID':'alc','srt':None})})
            alc.put({'BOTSID':'ALC','1227':lalc.get({'BOTSID':'alc','calculationsequence':None})})
            alc.put({'BOTSID':'ALC'},{'BOTSID':'MOA','C516.5025':'8','C516.5004':lalc.get({'BOTSID':'alc','mon':None})})
            alc.put({'BOTSID':'ALC'},{'BOTSID':'MOA','C516.5025':'25','C516.5004':lalc.get({'BOTSID':'alc','basemon':None})})
            alc.put({'BOTSID':'ALC'},{'BOTSID':'PCD','C501.5245':'1','C501.5482':lalc.get({'BOTSID':'alc','per':None})})
            alc.put({'BOTSID':'ALC'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','5305':lalc.get({'BOTSID':'alc','vatrate':None})})
            alc.put({'BOTSID':'ALC'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','C243.5278':lalc.get({'BOTSID':'alc','vatper':None})})


    out.put({'BOTSID':'UNH'},{'BOTSID':'UNS','0081':'S'})
        
    out.put({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'79','C516.5004':inn.get({'BOTSID':'message','netmon':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'131','C516.5004':inn.get({'BOTSID':'message','alcmon':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'176','C516.5004':inn.get({'BOTSID':'message','vatmon':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'124','C516.5004':inn.get({'BOTSID':'message','vatmon':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'77','C516.5004':inn.get({'BOTSID':'message','invmon':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'125','C516.5004':inn.get({'BOTSID':'message','vatbasemon':None})})
            
    for sub in inn.getloop({'BOTSID':'message'},{'BOTSID':'subs'},{'BOTSID':'sub'}):
        tax = out.putloop({'BOTSID':'UNH'},{'BOTSID':'TAX','BOTSIDnr':'2','5283':'7','C241.5153':'VAT'})
        tax.put({'BOTSID':'TAX','BOTSIDnr':'2','5305':sub.get({'BOTSID':'sub','vatrate':None})})
        tax.put({'BOTSID':'TAX','BOTSIDnr':'2','C243.5278':sub.get({'BOTSID':'sub','vatper':None})})
        tax.put({'BOTSID':'TAX','BOTSIDnr':'2'},{'BOTSID':'MOA','C516.5025':'125','C516.5004':sub.get({'BOTSID':'sub','vatbasemon':None})})
        tax.put({'BOTSID':'TAX','BOTSIDnr':'2'},{'BOTSID':'MOA','C516.5025':'124','C516.5004':sub.get({'BOTSID':'sub','vatmon':None})})
    
    
    out.put({'BOTSID':'UNH'},{'BOTSID':'UNT','0074':out.getcount()+1,'0062':out.ta_info['reference']})  #last line (counts the segments produced in out-message)

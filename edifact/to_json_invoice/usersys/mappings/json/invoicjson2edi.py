#mapping-script
import bots.transform as transform

def main(inn,out):
    out.put({'BOTSID':'UNH'},{'BOTSID':'UNS','0081':'S'})
    out.put({'BOTSID':'UNH','0062':out.ta_info['reference'],'S009.0065':'INVOIC','S009.0052':'D','S009.0054':'96A','S009.0051':'UN','S009.0057':'EAN008'})
    out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','1225':'9','1004':inn.get({'BOTSID':'HEA','FACTUURNUMMER':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':inn.get({'BOTSID':'HEA','SOORTFACTUUR':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','4343':inn.get({'BOTSID':'HEA','ACCIJNSVRIJ':None})})
        
    date = inn.get({'BOTSID':'HEA','LEVERDATUM':None})
    out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'35','C507.2379':transform.dateformat(date),'C507.2380':date})
    out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2379':'102','C507.2380':transform.strftime('%Y%m%d')})
        
    out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'AAK','C506.1154':inn.get({'BOTSID':'HEA','VERZENDBERICHTNUMMER':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'ON','C506.1154':inn.get({'BOTSID':'HEA','ORDERNUMMERAFNEMER':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'IV','C506.1154':inn.get({'BOTSID':'HEA','CORFACTUURNUMMER':None})})
        
    if out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY','C082.3055':'9','C082.3039':inn.get({'BOTSID':'HEA','EANAFNEMER':None})}):
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY'},{'BOTSID':'RFF','C506.1153':'VA','C506.1154':inn.get({'BOTSID':'HEA','BTWAFNEMER':None})})
    if out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3055':'9','C082.3039':inn.get({'BOTSID':'HEA','EANLEVERANCIER':None})}):
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU'},{'BOTSID':'RFF','C506.1153':'VA','C506.1154':inn.get({'BOTSID':'HEA','BTWLEVERANCIER':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'DP','C082.3055':'9','C082.3039':inn.get({'BOTSID':'HEA','EANAFLEVER':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SF','C082.3055':'9','C082.3039':inn.get({'BOTSID':'HEA','EANHAALADRES':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'UC','C082.3055':'9','C082.3039':inn.get({'BOTSID':'HEA','EANEINDBESTEMMING':None})})
    if out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'IV','C082.3055':'9','C082.3039':inn.get({'BOTSID':'HEA','EANFACTUUR':None})}):
        out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'IV'},{'BOTSID':'RFF','C506.1153':'VA','C506.1154':inn.get({'BOTSID':'HEA','BTWFACTUUR':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'PE','C082.3055':'9','C082.3039':inn.get({'BOTSID':'HEA','EANBONTVANGER':None})})
        
    out.put({'BOTSID':'UNH'},{'BOTSID':'CUX','C504#1.6347':'2','C504#1.6343':'4','C504#1.6345':inn.get({'BOTSID':'HEA','VALUTA':None})})
        
    for alc in inn.getloop({'BOTSID':'HEA'},{'BOTSID':'HAL'}):
        hal = out.putloop({'BOTSID':'UNH'},{'BOTSID':'ALC'})
        hal.put({'BOTSID':'ALC','5463':alc.get({'BOTSID':'HAL','KORTINGTOESLAG':None})})
        hal.put({'BOTSID':'ALC','C214.7161':alc.get({'BOTSID':'HAL','SOORTKORTING':None})})
        hal.put({'BOTSID':'ALC'},{'BOTSID':'MOA','C516.5025':'8','C516.5004':alc.get({'BOTSID':'HAL','KORTINGSBEDRAG':None})})
        hal.put({'BOTSID':'ALC'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','C243.5278':alc.get({'BOTSID':'HAL','BTWPERCENTAGE':None})})
        hal.put({'BOTSID':'ALC'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','5305':alc.get({'BOTSID':'HAL','BTWTARIEF':None})})

    for lin in inn.getloop({'BOTSID':'HEA'},{'BOTSID':'LIN'}):
        lou = out.putloop({'BOTSID':'UNH'},{'BOTSID':'LIN'})
        lou.put({'BOTSID':'LIN','1082':lin.get({'BOTSID':'LIN','REGEL':None})})
        lou.put({'BOTSID':'LIN','C212.7143':'EN','C212.7140':lin.get({'BOTSID':'LIN','ARTIKEL':None})})
        lou.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'47','C186.6060':lin.get({'BOTSID':'LIN','GEFACTAANTAL':None})})
        lou.put({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'12','C186.6060':lin.get({'BOTSID':'LIN','GELEVERDAANTAL':None})})
        lou.put({'BOTSID':'LIN'},{'BOTSID':'RFF','C506.1153':'PD','C506.1154':lin.get({'BOTSID':'LIN','PROMOTIECODE':None})})
        lou.put({'BOTSID':'LIN'},{'BOTSID':'IMD','C960.4294':lin.get({'BOTSID':'LIN','ARTIKELOMSCHRIJVING':None})})
        lou.put({'BOTSID':'LIN'},{'BOTSID':'MOA','C516.5025':'203','C516.5004':lin.get({'BOTSID':'LIN','NETTOREGELBEDRAG':None})})
        if lou.put({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'INV','C509.5118':lin.get({'BOTSID':'LIN','PRIJS':None})}):
            lou.put({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'INV','C509.5284':lin.getnozero({'BOTSID':'LIN','AANTALPRIJSBASIS':None})})
            lou.put({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'INV','C509.6411':lin.get({'BOTSID':'LIN','EENHEIDPRIJSBASIS':None})})
        if lou.put({'BOTSID':'LIN'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','5305':lin.get({'BOTSID':'LIN','BTWTARIEF':None})}):
            lou.put({'BOTSID':'LIN'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','C243.5278':lin.get({'BOTSID':'LIN','BTWPERCENTAGE':None})})

        for alc in lin.getloop({'BOTSID':'LIN'},{'BOTSID':'LAL'}):
            lal = lou.putloop({'BOTSID':'LIN'},{'BOTSID':'ALC'})
            lal.put({'BOTSID':'ALC','5463':alc.get({'BOTSID':'LAL','KORTINGTOESLAG':None})})
            lal.put({'BOTSID':'ALC','C214.7161':alc.get({'BOTSID':'LAL','SOORTKORTING':None})})
            lal.put({'BOTSID':'ALC'},{'BOTSID':'MOA','C516.5025':'8','C516.5004':alc.get({'BOTSID':'LAL','KORTINGSBEDRAG':None})})
            if lal.put({'BOTSID':'ALC'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','5305':alc.get({'BOTSID':'LAL','BTWTARIEF':None})}):
                lal.put({'BOTSID':'ALC'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','C243.5278':alc.get({'BOTSID':'LAL','BTWPERCENTAGE':None})})

    out.put({'BOTSID':'UNH'},{'BOTSID':'UNS','0081':'S'})
    out.put({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'79','C516.5004':inn.get({'BOTSID':'HEA'},{'BOTSID':'TOT','TOTAALREGEL':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'131','C516.5004':inn.getnozero({'BOTSID':'HEA'},{'BOTSID':'TOT','TOTAALFACTUURKORTING':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'176','C516.5004':inn.get({'BOTSID':'HEA'},{'BOTSID':'TOT','TOTAALBTW':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'77','C516.5004':inn.get({'BOTSID':'HEA'},{'BOTSID':'TOT','TOTAALFACTUUR':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'129','C516.5004':inn.getnozero({'BOTSID':'HEA'},{'BOTSID':'TOT','GRONDSLAGBETKORTING':None})})
    
    out.put({'BOTSID':'UNH'},{'BOTSID':'TAX','BOTSIDnr':'2','5283':'7','C241.5153':'VAT','5305':inn.get({'BOTSID':'HEA'},{'BOTSID':'TOT','BTWTARIEF1':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'TAX','BOTSIDnr':'2','5283':'7','C241.5153':'VAT','C243.5278':inn.get({'BOTSID':'HEA'},{'BOTSID':'TOT','BTWPERCENTAGE1':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'TAX','BOTSIDnr':'2','5283':'7','C241.5153':'VAT'},{'BOTSID':'MOA','C516.5025':'125','C516.5004':inn.get({'BOTSID':'HEA'},{'BOTSID':'TOT','BTWGRONDSLAG1':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'TAX','BOTSIDnr':'2','5283':'7','C241.5153':'VAT'},{'BOTSID':'MOA','C516.5025':'124','C516.5004':inn.get({'BOTSID':'HEA'},{'BOTSID':'TOT','BTWBEDRAG1':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'UNT','0074':out.getcount()+1,'0062':out.ta_info['reference']})

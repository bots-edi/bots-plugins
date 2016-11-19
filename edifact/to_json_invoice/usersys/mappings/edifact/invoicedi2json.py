#mapping-script

def main(inn,out):
    out.put({'BOTSID':'HEA','SOORT':'INVOICD96AUNEAN008'})
    out.put({'BOTSID':'HEA','EANZENDER':inn.ta_info['frompartner']})
    out.put({'BOTSID':'HEA','EANONTVANGER':inn.ta_info['topartner']})
    out.put({'BOTSID':'HEA','TEST':inn.ta_info['testindicator']})
    out.put({'BOTSID':'HEA','FACTUURNUMMER':inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':None})})
    out.put({'BOTSID':'HEA','SOORTFACTUUR':inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':None})})
        
    FACTUURDATUM = inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2380':None})
    if FACTUURDATUM:
        out.put({'BOTSID':'HEA','FACTUURDATUM':FACTUURDATUM[:8]})
    out.put({'BOTSID':'HEA','LEVERDATUM':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'35','C507.2380':None})})
            
    out.put({'BOTSID':'HEA','VERZENDBERICHTNUMMER':inn.get({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'AAK','C506.1154':None})})
    out.put({'BOTSID':'HEA','ORDERNUMMERAFNEMER':inn.get({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'ON','C506.1154':None})})
    out.put({'BOTSID':'HEA','CORFACTUURNUMMER':inn.get({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'IV','C506.1154':None})})
        
    out.put({'BOTSID':'HEA','EANAFNEMER':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY','C082.3039':None})})
    out.put({'BOTSID':'HEA','BTWAFNEMER':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY'},{'BOTSID':'RFF','C506.1153':'VA','C506.1154':None})})
    out.put({'BOTSID':'HEA','EANLEVERANCIER':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3039':None})})
    out.put({'BOTSID':'HEA','BTWLEVERANCIER':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU'},{'BOTSID':'RFF','C506.1153':'VA','C506.1154':None})})
    out.put({'BOTSID':'HEA','EANAFLEVER':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'DP','C082.3039':None})})
    out.put({'BOTSID':'HEA','EANHAALADRES':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SF','C082.3039':None})})
    out.put({'BOTSID':'HEA','EANEINDBESTEMMING':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'UC','C082.3039':None})})
    out.put({'BOTSID':'HEA','EANFACTUUR':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'IV','C082.3039':None})})
    out.put({'BOTSID':'HEA','BTWFACTUUR':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'IV'},{'BOTSID':'RFF','C506.1153':'VA','C506.1154':None})})
    out.put({'BOTSID':'HEA','EANBONTVANGER':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'PE','C082.3039':None})})
        
    out.put({'BOTSID':'HEA','ACCIJNSVRIJ':inn.get({'BOTSID':'UNH'},{'BOTSID':'TAX','5283':'7','C241.5153':'ACT','5305':'E'})})
    out.put({'BOTSID':'HEA','VALUTA':inn.get({'BOTSID':'UNH'},{'BOTSID':'CUX','C504#1.6347':'2','C504#1.6343':'4','C504#1.6345':None})})
        
    out.put({'BOTSID':'HEA','DAGNAFACTUUR1':inn.get({'BOTSID':'UNH'},{'BOTSID':'PAT','4279':'22','C112.2475':'5','C112.2009':'3','C112.2151':'D','C112.2152':None})})
    out.put({'BOTSID':'HEA','PERCENTKORTING1':inn.get({'BOTSID':'UNH'},{'BOTSID':'PAT','4279':'22','C112.2475':'5','C112.2009':'3','C112.2151':'D'},{'BOTSID':'PCD','C501.5245':'12','C501.5482':None})})
    
    for alc in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'ALC'}):
        hal = out.putloop({'BOTSID':'HEA'},{'BOTSID':'HAL'})
        hal.put({'BOTSID':'HAL','KORTINGTOESLAG':alc.get({'BOTSID':'ALC','5463':None})})
        hal.put({'BOTSID':'HAL','SOORTKORTING':alc.get({'BOTSID':'ALC','C214.7161':None})})
        hal.put({'BOTSID':'HAL','KORTINGSBEDRAG':alc.get({'BOTSID':'ALC'},{'BOTSID':'MOA','C516.5025':'8','C516.5004':None})})
        hal.put({'BOTSID':'HAL','BTWPERCENTAGE':alc.get({'BOTSID':'ALC'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','C243.5278':None})})
        hal.put({'BOTSID':'HAL','BTWTARIEF':alc.get({'BOTSID':'ALC'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','5305':None})})
            
    inn.sort({'BOTSID':'UNH'},{'BOTSID':'LIN','C212.7140':None})    #sort the article lines on article number. 

    for lin in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'LIN'}):
        lou = out.putloop({'BOTSID':'HEA'},{'BOTSID':'LIN'})
        lou.put({'BOTSID':'LIN','REGEL':lin.get({'BOTSID':'LIN','1082':None})})
        lou.put({'BOTSID':'LIN','ARTIKEL':lin.get({'BOTSID':'LIN','C212.7140':None})})
        lou.put({'BOTSID':'LIN','GEFACTAANTAL':lin.get({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'47','C186.6060':None})})
        lou.put({'BOTSID':'LIN','GELEVERDAANTAL':lin.get({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'12','C186.6060':None})})
        lou.put({'BOTSID':'LIN','PROMOTIECODE':lin.get({'BOTSID':'LIN'},{'BOTSID':'RFF','C506.1153':'PD','C506.1154':None})})
        lou.put({'BOTSID':'LIN','ARTIKELOMSCHRIJVING':lin.get({'BOTSID':'LIN'},{'BOTSID':'IMD','C273.7008#1':None})})
        lou.put({'BOTSID':'LIN','NETTOREGELBEDRAG':lin.get({'BOTSID':'LIN'},{'BOTSID':'MOA','C516.5025':'203','C516.5004':None})})
        lou.put({'BOTSID':'LIN','PRIJS':lin.get({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'INV','C509.5118':None})})
        lou.put({'BOTSID':'LIN','AANTALPRIJSBASIS':lin.get({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'INV','C509.5284':None})})
        lou.put({'BOTSID':'LIN','EENHEIDPRIJSBASIS':lin.get({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'INV','C509.6411':None})})
        lou.put({'BOTSID':'LIN','BTWTARIEF':lin.get({'BOTSID':'LIN'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','5305':None})})
        lou.put({'BOTSID':'LIN','BTWPERCENTAGE':lin.get({'BOTSID':'LIN'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','C243.5278':None})})

        for alc in lin.getloop({'BOTSID':'LIN'},{'BOTSID':'ALC'}):
            lal = lou.putloop({'BOTSID':'LIN'},{'BOTSID':'LAL'})
            lal.put({'BOTSID':'LAL','KORTINGTOESLAG':alc.get({'BOTSID':'ALC','5463':None})})
            lal.put({'BOTSID':'LAL','SOORTKORTING':alc.get({'BOTSID':'ALC','C214.7161':None})})
            lal.put({'BOTSID':'LAL','KORTINGSBEDRAG':alc.get({'BOTSID':'ALC'},{'BOTSID':'MOA','C516.5025':'8','C516.5004':None})})
            lal.put({'BOTSID':'LAL','BTWPERCENTAGE':alc.get({'BOTSID':'ALC'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','C243.5278':None})})
            lal.put({'BOTSID':'LAL','BTWTARIEF':alc.get({'BOTSID':'ALC'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','5305':None})})

    out.put({'BOTSID':'HEA'},{'BOTSID':'TOT','TOTAALREGEL':inn.get({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'79','C516.5004':None})})
    out.put({'BOTSID':'HEA'},{'BOTSID':'TOT','TOTAALFACTUURKORTING':inn.get({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'131','C516.5004':None})})
    out.put({'BOTSID':'HEA'},{'BOTSID':'TOT','TOTAALBTW':inn.get({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'176','C516.5004':None})})
    out.put({'BOTSID':'HEA'},{'BOTSID':'TOT','TOTAALFACTUUR':inn.get({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'77','C516.5004':None})})
    out.put({'BOTSID':'HEA'},{'BOTSID':'TOT','GRONDSLAGBETKORTING':inn.get({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'129','C516.5004':None})})
    
    out.put({'BOTSID':'HEA'},{'BOTSID':'TOT','BTWTARIEF1':inn.get({'BOTSID':'UNH'},{'BOTSID':'TAX','BOTSIDnr':'2','5283':'7','C241.5153':'VAT','5305':None})})
    out.put({'BOTSID':'HEA'},{'BOTSID':'TOT','BTWPERCENTAGE1':inn.get({'BOTSID':'UNH'},{'BOTSID':'TAX','BOTSIDnr':'2','5283':'7','C241.5153':'VAT','C243.5278':None})})
    out.put({'BOTSID':'HEA'},{'BOTSID':'TOT','BTWGRONDSLAG1':inn.get({'BOTSID':'UNH'},{'BOTSID':'TAX','BOTSIDnr':'2','5283':'7','C241.5153':'VAT'},{'BOTSID':'MOA','C516.5025':'125','C516.5004':None})})
    out.put({'BOTSID':'HEA'},{'BOTSID':'TOT','BTWBEDRAG1':inn.get({'BOTSID':'UNH'},{'BOTSID':'TAX','BOTSIDnr':'2','5283':'7','C241.5153':'VAT'},{'BOTSID':'MOA','C516.5025':'124','C516.5004':None})})

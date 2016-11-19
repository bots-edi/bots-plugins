#mapping-script

def main(inn,out):
    out.put({'BOTSID':'HEA','SOORT':'INVOICD96AUNEAN008'})
    out.put({'BOTSID':'HEA','EANZENDER':inn.ta_info['frompartner']})
    out.put({'BOTSID':'HEA','EANONTVANGER':inn.ta_info['topartner']})
    out.put({'BOTSID':'HEA','TEST':inn.ta_info['testindicator']})
    out.put({'BOTSID':'HEA','FACTUURNUMMER':inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':None})})
    out.put({'BOTSID':'HEA','SOORTFACTUUR':inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':None})})
    HEA__RECORDATTRIBUTE = inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1000':None}) or 'TESTRECORDATTR'
    out.put({'BOTSID':'HEA','HEA__RECORDATTRIBUTE':HEA__RECORDATTRIBUTE})   #test HEA__RECORDATTRIBUTE
        
    FACTUURDATUM = inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2380':None})
    if FACTUURDATUM:
        out.put({'BOTSID':'HEA','FACTUURDATUM':FACTUURDATUM[:8],'FACTUURDATUM__FIELDATTRIBUTE':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2379':None})}) #test FACTUURDATUM__FIELDATTRIBUTE
    out.put({'BOTSID':'HEA','XXXDATUM':'' ,'XXXDATUM__FIELDATTRIBUTE':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'XXX','C507.2379':None})}) #test XXXDATUM__FIELDATTRIBUTE xml element has no content
            
    out.put({'BOTSID':'HEA','ORDERNUMMERAFNEMER':inn.get({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'ON','C506.1154':None})})
        
    out.put({'BOTSID':'HEA','EANAFNEMER':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY','C082.3039':None})})
    out.put({'BOTSID':'HEA','BTWAFNEMER':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY'},{'BOTSID':'RFF','C506.1153':'VA','C506.1154':None})})
    out.put({'BOTSID':'HEA','EANLEVERANCIER':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3039':None})})
    out.put({'BOTSID':'HEA','BTWLEVERANCIER':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU'},{'BOTSID':'RFF','C506.1153':'VA','C506.1154':None})})
    out.put({'BOTSID':'HEA','EANAFLEVER':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'DP','C082.3039':None})})
    out.put({'BOTSID':'HEA','EANFACTUUR':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'IV','C082.3039':None})})
        
    out.put({'BOTSID':'HEA','VALUTA':inn.get({'BOTSID':'UNH'},{'BOTSID':'CUX','C504#1.6347':'2','C504#1.6343':'4','C504#1.6345':None})})


    for lin in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'LIN'}):
        lou = out.putloop({'BOTSID':'HEA'},{'BOTSID':'LIN'})
        lou.put({'BOTSID':'LIN','REGEL':lin.get({'BOTSID':'LIN','1082':None})})
        lou.put({'BOTSID':'LIN','ARTIKEL':lin.get({'BOTSID':'LIN','C212.7140':None})})
        lou.put({'BOTSID':'LIN','GEFACTAANTAL':lin.get({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'47','C186.6060':None})})
        lou.put({'BOTSID':'LIN','GELEVERDAANTAL':lin.get({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'12','C186.6060':None})})
        lou.put({'BOTSID':'LIN','NETTOREGELBEDRAG':lin.get({'BOTSID':'LIN'},{'BOTSID':'MOA','C516.5025':'203','C516.5004':None})})
        lou.put({'BOTSID':'LIN','PRIJS':lin.get({'BOTSID':'LIN'},{'BOTSID':'PRI','C509.5125':'INV','C509.5118':None})})
        lou.put({'BOTSID':'LIN','BTWTARIEF':lin.get({'BOTSID':'LIN'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','5305':None})})
        lou.put({'BOTSID':'LIN','BTWPERCENTAGE':lin.get({'BOTSID':'LIN'},{'BOTSID':'TAX','5283':'7','C241.5153':'VAT','C243.5278':None})})


    out.put({'BOTSID':'HEA','TOTAALREGEL':inn.get({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'79','C516.5004':None})})
    out.put({'BOTSID':'HEA','TOTAALBTW':inn.get({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'176','C516.5004':None})})
    out.put({'BOTSID':'HEA','TOTAALFACTUUR':inn.get({'BOTSID':'UNH'},{'BOTSID':'MOA','C516.5025':'77','C516.5004':None})})
    
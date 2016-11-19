#mapping-script

def main(inn,out):
    out.put({'BOTSID':'HEA','EANZENDER':inn.ta_info['frompartner']})
    out.put({'BOTSID':'HEA','EANONTVANGER':inn.ta_info['topartner']})
    out.put({'BOTSID':'HEA','TEST':inn.ta_info['testindicator']})
    out.put({'BOTSID':'HEA','SOORT':'ORDERSD96AUNEAN008'})
    
    out.put({'BOTSID':'HEA','ORDERNUMMER':inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':None})})
    out.put({'BOTSID':'HEA','SOORTORDER':inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':None})})
    
    out.put({'BOTSID':'HEA','ORDERDATUM':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2380':None})})
    out.put({'BOTSID':'HEA','LEVERDATUM':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'2','C507.2380':None})})
    out.put({'BOTSID':'HEA','VLEVERDATUM':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'64','C507.2380':None})})
    out.put({'BOTSID':'HEA','LLEVERDATUM':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'63','C507.2380':None})})
    
    out.put({'BOTSID':'HEA','RAAMORDERNUMMER':inn.get({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'BO','C506.1154':None})})
    out.put({'BOTSID':'HEA','ACTIENUMMER':inn.get({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'PD','C506.1154':None})})
    
    out.put({'BOTSID':'HEA','EANAFNEMER':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY','C082.3039':None})})
    out.put({'BOTSID':'HEA','EANLEVERANCIER':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3039':None})})
    out.put({'BOTSID':'HEA','EANAFLEVER':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'DP','C082.3039':None})})
    out.put({'BOTSID':'HEA','EANHAALADRES':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SF','C082.3039':None})})
    out.put({'BOTSID':'HEA','EANEINDBESTEMMING':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'UC','C082.3039':None})})
    out.put({'BOTSID':'HEA','EANFACTUUR':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'IV','C082.3039':None})})
    
    if inn.get({'BOTSID':'UNH'},{'BOTSID':'TAX','5283':'7','C241.5153':'ACT','5305':'E'}):
        out.put({'BOTSID':'HEA','ACCIJNSVRIJ':'E'})
    if inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','1225':'46'}):
        out.put({'BOTSID':'HEA','GEIMPROVISEERD':'46'})
    if inn.get({'BOTSID':'UNH'},{'BOTSID':'TOD','4055':'4'}):
        out.put({'BOTSID':'HEA','BACKHAULING':'4'})
    if inn.get({'BOTSID':'UNH'},{'BOTSID':'TOD','4055':'02E'}):
        out.put({'BOTSID':'HEA','SPOEDORDER':'02E'})
    if inn.get({'BOTSID':'UNH'},{'BOTSID':'ALI','4183#1':'NUL'}):
        out.put({'BOTSID':'HEA','NULORDER':NUL})
    if inn.get({'BOTSID':'UNH'},{'BOTSID':'ALI','4183#1':'77E'}):
        out.put({'BOTSID':'HEA','WINKELINSTALLATIE':'77E'})

    for lin in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'LIN'}):
        lou = out.putloop({'BOTSID':'HEA'},{'BOTSID':'LIN'})
        lou.put({'BOTSID':'LIN','REGEL':lin.get({'BOTSID':'LIN','1082':None})})
        lou.put({'BOTSID':'LIN','ARTIKEL':lin.get({'BOTSID':'LIN','C212.7140':None})})
        lou.put({'BOTSID':'LIN','BESTELDAANTAL':lin.get({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'21','C186.6060':None})})
        lou.put({'BOTSID':'LIN','PROMOTIECODE':lin.get({'BOTSID':'LIN'},{'BOTSID':'RFF','C506.1153':'PD','C506.1154':None})})
        lou.put({'BOTSID':'LIN','ARTIKELOMSCHRIJVING':lin.get({'BOTSID':'LIN'},{'BOTSID':'IMD','C273.7008#1':None})})

    # check if an APERAK is returned or not
    if inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','4343':'AB'}):
        out.put({'BOTSID':'HEA','INDICATIEONTVANGSTBEVESTIGING':'AB'})
        return 'edifactorders2aperak'
    else:
        return None

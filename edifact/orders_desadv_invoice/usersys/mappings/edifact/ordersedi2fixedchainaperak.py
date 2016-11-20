#mapping-script

def main(inn,out):
    terug = None
    out.put({'BOTSID':'HEA','EANZENDER':inn.ta_info['frompartner']})
    out.put({'BOTSID':'HEA','EANONTVANGER':inn.ta_info['topartner']})
    out.put({'BOTSID':'HEA','TEST':inn.ta_info['testindicator']})
    out.put({'BOTSID':'HEA','SOORT':'ORDERSD96AUNEAN008'})
    reference = inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':None})
    out.put({'BOTSID':'HEA','ORDERNUMMER':reference})
    out.ta_info['reference']=reference
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
    ACCIJNSVRIJ = inn.get({'BOTSID':'UNH'},{'BOTSID':'TAX','5283':'7','C241.5153':'ACT','5305':None})
    if ACCIJNSVRIJ == 'E':
        out.put({'BOTSID':'HEA','ACCIJNSVRIJ':ACCIJNSVRIJ})
    GEIMPROVISEERD = inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','1225':None})
    if GEIMPROVISEERD == '46':
        out.put({'BOTSID':'HEA','GEIMPROVISEERD':GEIMPROVISEERD})
    INDICATIEONTVANGSTBEVESTIGING = inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','4343':None})
    if INDICATIEONTVANGSTBEVESTIGING == 'AB':
        out.put({'BOTSID':'HEA','INDICATIEONTVANGSTBEVESTIGING':INDICATIEONTVANGSTBEVESTIGING})
        terug = 'edifactorders2aperak'
    for tod in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'TOD'}):
        TODVAR = tod.get({'BOTSID':'TOD','4055':None})
        if TODVAR == '4':
            out.put({'BOTSID':'HEA','BACKHAULING':TODVAR})
        if TODVAR == '02E':
            out.put({'BOTSID':'HEA','SPOEDORDER':TODVAR})
    for ali in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'ALI'}):
        FIELD = ali.get({'BOTSID':'ALI','4183#1':None})
        if FIELD == 'NUL':
            out.put({'BOTSID':'HEA','NULORDER':FIELD})
        if FIELD == '77E':
            out.put({'BOTSID':'HEA','WINKELINSTALLATIE':FIELD})

    for lin in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'LIN'}):
        lou = out.putloop({'BOTSID':'HEA'},{'BOTSID':'LIN'})
        lou.put({'BOTSID':'LIN','REGEL':lin.get({'BOTSID':'LIN','1082':None})})
        lou.put({'BOTSID':'LIN','ARTIKEL':lin.get({'BOTSID':'LIN','C212.7140':None})})
        lou.put({'BOTSID':'LIN','BESTELDAANTAL':lin.get({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'21','C186.6060':None})})
        lou.put({'BOTSID':'LIN','PROMOTIECODE':lin.get({'BOTSID':'LIN'},{'BOTSID':'RFF','C506.1153':'PD','C506.1154':None})})
        lou.put({'BOTSID':'LIN','ARTIKELOMSCHRIJVING':lin.get({'BOTSID':'LIN'},{'BOTSID':'IMD','C960.4294':None})})
    return terug

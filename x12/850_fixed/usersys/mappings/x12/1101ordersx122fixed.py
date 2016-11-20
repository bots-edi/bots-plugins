#mapping-script

def main(inn,out):
    #~ print 'in 1101ordersx122fixed.py'
    out.put({'BOTSID':'HEA','EANZENDER':inn.ta_info['frompartner']})
    out.put({'BOTSID':'HEA','EANONTVANGER':inn.ta_info['topartner']})
    #~ out.put({'BOTSID':'HEA','TEST':inn.ta_info['testindicator']})
    #~ out.put({'BOTSID':'HEA','SOORT':'ORDERSD96AUNEAN008'})
    reference = inn.get({'BOTSID':'ST'},{'BOTSID':'BEG','BEG03':None})
    out.put({'BOTSID':'HEA','ORDERNUMMER':reference})
    out.ta_info['reference']=reference
    out.put({'BOTSID':'HEA','SOORTORDER':inn.get({'BOTSID':'ST'},{'BOTSID':'BEG','BEG02':None})})
    out.put({'BOTSID':'HEA','ORDERDATUM':inn.get({'BOTSID':'ST'},{'BOTSID':'BEG','BEG04':None})})
    out.put({'BOTSID':'HEA','LEVERDATUM':inn.get({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'002','DTM02':None})})
    #~ out.put({'BOTSID':'HEA','VLEVERDATUM':inn.get({'BOTSID':'ST'},{'BOTSID':'DTM','C507.2005':'64','C507.2380':None})})
    #~ out.put({'BOTSID':'HEA','LLEVERDATUM':inn.get({'BOTSID':'ST'},{'BOTSID':'DTM','C507.2005':'63','C507.2380':None})})
    #~ out.put({'BOTSID':'HEA','RAAMORDERNUMMER':inn.get({'BOTSID':'ST'},{'BOTSID':'RFF','C506.1153':'BO','C506.1154':None})})
    #~ out.put({'BOTSID':'HEA','ACTIENUMMER':inn.get({'BOTSID':'ST'},{'BOTSID':'RFF','C506.1153':'PD','C506.1154':None})})
    out.put({'BOTSID':'HEA','EANAFNEMER':inn.get({'BOTSID':'ST'},{'BOTSID':'N1','N101':'BY','N4':None})})
    #~ out.put({'BOTSID':'HEA','EANLEVERANCIER':inn.get({'BOTSID':'ST'},{'BOTSID':'NAD','3035':'SU','C082.3039':None})})
    out.put({'BOTSID':'HEA','EANAFLEVER':inn.get({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST','N4':None})})
    out.put({'BOTSID':'HEA','EANHAALADRES':inn.get({'BOTSID':'ST'},{'BOTSID':'N1','N101':'SF','N4':None})})
    #~ out.put({'BOTSID':'HEA','EANEINDBESTEMMING':inn.get({'BOTSID':'ST'},{'BOTSID':'NAD','3035':'UC','C082.3039':None})})
    #~ out.put({'BOTSID':'HEA','EANFACTUUR':inn.get({'BOTSID':'ST'},{'BOTSID':'NAD','3035':'IV','C082.3039':None})})
    #~ INDICATIEONTVANGSTBEVESTIGING = inn.get({'BOTSID':'ST'},{'BOTSID':'BGM','4343':None})
    #~ if INDICATIEONTVANGSTBEVESTIGING == 'AB':
        #~ out.put({'BOTSID':'HEA','INDICATIEONTVANGSTBEVESTIGING':INDICATIEONTVANGSTBEVESTIGING})

    for po1 in inn.getloop({'BOTSID':'ST'},{'BOTSID':'PO1'}):
        lou = out.putloop({'BOTSID':'HEA'},{'BOTSID':'LIN'})
        lou.put({'BOTSID':'LIN','REGEL':po1.get({'BOTSID':'PO1','PO101':None})})
        lou.put({'BOTSID':'LIN','ARTIKEL':po1.get({'BOTSID':'PO1','PO107':None})})
        lou.put({'BOTSID':'LIN','BESTELDAANTAL':po1.get({'BOTSID':'PO1','PO102':None})})
        #~ lou.put({'BOTSID':'PO1','PROMOTIECODE':po1.get({'BOTSID':'PO1'},{'BOTSID':'RFF','C506.1153':'PD','C506.1154':None})})
        lou.put({'BOTSID':'LIN','ARTIKELOMSCHRIJVING':po1.get({'BOTSID':'PO1'},{'BOTSID':'PID','PID05':None})})

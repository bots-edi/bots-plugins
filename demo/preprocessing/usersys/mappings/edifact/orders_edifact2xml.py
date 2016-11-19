#mapping-script

def main(inn,out):
    out.put({'BOTSID':'message','sender':inn.ta_info['frompartner']})
    out.put({'BOTSID':'message','receiver':inn.ta_info['topartner']})
    out.put({'BOTSID':'message','testindicator':inn.ta_info['testindicator']})  #in production there is no test-indicator...in xml this ends up as an empty xml element

    out.put({'BOTSID':'message','docsrt':inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':None})})
    reference = inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':None})
    out.ta_info['reference']=reference
    out.put({'BOTSID':'message','docnum':reference})
    
    out.put({'BOTSID':'message','docdtm':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2380':None})})
    out.put({'BOTSID':'message','deldtm':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'2','C507.2380':None})})
    out.put({'BOTSID':'message','earldeldtm':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'64','C507.2380':None})})
    out.put({'BOTSID':'message','latedeldtm':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'63','C507.2380':None})})

    out.put({'BOTSID':'message','currency':inn.get({'BOTSID':'UNH'},{'BOTSID':'CUX','C504#1.6347':'2','C504#1.6343':'9','C504#1.6345':None})})

    #handle parties
    for nad in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'NAD'}):
        party = out.putloop({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party'})
        party.put({'BOTSID':'party','qual':nad.get({'BOTSID':'NAD','3035':None})})
        party.put({'BOTSID':'party','gln':nad.get({'BOTSID':'NAD','C082.3039':None})})
        party.put({'BOTSID':'party','name1':nad.get({'BOTSID':'NAD','C080.3036#1':None})})
        party.put({'BOTSID':'party','name2':nad.get({'BOTSID':'NAD','C080.3036#2':None})})
        party.put({'BOTSID':'party','address1':nad.get({'BOTSID':'NAD','C059.3042#1':None})})
        party.put({'BOTSID':'party','address2':nad.get({'BOTSID':'NAD','C059.3042#2':None})})
        party.put({'BOTSID':'party','address3':nad.get({'BOTSID':'NAD','C059.3042#3':None})})
        party.put({'BOTSID':'party','city':nad.get({'BOTSID':'NAD','3164':None})})
        party.put({'BOTSID':'party','pcode':nad.get({'BOTSID':'NAD','3251':None})})
        party.put({'BOTSID':'party','country':nad.get({'BOTSID':'NAD','3207':None})})
        
        party.put({'BOTSID':'party','vatnum':nad.get({'BOTSID':'NAD'},{'BOTSID':'RFF','C506.1153':'VA','C506.1154':None})})
        party.put({'BOTSID':'party','externalID':nad.get({'BOTSID':'NAD'},{'BOTSID':'RFF','C506.1153':'API','C506.1154':None})})
        party.put({'BOTSID':'party','internalID':nad.get({'BOTSID':'NAD'},{'BOTSID':'RFF','C506.1153':'IT','C506.1154':None})})
       

    #handle lines
    for lin in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'LIN'}):
        regel = out.putloop({'BOTSID':'message'},{'BOTSID':'lines'},{'BOTSID':'line'})
        regel.put({'BOTSID':'line','linenum':lin.get({'BOTSID':'LIN','1082':None})})
        regel.put({'BOTSID':'line','gtin':lin.get({'BOTSID':'LIN','C212.7143':'EN','C212.7140':None})})
        regel.put({'BOTSID':'line','ordqua':lin.get({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'21','C186.6060':None})})
        regel.put({'BOTSID':'line','ordunit':lin.get({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'21','C186.6411':None})})
        regel.put({'BOTSID':'line','suart':lin.get({'BOTSID':'LIN'},{'BOTSID':'PIA','C212#1.7143':'SA','C212#1.7140':None})})
        regel.put({'BOTSID':'line','byart':lin.get({'BOTSID':'LIN'},{'BOTSID':'PIA','C212#1.7143':'IN','C212#1.7140':None})})
        regel.put({'BOTSID':'line','desc':lin.get({'BOTSID':'LIN'},{'BOTSID':'IMD','7077':'F','C273.7008#1':None})})

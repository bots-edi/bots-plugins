#mapping-script

    
def main(inn,out):
    out.put({'BOTSID':'ST','ST01':'850','ST02':out.ta_info['reference']})
    out.put({'BOTSID':'ST'},{'BOTSID':'BEG','BEG01':'00','BEG02':'SA','BEG03':inn.get({'BOTSID':'header','PONUMBER':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'BEG','BEG05':inn.get({'BOTSID':'header','PODATE':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'REF','REF01':'ZZ','REF02':inn.get({'BOTSID':'header','POREFERENCE':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'PER','PER01':'IC','PER02':inn.get({'BOTSID':'header','CONTACTNAME':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'PER','PER04':inn.get({'BOTSID':'header','CONTACTPHONE':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'PER','PER06':inn.get({'BOTSID':'header','CONTACTEMAIL':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST','N104':inn.get({'BOTSID':'header','STID':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST','N102':inn.get({'BOTSID':'header','STNAME':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST',},{'BOTSID':'N2','N201':inn.get({'BOTSID':'header','STADDNAME':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST',},{'BOTSID':'N3','N301':inn.get({'BOTSID':'header','STSTREET':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST',},{'BOTSID':'N4','N401':inn.get({'BOTSID':'header','STCITY':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST',},{'BOTSID':'N4','N402':inn.get({'BOTSID':'header','STSTATE':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST',},{'BOTSID':'N4','N403':inn.get({'BOTSID':'header','STZIPCODE':None})})
        
    #LINES***************************************
    for lin in inn.getloop({'BOTSID':'header'},{'BOTSID':'lines'},{'BOTSID':'line'}): 
        lou = out.putloop({'BOTSID':'ST'},{'BOTSID':'PO1'})
        lou.put({'BOTSID':'PO1','PO101':lin.get({'BOTSID':'line','LINENUMBER':None})})
        lou.put({'BOTSID':'PO1','PO102':lin.get({'BOTSID':'line','QTY':None})})
        lou.put({'BOTSID':'PO1','PO103':lin.get({'BOTSID':'line','UNIT':None})})
        lou.put({'BOTSID':'PO1','PO104':lin.get({'BOTSID':'line','UNITPRICE':None})})
        lou.put({'BOTSID':'PO1','PO107':lin.get({'BOTSID':'line','VENDORITEMNUMBER':None})})
        lou.put({'BOTSID':'PO1','PO109':lin.get({'BOTSID':'line','BUYERITEMNUMBER':None})})
        lou.put({'BOTSID':'PO1'},{'BOTSID':'PID','PID01':'F','PID05':lin.get({'BOTSID':'line','DESCRIPTION':None})})

    out.put({'BOTSID':'ST'},{'BOTSID':'SE','SE01':out.getcount()+1,'SE02':out.ta_info['reference']})  #last Line (counts the segments produced in out-message)


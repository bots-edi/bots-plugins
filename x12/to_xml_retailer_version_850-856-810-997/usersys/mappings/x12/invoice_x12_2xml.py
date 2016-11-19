#mapping-script
from x12lib import get_art_num          #import x12 specifc helper function
import bots.transform as transform      #import div bots helper functions

def main(inn,out):
    #pick up some values from ISA envelope
    out.put({'BOTSID':'message','sender':inn.ta_info['frompartner']})
    out.put({'BOTSID':'message','receiver':inn.ta_info['topartner']})
    out.put({'BOTSID':'message','testindicator':inn.ta_info['testindicator']})
    
    out.put({'BOTSID':'message','docdtm':transform.datemask(inn.get({'BOTSID':'ST'},{'BOTSID':'BIG','BIG01':None}),'CCYYMMDD','CCYY-MM-DD')})
    out.put({'BOTSID':'message','docnum':inn.get({'BOTSID':'ST'},{'BOTSID':'BIG','BIG02':None})})
    out.put({'BOTSID':'message','ordernumber':inn.get({'BOTSID':'ST'},{'BOTSID':'BIG','BIG04':None})})
    #~ out.put({'BOTSID':'ST'},{'BOTSID':'BIG','BIG07':'DR'})      #credit or debit
    
    out.put({'BOTSID':'message','deldtm':transform.datemask(inn.get({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'999','DTM02':None}),'CCYYMMDD','CCYY-MM-DD')})
    out.put({'BOTSID':'message','VendorID':inn.get({'BOTSID':'ST'},{'BOTSID':'REF','REF01':'VR','REF02':None})})
    
    out.put({'BOTSID':'message','termsdiscountpercent':inn.get({'BOTSID':'ST'},{'BOTSID':'ITD','ITD03':None})})
    out.put({'BOTSID':'message','termsdiscountdaysdue':inn.get({'BOTSID':'ST'},{'BOTSID':'ITD','ITD05':None})})
    out.put({'BOTSID':'message','termsnetdays':inn.get({'BOTSID':'ST'},{'BOTSID':'ITD','ITD07':None})})
    out.put({'BOTSID':'message','totaltermsdiscount':inn.get({'BOTSID':'ST'},{'BOTSID':'ITD','ITD08':None})})

    #loop over partys
    for party in inn.getloop({'BOTSID':'ST'},{'BOTSID':'N1'}): 
        pou = out.putloop({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party'})
        pou.put({'BOTSID':'party','qual':party.get({'BOTSID':'N1','N101':None})})
        pou.put({'BOTSID':'party','gln':party.get({'BOTSID':'N1','N103':'UL','N104':None})})
        #get DUNS number. 2 qualifiers are used; helper function transform.useoneof checks both
        pou.put({'BOTSID':'party','DUNS':transform.useoneof(party.get({'BOTSID':'N1','N103':'1','N104':None}),party.get({'BOTSID':'N1','N103':'9','N104':None}))})
        pou.put({'BOTSID':'party','externalID':party.get({'BOTSID':'N1','N103':'92','N104':None})})
        pou.put({'BOTSID':'party','internalID':party.get({'BOTSID':'N1','N103':'91','N104':None})})
        pou.put({'BOTSID':'party','name1':party.get({'BOTSID':'N1','N102':None})})
        pou.put({'BOTSID':'party','name2':party.get({'BOTSID':'N1'},{'BOTSID':'N2','N201':None})})
        pou.put({'BOTSID':'party','address1':party.get({'BOTSID':'N1'},{'BOTSID':'N3','N301':None})})
        pou.put({'BOTSID':'party','address2':party.get({'BOTSID':'N1'},{'BOTSID':'N3','N302':None})})
        pou.put({'BOTSID':'party','city':party.get({'BOTSID':'N1'},{'BOTSID':'N4','N401':None})})
        pou.put({'BOTSID':'party','state':party.get({'BOTSID':'N1'},{'BOTSID':'N4','N402':None})})
        pou.put({'BOTSID':'party','pcode':party.get({'BOTSID':'N1'},{'BOTSID':'N4','N403':None})})
        pou.put({'BOTSID':'party','country':party.get({'BOTSID':'N1'},{'BOTSID':'N4','N404':None})})

    #loop over lines***************************************
    for lin in inn.getloop({'BOTSID':'ST'},{'BOTSID':'IT1'}): 
        lou = out.putloop({'BOTSID':'message'},{'BOTSID':'lines'},{'BOTSID':'line'}) 
        lou.put({'BOTSID':'line','linenum':lin.get({'BOTSID':'IT1','IT101':None})})
        lou.put({'BOTSID':'line','invqua':lin.get({'BOTSID':'IT1','IT102':None})})
        lou.put({'BOTSID':'line','ordunit':transform.useoneof(lin.get({'BOTSID':'IT1','IT103':None}),'EA')})
        lou.put({'BOTSID':'line','price':lin.get({'BOTSID':'IT1','IT104':None})})
        
        lou.put({'BOTSID':'line','gtin':get_art_num(lin,'UP')})
        lou.put({'BOTSID':'line','suart':get_art_num(lin,'VN')})
        #get buyers article number; 1 different qualifiers are used; helper function transform.useoneof checks both
        lou.put({'BOTSID':'line','byart':transform.useoneof(get_art_num(lin,'IN'),get_art_num(lin,'BP'))})
        lou.put({'BOTSID':'line','desc':lin.get({'BOTSID':'IT1'},{'BOTSID':'PID','PID01':'F','PID05':None})})

            
    out.put({'BOTSID':'message','totalinvoiceamount':inn.get({'BOTSID':'ST'},{'BOTSID':'TDS','TDS01':None})})  
    
    #~ out.put({'BOTSID':'ST'},{'BOTSID':'ISS','ISS02':'EA','ISS01':out.getcountsum({'BOTSID':'ST'},{'BOTSID':'IT1','IT102':None}) })  #bots counts total Number of Units Shipped 
    #~ out.put({'BOTSID':'ST'},{'BOTSID':'CTT','CTT01':out.getcountoccurrences({'BOTSID':'ST'},{'BOTSID':'IT1'}) }) #bots counts number of line items/IT1 segments 
    #~ out.put({'BOTSID':'ST'},{'BOTSID':'SE','SE01':out.getcount()+1,'SE02':out.ta_info['reference'].zfill(4)})  #SE01: bots counts the segments produced in the X12 message.

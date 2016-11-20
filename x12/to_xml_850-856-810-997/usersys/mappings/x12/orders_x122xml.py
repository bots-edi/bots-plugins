#mapping-script
from x12lib import get_art_num          #import x12 specifc helper function
import bots.transform as transform      #import div bots helper functions

def main(inn,out):
    #pick up some values from ISA envelope
    out.put({'BOTSID':'message','sender':inn.ta_info['frompartner']})
    out.put({'BOTSID':'message','receiver':inn.ta_info['topartner']})
    out.put({'BOTSID':'message','testindicator':inn.ta_info['testindicator']})
    
    #pick up document number. is used in bots to give 'document-view'
    docnum = inn.get({'BOTSID':'ST'},{'BOTSID':'BEG','BEG03':None})
    out.put({'BOTSID':'message','docnum':docnum})
    inn.ta_info['botskey']=docnum
    out.ta_info['botskey']=docnum
    
    out.put({'BOTSID':'message','docsrt':inn.get({'BOTSID':'ST'},{'BOTSID':'BEG','BEG02':None})})
    #convert dates to right internal format
    docdtm = inn.get({'BOTSID':'ST'},{'BOTSID':'BEG','BEG05':None})
    docdtm = transform.datemask(docdtm,'CCYYMMDDHHMM','CCYY-MM-DD')
    out.put({'BOTSID':'message','docdtm':docdtm})
    #same date handling as above, now in a one-liner.
    out.put({'BOTSID':'message','deldtm':transform.datemask(inn.get({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'002','DTM02':None}),'CCYYMMDDHHMM','CCYY-MM-DD')})
    out.put({'BOTSID':'message','earldeldtm':transform.datemask(inn.get({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'064','DTM02':None}),'CCYYMMDDHHMM','CCYY-MM-DD')})
    out.put({'BOTSID':'message','latedeldtm':transform.datemask(inn.get({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'063','DTM02':None}),'CCYYMMDDHHMM','CCYY-MM-DD')})
    
    out.put({'BOTSID':'message','currency':inn.get({'BOTSID':'ST'},{'BOTSID':'CUR','CUR01':'BY','CUR02':None})})
    
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
        
    #mapping above is for full addresses. Often only party-IDs are used (good EDI practices.....
    #mapping could be simpler, eg:
    #~ out.put({'BOTSID':'message','buyer_ID':inn.get({'BOTSID':'ST'},{'BOTSID':'N1','N101':'BY','N4':None})})
    #~ out.put({'BOTSID':'message','delivery_ID':inn.get({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST','N4':None})})
    
    #loop over lines
    for po1 in inn.getloop({'BOTSID':'ST'},{'BOTSID':'PO1'}):
        lou = out.putloop({'BOTSID':'message'},{'BOTSID':'lines'},{'BOTSID':'line'})
        lou.put({'BOTSID':'line','linenum':po1.get({'BOTSID':'PO1','PO101':None})})
        lou.put({'BOTSID':'line','ordqua':po1.get({'BOTSID':'PO1','PO102':None})})
        #get ordering unit; if not there use 'EA' 9each, pice) as default
        lou.put({'BOTSID':'line','ordunit':transform.useoneof(po1.get({'BOTSID':'PO1','PO103':None}),'EA')})
        lou.put({'BOTSID':'line','price':po1.get({'BOTSID':'PO1','PO104':None})})
        lou.put({'BOTSID':'line','gtin':get_art_num(po1,'UP')})
        lou.put({'BOTSID':'line','suart':get_art_num(po1,'VN')})
        #get buyers article number; 1 different qualifiers are used; helper function transform.useoneof checks both
        lou.put({'BOTSID':'line','byart':transform.useoneof(get_art_num(po1,'IN'),get_art_num(po1,'BP'))})
        lou.put({'BOTSID':'line','desc':po1.get({'BOTSID':'PO1'},{'BOTSID':'PID','PID01':'F','PID05':None})})

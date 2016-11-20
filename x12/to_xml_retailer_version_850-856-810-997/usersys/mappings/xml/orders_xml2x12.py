#mapping-script
#~ from x12lib import get_art_num          #import x12 specifc helper function
import bots.transform as transform      #import div bots helper functions

def main(inn,out):
    out.put({'BOTSID':'ST','ST01':'850','ST02':out.ta_info['reference'].zfill(4)})
    #pick up some values from ISA envelope
    #~ out.put({'BOTSID':'message','sender':inn.ta_info['frompartner']})
    #~ out.put({'BOTSID':'message','receiver':inn.ta_info['topartner']})
    #~ out.put({'BOTSID':'message','testindicator':inn.ta_info['testindicator']})
    
    #pick up document number. is used in bots to give 'document-view'
    docnum = inn.get({'BOTSID':'message','docnum':None})
    out.put({'BOTSID':'ST'},{'BOTSID':'BEG','BEG01':'00','BEG03':docnum})
    inn.ta_info['botskey']=docnum
    out.ta_info['botskey']=docnum
    
    out.put({'BOTSID':'ST'},{'BOTSID':'BEG','BEG02':inn.get({'BOTSID':'message','docsrt':None})})
    #convert dates to right internal format
    docdtm = inn.get({'BOTSID':'message','docdtm':None})
    docdtm = transform.datemask(docdtm,'CCYY-MM-DD','CCYYMMDD')
    out.put({'BOTSID':'ST'},{'BOTSID':'BEG','BEG05':docdtm})
    #same date handling as above, now in a one-liner.
    out.put({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'002','DTM02':transform.datemask(inn.get({'BOTSID':'message','deldtm':None}),'CCYY-MM-DD','CCYYMMDD')})
    out.put({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'064','DTM02':transform.datemask(inn.get({'BOTSID':'message','earldeldtm':None}),'CCYY-MM-DD','CCYYMMDD')})
    out.put({'BOTSID':'ST'},{'BOTSID':'DTM','DTM01':'063','DTM02':transform.datemask(inn.get({'BOTSID':'message','latedeldtm':None}),'CCYY-MM-DD','CCYYMMDD')})
    
    out.put({'BOTSID':'ST'},{'BOTSID':'CUR','CUR01':'BY','CUR02':inn.get({'BOTSID':'message','currency':None})})
    
    #loop over partys
    for party in inn.getloop({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party'}): 
        pou = out.putloop({'BOTSID':'ST'},{'BOTSID':'N1'})
        pou.put({'BOTSID':'N1','N101':party.get({'BOTSID':'party','qual':None})})
        #write partyID: if gln write it, else  DUNS etc
        #this uses the fact the out.put retunr True if succeeded. 
        if pou.put({'BOTSID':'N1','N103':'UL','N104':party.get({'BOTSID':'party','gln':None})}):
            pass
        elif pou.put({'BOTSID':'N1','N103':'1','N104':party.get({'BOTSID':'party','DUNS':None})}):
            pass
        elif pou.put({'BOTSID':'N1','N103':'92','N104':party.get({'BOTSID':'party','externalID':None})}):
            pass
        else:
            pou.put({'BOTSID':'N1','N103':'91','N104':party.get({'BOTSID':'party','internalID':None})})
        pou.put({'BOTSID':'N1','N102':party.get({'BOTSID':'party','name1':None})})
        pou.put({'BOTSID':'N1'},{'BOTSID':'N2','N201':party.get({'BOTSID':'party','name2':None})})
        pou.put({'BOTSID':'N1'},{'BOTSID':'N3','N301':party.get({'BOTSID':'party','address1':None})})
        pou.put({'BOTSID':'N1'},{'BOTSID':'N3','N302':party.get({'BOTSID':'party','address2':None})})
        pou.put({'BOTSID':'N1'},{'BOTSID':'N4','N401':party.get({'BOTSID':'party','city':None})})
        pou.put({'BOTSID':'N1'},{'BOTSID':'N4','N402':party.get({'BOTSID':'party','state':None})})
        pou.put({'BOTSID':'N1'},{'BOTSID':'N4','N403':party.get({'BOTSID':'party','pcode':None})})
        pou.put({'BOTSID':'N1'},{'BOTSID':'N4','N404':party.get({'BOTSID':'party','country':None})})
        
    
    #loop over lines
    for po1 in inn.getloop({'BOTSID':'message'},{'BOTSID':'lines'},{'BOTSID':'line'}):
        lou = out.putloop({'BOTSID':'ST'},{'BOTSID':'PO1'})
        lou.put({'BOTSID':'PO1','PO101':po1.get({'BOTSID':'line','linenum':None})})
        lou.put({'BOTSID':'PO1','PO102':po1.get({'BOTSID':'line','ordqua':None})})
        lou.put({'BOTSID':'PO1','PO103':po1.get({'BOTSID':'line','ordunit':None})})
        lou.put({'BOTSID':'PO1','PO104':po1.get({'BOTSID':'line','price':None})})
        offset = 6
        gtin = po1.get({'BOTSID':'line','gtin':None})
        if gtin:
            lou.put({'BOTSID':'PO1','PO1%02d'%offset:'UP','PO1%02d'%(offset+1):gtin})
            offset += 2
        suart = po1.get({'BOTSID':'line','suart':None})
        if suart:
            lou.put({'BOTSID':'PO1','PO1%02d'%offset:'VN','PO1%02d'%(offset+1):suart})
            offset += 2
        byart = po1.get({'BOTSID':'line','byart':None})
        if byart:
            lou.put({'BOTSID':'PO1','PO1%02d'%offset:'IN','PO1%02d'%(offset+1):byart})
        lou.put({'BOTSID':'PO1'},{'BOTSID':'PID','PID01':'F','PID05':po1.get({'BOTSID':'line','desc':None})})

    out.put({'BOTSID':'ST'},{'BOTSID':'CTT','CTT01':out.getcountoccurrences({'BOTSID':'ST'},{'BOTSID':'PO1'}) }) #bots counts line items
    out.put({'BOTSID':'ST'},{'BOTSID':'SE','SE01':out.getcount()+1,'SE02':out.ta_info['reference'].zfill(4)})  #SE01: bots counts the segments produced in the X12 message.

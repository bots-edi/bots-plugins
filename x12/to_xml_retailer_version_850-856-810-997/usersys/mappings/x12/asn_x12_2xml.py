#mapping-script
import bots.transform as transform


def main(inn,out):
    #pick up some values from ISA envelope
    out.put({'BOTSID':'message','sender':inn.ta_info['frompartner']})
    out.put({'BOTSID':'message','receiver':inn.ta_info['topartner']})
    out.put({'BOTSID':'message','testindicator':inn.ta_info['testindicator']})
    
    out.put({'BOTSID':'message','docnum':inn.get({'BOTSID':'ST'},{'BOTSID':'BSN','BSN02':None})})
    out.put({'BOTSID':'message','docdtm':transform.datemask(inn.get({'BOTSID':'ST'},{'BOTSID':'BSN','BSN03':None}),'CCYYMMDD','CCYY-MM-DD')})
    out.put({'BOTSID':'message','doctime':inn.get({'BOTSID':'ST'},{'BOTSID':'BSN','BSN04':None})})

    #***********************************************************************************************
    #shipment level*********************************************************************************
    for shipment in inn.getloop({'BOTSID':'ST'},{'BOTSID':'HL','HL01':'1','HL03':'S'}): 
        #~ hlcounter = 1       #HL segments have sequentail count
        #~ shipment = out.putloop({'BOTSID':'ST'},{'BOTSID':'HL','HL01':hlcounter,'HL03':'S'})
        #~ currentshipment = hlcounter     #remember the current counter, as child-HL segments have to point to this shipment
        #~ hlcounter += 1
        
        out.put({'BOTSID':'message','scac':shipment.get({'BOTSID':'HL'},{'BOTSID':'TD5','TD501':'O','TD502':'2','TD503':None})})
        out.put({'BOTSID':'message','bol':shipment.get({'BOTSID':'HL'},{'BOTSID':'REF','REF01':'BM','REF02':None})})
        out.put({'BOTSID':'message','carrierreferencenumber':shipment.get({'BOTSID':'HL'},{'BOTSID':'REF','REF01':'CN','REF02':None})})
        out.put({'BOTSID':'message','shipdtm':transform.datemask(shipment.get({'BOTSID':'HL'},{'BOTSID':'DTM','DTM01':'011','DTM02':None}),'CCYYMMDD','CCYY-MM-DD')})
        out.put({'BOTSID':'message','deldtm':transform.datemask(shipment.get({'BOTSID':'HL'},{'BOTSID':'DTM','DTM01':'017','DTM02':None}),'CCYYMMDD','CCYY-MM-DD')})

        #loop over partys on shipment level
        for party in shipment.getloop({'BOTSID':'HL'},{'BOTSID':'N1'}): 
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

    #********************************************************************************************
    #order level*********************************************************************************
    for in_order in inn.getloop({'BOTSID':'ST'},{'BOTSID':'HL','HL03':'O'}):
        out_order = out.putloop({'BOTSID':'message'},{'BOTSID':'orders'},{'BOTSID':'order'})
        out_order.put({'BOTSID':'order','ordernumber':in_order.get({'BOTSID':'HL'},{'BOTSID':'PRF','PRF01':None})})
        out_order.put({'BOTSID':'order','orderdtm':transform.datemask(in_order.get({'BOTSID':'HL'},{'BOTSID':'PRF','PRF04':None}),'CCYYMMDD','CCYY-MM-DD')})
        current_order = in_order.get({'BOTSID':'HL','HL01':None})

        #pack/sscc level*********************************************************************************
        for in_sscc in inn.getloop({'BOTSID':'ST'},{'BOTSID':'HL','HL02':current_order,'HL03':'P'}):
            current_sscc = in_sscc.get({'BOTSID':'HL','HL01':None})
            sscc = in_sscc.get({'BOTSID':'HL'},{'BOTSID':'MAN','MAN01':'GM','MAN02': None})
            #line/article level*********************************************************************************
            #loop over all lines that have this sscc
            for lin in inn.getloop({'BOTSID':'ST'},{'BOTSID':'HL','HL02':current_sscc,'HL03':'I'}):
                lou = out_order.putloop({'BOTSID':'order'},{'BOTSID':'lines'},{'BOTSID':'line'})
                lou.put({'BOTSID':'line','linenum':lin.get({'BOTSID':'HL'},{'BOTSID':'LIN','LIN01':None})})
                lou.put({'BOTSID':'line','gtin':lin.get({'BOTSID':'HL'},{'BOTSID':'LIN','LIN02':'UP','LIN03':None})})
                lou.put({'BOTSID':'line','delqua':lin.get({'BOTSID':'HL'},{'BOTSID':'SN1','SN103':'EA','SN102':None})})
                lou.put({'BOTSID':'line','ordqua':lin.get({'BOTSID':'HL'},{'BOTSID':'SN1','SN106':'EA','SN105':None})})
                lou.put({'BOTSID':'line','desc':lin.get({'BOTSID':'HL'},{'BOTSID':'PID','PID01':'F','PID02':'08','PID05':None})})
                lou.put({'BOTSID':'line','sscc':sscc})



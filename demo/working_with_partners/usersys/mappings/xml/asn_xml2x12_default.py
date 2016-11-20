#mapping-script
import bots.transform as transform

def party_mapping(inn,shipment):
    #loop over partys (all on shipment level for simplicity ;-)
    for party in inn.getloop({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party'}): 
        pou = shipment.putloop({'BOTSID':'HL'},{'BOTSID':'N1'})
        pou.put({'BOTSID':'N1','N101':party.get({'BOTSID':'party','qual':None})})
        #write partyID: if gln write it, else  DUNS etc
        #this uses the fact the out.put returns True if succeeded. 
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
        
    #PARTNER LOOKUP   *** sometimes there is no 'BY' qualifier in xml inhouse message. This is fixed here
    if not inn.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'BY'}):
        pou = shipment.putloop({'BOTSID':'HL'},{'BOTSID':'N1'})
        #do a lookup for values in partner 
        pou.put({'BOTSID':'N1','N101':'BY','N102':transform.partnerlookup(inn.ta_info['topartner'],'attr1')})
        pou.put({'BOTSID':'N1','N103':'92','N104':transform.partnerlookup(inn.ta_info['topartner'],'name')})
        


def main(inn,out):
    #sender, receiver is correct via QUERIES in grammar. 
    out.put({'BOTSID':'ST','ST01':'856','ST02':out.ta_info['reference'].zfill(4)})
    
    out.put({'BOTSID':'ST'},{'BOTSID':'BSN','BSN01':'00'})
    out.put({'BOTSID':'ST'},{'BOTSID':'BSN','BSN02':inn.get({'BOTSID':'message','docnum':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'BSN','BSN03':transform.datemask(inn.get({'BOTSID':'message','docdtm':None}),'CCYY-MM-DD HH:mm','CCYYMMDD')})
    out.put({'BOTSID':'ST'},{'BOTSID':'BSN','BSN04':transform.useoneof(inn.get({'BOTSID':'message','doctime':None}),'0000')})
    out.put({'BOTSID':'ST'},{'BOTSID':'BSN','BSN05':'0001'})        #0001: Shipment, Order, Packaging, Item

    #***********************************************************************************************
    #shipment level*********************************************************************************
    hlcounter = 1       #HL segments have sequentail count
    shipment = out.putloop({'BOTSID':'ST'},{'BOTSID':'HL','HL01':hlcounter,'HL03':'S'})
    currentshipment = hlcounter     #remember the current counter, as child-HL segments have to point to this shipment
    hlcounter += 1
    
    shipment.put({'BOTSID':'HL'},{'BOTSID':'TD5','TD501':'O','TD502':'2','TD503':inn.get({'BOTSID':'message','scac':None})})
    shipment.put({'BOTSID':'HL'},{'BOTSID':'REF','REF01':'BM','REF02':inn.get({'BOTSID':'message','bol':None})})
    shipment.put({'BOTSID':'HL'},{'BOTSID':'REF','REF01':'CN','REF02':inn.get({'BOTSID':'message','carrierreferencenumber':None})})
    shipment.put({'BOTSID':'HL'},{'BOTSID':'DTM','DTM01':'011','DTM02':transform.datemask(inn.get({'BOTSID':'message','shipdtm':None}),'CCYY-MM-DD HH:mm','CCYYMMDD')})
    shipment.put({'BOTSID':'HL'},{'BOTSID':'DTM','DTM01':'017','DTM02':transform.datemask(inn.get({'BOTSID':'message','deldtm':None}),'CCYY-MM-DD HH:mm','CCYYMMDD')})

    #mapping for partners is in default 856 mapping
    party_mapping(inn,shipment)

    #********************************************************************************************
    #order level*********************************************************************************
    for order in inn.getloop({'BOTSID':'message'},{'BOTSID':'orders'},{'BOTSID':'order'}):
        ordernode = out.putloop({'BOTSID':'ST'},{'BOTSID':'HL','HL01':hlcounter,'HL02':currentshipment,'HL03':'O'})
        currentorder = hlcounter
        hlcounter += 1
        ordernode.put({'BOTSID':'HL'},{'BOTSID':'PRF','PRF01':order.get({'BOTSID':'order','ordernumber':None})})
        ordernode.put({'BOTSID':'HL'},{'BOTSID':'PRF','PRF04':transform.datemask(order.get({'BOTSID':'order','orderdtm':None}),'CCYY-MM-DD HH:mm','CCYYMMDD')})

        #************************************************************************************************
        #pack/sscc level*********************************************************************************
        #in xml; inhouse file sscc number is included in each line.
        #so first: get a list of all sscc's for this order
        list_of_sscc = [orderline.get({'BOTSID':'line','sscc':None}) for orderline in order.getloop({'BOTSID':'order'},{'BOTSID':'lines'},{'BOTSID':'line'})]
        #list_of_sscc has double sscc's, so remove doubles 
        list_of_sscc = set(list_of_sscc)
        if None in list_of_sscc:
            raise Exception('found lines in ASN without SSCC. SSCC is really needed for this customer.')
        #now write sscc/pack level for each sscc
        for sscc in list_of_sscc:
            ssccnode = out.putloop({'BOTSID':'ST'},{'BOTSID':'HL','HL01':hlcounter,'HL02':currentorder,'HL03':'P'})
            currentsscc = hlcounter
            hlcounter += 1
            ssccnode.put({'BOTSID':'HL'},{'BOTSID':'MAN','MAN01':'GM','MAN02': '00' + sscc})

            #***************************************************************************************************
            #line/article level*********************************************************************************
            #loop over all lines that have this sscc
            for lin in order.getloop({'BOTSID':'order'},{'BOTSID':'lines'},{'BOTSID':'line','sscc':sscc}):
                itemnode = out.putloop({'BOTSID':'ST'},{'BOTSID':'HL','HL01':hlcounter,'HL02':currentsscc,'HL03':'I'})
                hlcounter += 1
                itemnode.put({'BOTSID':'HL'},{'BOTSID':'LIN','LIN01':lin.get({'BOTSID':'line','linenum':None})})
                itemnode.put({'BOTSID':'HL'},{'BOTSID':'LIN','LIN02':'UP','LIN03':lin.get({'BOTSID':'line','gtin':None})})
                itemnode.put({'BOTSID':'HL'},{'BOTSID':'LIN','LIN04':'VN','LIN05':lin.get({'BOTSID':'line','suart':None})})
                itemnode.put({'BOTSID':'HL'},{'BOTSID':'LIN','LIN06':'BP','LIN07':lin.get({'BOTSID':'line','byart':None})})
                itemnode.put({'BOTSID':'HL'},{'BOTSID':'SN1','SN103':'EA','SN102':lin.get({'BOTSID':'line','delqua':None})})
                itemnode.put({'BOTSID':'HL'},{'BOTSID':'SN1','SN106':'EA','SN105':lin.get({'BOTSID':'line','ordqua':None})})
                itemnode.put({'BOTSID':'HL'},{'BOTSID':'PID','PID01':'F','PID02':'08','PID05':lin.get({'BOTSID':'line','desc':None})})


    out.put({'BOTSID':'ST'},{'BOTSID':'CTT','CTT01':out.getcountoccurrences({'BOTSID':'ST'},{'BOTSID':'HL'},{'BOTSID':'LIN'}) }) #bots counts line items
    out.put({'BOTSID':'ST'},{'BOTSID':'SE','SE01':out.getcount()+1,'SE02':out.ta_info['reference'].zfill(4)})  #SE01: bots counts the segments produced in the X12 message.

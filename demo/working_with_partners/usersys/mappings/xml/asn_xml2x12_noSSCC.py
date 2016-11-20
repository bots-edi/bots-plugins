#mapping-script
import bots.transform as transform
import asn_xml2x12_default

def main(inn,out):
    #sender, receiver is correct via QUERIES in grammar. 
    out.put({'BOTSID':'ST','ST01':'856','ST02':out.ta_info['reference'].zfill(4)})
    
    out.put({'BOTSID':'ST'},{'BOTSID':'BSN','BSN01':'00'})
    out.put({'BOTSID':'ST'},{'BOTSID':'BSN','BSN02':inn.get({'BOTSID':'message','docnum':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'BSN','BSN03':transform.datemask(inn.get({'BOTSID':'message','docdtm':None}),'CCYY-MM-DD HH:mm','CCYYMMDD')})
    out.put({'BOTSID':'ST'},{'BOTSID':'BSN','BSN04':transform.useoneof(inn.get({'BOTSID':'message','doctime':None}),'0000')})
    out.put({'BOTSID':'ST'},{'BOTSID':'BSN','BSN05':'0002'})        #0001: Shipment, Order, Item (pfff, just making this up)

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
    asn_xml2x12_default.party_mapping(inn,shipment)

    #********************************************************************************************
    #order level*********************************************************************************
    for order in inn.getloop({'BOTSID':'message'},{'BOTSID':'orders'},{'BOTSID':'order'}):
        ordernode = out.putloop({'BOTSID':'ST'},{'BOTSID':'HL','HL01':hlcounter,'HL02':currentshipment,'HL03':'O'})
        currentorder = hlcounter
        hlcounter += 1
        ordernode.put({'BOTSID':'HL'},{'BOTSID':'PRF','PRF01':order.get({'BOTSID':'order','ordernumber':None})})
        ordernode.put({'BOTSID':'HL'},{'BOTSID':'PRF','PRF04':transform.datemask(order.get({'BOTSID':'order','orderdtm':None}),'CCYY-MM-DD HH:mm','CCYYMMDD')})


        #***************************************************************************************************
        #line/article level*********************************************************************************
        for lin in order.getloop({'BOTSID':'order'},{'BOTSID':'lines'},{'BOTSID':'line'}):
            itemnode = out.putloop({'BOTSID':'ST'},{'BOTSID':'HL','HL01':hlcounter,'HL02':currentorder,'HL03':'I'})
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

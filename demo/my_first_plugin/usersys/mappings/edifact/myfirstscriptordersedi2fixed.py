#mapping-script

#bots calls the 'main' script in this mapping script
#this order translation is based upon dutch edifact interpretations.
def main(inn,out):
    '''
    inn: the object for the incoming message; via get() and getloop() the content of the message can be accessed.
    inn.ta_info contains a python dictionary with information about the incoming message
    out: the object for the outgoing message; via put() and putloop() content is written for this message.
    out.ta_info contains a python dictionary with information about the outgoing message
    '''
    out.put({'BOTSID':'HEA','SENDER':inn.ta_info['frompartner']})       #get sender from ta_info (sender comes from interchange, via QUERIES in edifact grammar)
    out.put({'BOTSID':'HEA','RECEIVER':inn.ta_info['topartner']})
    out.put({'BOTSID':'HEA','MESSAGETYPE':inn.ta_info['messagetype']})
        
    ORDERNUMBER = inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':None})     #get ordernumber from the edifact message
    out.put({'BOTSID':'HEA','ORDERNUMBER':ORDERNUMBER})                      #and put it in the outgoing fixed message
    out.ta_info['botskey'] = ORDERNUMBER    #to have the ordernumber in the document screen
    
    out.put({'BOTSID':'HEA','ORDERTYPE':inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':None})})   #combine get and put in one line!!
    out.put({'BOTSID':'HEA','ORDERDATE':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2380':None})})     #get statement ONLY looks for DTM with qualifier 137
    out.put({'BOTSID':'HEA','DELIVERY_DATE':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'2','C507.2380':None})})
    out.put({'BOTSID':'HEA','BUYER_ID':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY','C082.3039':None})})
    out.put({'BOTSID':'HEA','SUPPLIER_ID':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3039':None})})
    out.put({'BOTSID':'HEA','DELIVERYPLACE_ID':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'DP','C082.3039':None})})

    #start looping for the lines (LIN-segments)
    for lin in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'LIN'}):          #for each LIN (nested under UNH):
        lou = out.putloop({'BOTSID':'HEA'},{'BOTSID':'LIN'})                #write a fixed LIN-record
        #note that in this loop get() is used on the lin-object, and put() is used for the lou-object
        lou.put({'BOTSID':'LIN','LINENUMBER':lin.get({'BOTSID':'LIN','1082':None})})
        lou.put({'BOTSID':'LIN','ARTICLE_GTIN':lin.get({'BOTSID':'LIN','C212.7140':None})})
        lou.put({'BOTSID':'LIN','DESCRIPTION':lin.get({'BOTSID':'LIN'},{'BOTSID':'IMD','C273.7008#1':None})})
        lou.put({'BOTSID':'LIN','QUANTITY':lin.get({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'21','C186.6060':None})})

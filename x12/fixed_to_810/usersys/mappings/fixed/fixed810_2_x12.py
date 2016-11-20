#mapping-script
import time
import decimal

def main(inn,out):
    #~ print 'translation script invoice810.py'
    out.put({'BOTSID':'ST','ST02':out.ta_info['reference'],'ST01':'810'})
    out.put({'BOTSID':'ST'},{'BOTSID':'BIG','BIG01':time.strftime('%Y%m%d'),'BIG03':time.strftime('%Y%m%d')})

    out.put({'BOTSID':'ST'},{'BOTSID':'BIG','BIG02':inn.get({'BOTSID':'HEA','INVOICE':None})})

    ORDERNUMMER = inn.get({'BOTSID':'HEA','ORDERNUMMER':None})
    out.put({'BOTSID':'ST'},{'BOTSID':'BIG','BIG04':ORDERNUMMER})
    if not ORDERNUMMER:
        ORDERNUMMER = 'NO PO'
    out.put({'BOTSID':'ST'},{'BOTSID':'REF','REF01':'PO','REF02':ORDERNUMMER})


    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'RI','N102':'ALGORA PUBLISHING'})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'RI'},{'BOTSID':'N3','N301':'222 RIVERSIDE DRIVE'})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'RI'},{'BOTSID':'N3','N302':'STE. 16'})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'RI'},{'BOTSID':'N4','N401':'NEW YORK'})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'RI'},{'BOTSID':'N4','N402':'NY'})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'RI'},{'BOTSID':'N4','N403':'10025'})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'RI'},{'BOTSID':'N4','N404':'USA'})

    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST','N102':inn.get({'BOTSID':'HEA','SHIPTONAME':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST'},{'BOTSID':'N3','N301':inn.get({'BOTSID':'HEA','SHIPTOADDRESS1':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST'},{'BOTSID':'N3','N302':inn.get({'BOTSID':'HEA','SHIPTOADDRESS2':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST'},{'BOTSID':'N4','N401':inn.get({'BOTSID':'HEA','CITY':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST'},{'BOTSID':'N4','N402':inn.get({'BOTSID':'HEA','STATE':None})})
    out.put({'BOTSID':'ST'},{'BOTSID':'N1','N101':'ST'},{'BOTSID':'N4','N403':inn.get({'BOTSID':'HEA','ZIP':None})})


    totalline = decimal.Decimal('0') #~initialise totalline
    qtytotal = decimal.Decimal('0') #~initialise qtytotal
    discount = decimal.Decimal('0.8') #~set discount
    for regel in inn.getloop({'BOTSID':'HEA'},{'BOTSID':'LIN'}):
        lou = out.putloop({'BOTSID':'ST'},{'BOTSID':'IT1'})
        lou.put({'BOTSID':'IT1','IT102':regel.get({'BOTSID':'LIN','QUANTITY':None})})
        #calculate total number of items in invoice (qtytotal), total line amount
        qty = decimal.Decimal(regel.get({'BOTSID':'LIN','QUANTITY':None}))
        qtytotal += qty
        price = decimal.Decimal(regel.get({'BOTSID':'LIN','LISTPRICE':None}))
        netprice = price*discount 
        totalline += netprice*qty       #~assuming there is always a price and quantity
        lou.put({'BOTSID':'IT1','IT103':'EA'})
        lou.put({'BOTSID':'IT1','IT104':netprice })
        lou.put({'BOTSID':'IT1','IT105':'NT'})
        lou.put({'BOTSID':'IT1','IT106':'EN'})
        lou.put({'BOTSID':'IT1','IT107':regel.get({'BOTSID':'LIN','ISBN':None})})
        lou.put({'BOTSID':'IT1','IT109':regel.get({'BOTSID':'LIN','TITLE':None})})
        lou.put({'BOTSID':'IT1'},{'BOTSID':'CTP','CTP07':'.7','CTP06':'DIS','CTP03':'LPR','CTP02':inn.get({'BOTSID':'LIN','LISTPRICE':None})})
    
    print totalline
    out.put({'BOTSID':'ST'},{'BOTSID':'TDS','TDS01':totalline }) 

    numberoflines = out.getcountoccurrences({'BOTSID':'ST'},{'BOTSID':'IT1'})
    out.put({'BOTSID':'ST'},{'BOTSID':'CTT','CTT01':numberoflines }) 

    out.put({'BOTSID':'ST'},{'BOTSID':'CTT','CTT02':qtytotal })

    out.put({'BOTSID':'ST'},{'BOTSID':'SE','SE01':out.getcount()+1,'SE02':out.ta_info['reference']})  #last line (counts the segments produced in out-message)


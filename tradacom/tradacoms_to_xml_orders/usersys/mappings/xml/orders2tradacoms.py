#mapping-script
import time
import bots.transform as transform

def datewithoutcc(date):
    ''' delete CC before data. 
        CCYYMMDD(HHMM(SS)) ->YYMMDD(HHMM(SS))
    '''
    if not date:
        return None
    if len(date) in [10,6]:
        return date
    else:
        return date[2:]


def main(inn,out):
    out.put({'BOTSID':'STX'})   #for tradacoms: dummy root node is created (is not used!! for eg envelope)
    
    messagecounter = 0
    ordercounter = 0
    isfirstmessage = True
    for mes in inn.getloop({'BOTSID':'envelope'},{'BOTSID':'message'}):
        if isfirstmessage:
        #~ #do the ORDHDR
            isfirstmessage = False
            messagecounter += 1
            ord = out.putloop({'BOTSID':'STX'},{'BOTSID':'MHD'})
            ord.put({'BOTSID':'MHD','TYPE.01':'ORDHDR','TYPE.02':'9','MSRF':messagecounter})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'TYP','TCDE':mes.get({'BOTSID':'message','docsrt':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'TYP','TTYP':mes.get({'BOTSID':'message','mesfunc':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'SDT','SIDN.01':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'SU','gln':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'SDT','SIDN.02':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'SU','bilnum':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'SDT','SNAM':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'SU','name':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'SDT','SADD.01':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'SU','addressline1':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'SDT','SADD.02':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'SU','addressline2':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'SDT','SADD.03':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'SU','addressline3':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'SDT','SADD.04':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'SU','addressline4':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'SDT','SADD.05':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'SU','pcode':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'SDT','VATN.02':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'SU','vatnum':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'CDT','CIDN.01':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'BY','gln':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'CDT','CIDN.02':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'BY','bilnum':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'CDT','CNAM':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'BY','name':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'CDT','CADD.01':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'BY','addressline1':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'CDT','CADD.02':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'BY','addressline2':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'CDT','CADD.03':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'BY','addressline3':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'CDT','CADD.04':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'BY','addressline4':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'CDT','CADD.05':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'BY','pcode':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'CDT','VATR.02':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'BY','vatnum':None})})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'FIL','FLVN':'1','FLDT':transform.strftime('%y%m%d'),'FLGN':transform.unique('ORDHDR'+inn.ta_info['topartner'])})
            ord.put({'BOTSID':'MHD'},{'BOTSID':'MTR','NOSG':ord.getcount()+1})
    
        #~ #do the ORDERS
        messagecounter += 1
        ordercounter += 1
        ord = out.putloop({'BOTSID':'STX'},{'BOTSID':'MHD'})
        ord.put({'BOTSID':'MHD','TYPE.01':'ORDERS','TYPE.02':'9','MSRF':messagecounter})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'CLO','CLOC.01':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'DP','gln':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'CLO','CLOC.02':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'DP','bilnum':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'CLO','CLOC.03':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'DP','intcustomernum':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'CLO','CNAM':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'DP','name':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'CLO','CADD.01':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'DP','addressline1':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'CLO','CADD.02':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'DP','addressline2':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'CLO','CADD.03':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'DP','addressline3':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'CLO','CADD.04':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'DP','addressline4':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'CLO','CADD.05':mes.get({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party','qual':'DP','pcode':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'ORD','ORNO.01':mes.get({'BOTSID':'message','docnum':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'ORD','ORNO.02':mes.get({'BOTSID':'message','docnumvv':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'ORD','ORNO.03':datewithoutcc(mes.get({'BOTSID':'message','docdtm':None}))})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'ORD','ORNO.04':datewithoutcc(mes.get({'BOTSID':'message','docdtmvv':None}))})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'ORD','CLAS':mes.get({'BOTSID':'message','classification':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'ORD','ORCD':mes.get({'BOTSID':'message','orcd':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'ORD','SCRF.01':mes.get({'BOTSID':'message','projectnum':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'ORD','SCRF.02':mes.get({'BOTSID':'message','contractnum':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'DIN','EDAT':datewithoutcc(mes.get({'BOTSID':'message','earldeldtm':None}))})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'DIN','LDAT':datewithoutcc(mes.get({'BOTSID':'message','latedeldtm':None}))})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'DIN','RATM.01':mes.get({'BOTSID':'message','deltimefrom':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'DIN','RATM.02':mes.get({'BOTSID':'message','deltimetill':None})})
        
        count = 0
        for deltxt in mes.getloop({'BOTSID':'message'},{'BOTSID':'txts'},{'BOTSID':'txt','qual':'DEL'}):
            count += 1
            ord.put({'BOTSID':'MHD'},{'BOTSID':'DIN','DINS.0'+str(count):deltxt.get({'BOTSID':'txt','val':None})})
        linecounter = 0
        for lin in mes.getloop({'BOTSID':'message'},{'BOTSID':'lines'},{'BOTSID':'line'}):
            linecounter += 1
            xlin = ord.putloop({'BOTSID':'MHD'},{'BOTSID':'OLD'})
            xlin.put({'BOTSID':'OLD','SEQA':linecounter})
            xlin.put({'BOTSID':'OLD','SPRO.01':lin.get({'BOTSID':'line','gtin':None})})
            xlin.put({'BOTSID':'OLD','SPRO.02':lin.get({'BOTSID':'line','suart':None})})
            xlin.put({'BOTSID':'OLD','CPRO.02':lin.get({'BOTSID':'line','byart':None})})
            xlin.put({'BOTSID':'OLD','SACU':lin.get({'BOTSID':'line','gtincu':None})})
            xlin.put({'BOTSID':'OLD','UNOR.01':lin.get({'BOTSID':'line','numbergtincu':None})})
            xlin.put({'BOTSID':'OLD','UNOR.02':lin.get({'BOTSID':'line','ordqua':None})})
            xlin.put({'BOTSID':'OLD','UNOR.03':lin.get({'BOTSID':'line','ordunit':None})})
            xlin.put({'BOTSID':'OLD','OQTY.03':lin.get({'BOTSID':'line','ordunit':None})})
            xlin.put({'BOTSID':'OLD','OQTY.01':lin.get({'BOTSID':'line','num':None})})
            xlin.put({'BOTSID':'OLD','TDES.01':lin.get({'BOTSID':'line','desc':None})})
            xlin.put({'BOTSID':'OLD','SPIND':lin.get({'BOTSID':'line','pdnum':None})})
            xlin.put({'BOTSID':'OLD','SCRF.02':lin.get({'BOTSID':'line','contractnum':None})})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'OTR','LORD':linecounter})
        ord.put({'BOTSID':'MHD'},{'BOTSID':'MTR','NOSG':ord.getcount()+1})
        
    #~ #do the ORDTLR
    messagecounter += 1
    ord = out.putloop({'BOTSID':'STX'},{'BOTSID':'MHD'})
    ord.put({'BOTSID':'MHD','TYPE.01':'ORDTLR','TYPE.02':'9','MSRF':messagecounter})
    ord.put({'BOTSID':'MHD'},{'BOTSID':'OFT','FTOR':ordercounter})
    ord.put({'BOTSID':'MHD'},{'BOTSID':'MTR','NOSG':ord.getcount()+1})
        

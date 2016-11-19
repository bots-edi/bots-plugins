#mapping-script
import bots.transform as transform

def datewithcc(date):
    ''' append CC before data. 
        YYMMDD(HHMM(SS)) ->CCYYMMDD(HHMM(SS))
    '''
    if not date:
        return None
    if len(date) in [14,8]:
        return date
    else:
        return '20' + date


def main(inn,out):
    sender = inn.ta_info['frompartner']
    sendername = inn.get({'BOTSID':'STX','FROM.02':None})
    receiver = inn.ta_info['topartner']
    receivername = inn.get({'BOTSID':'STX','UNTO.02':None})
    envid = inn.get({'BOTSID':'STX','SNRF':None})
    envdtm = datewithcc(inn.get({'BOTSID':'STX','TRDT.01':None}))
    envtime = inn.get({'BOTSID':'STX','TRDT.02':None})
    if envtime:
        envdtm += envtime
    applref = inn.get({'BOTSID':'STX','APRF':None})
    orgeditype = inn.ta_info['editype']
    orgmessagetype = inn.ta_info['messagetype']
    type = 'orders'
    version = '1'
    
    #do the ORDHDR
    for ord in inn.getloop({'BOTSID':'STX'},{'BOTSID':'MHD','TYPE.01':'ORDHDR'}):
        docsrt = ord.get({'BOTSID':'MHD'},{'BOTSID':'TYP','TCDE':None})
        mesfunc = ord.get({'BOTSID':'MHD'},{'BOTSID':'TYP','TTYP':None})
        mesnum = ord.get({'BOTSID':'MHD'},{'BOTSID':'FIL','FLGN':None})
        #get supplier
        SUgln = ord.get({'BOTSID':'MHD'},{'BOTSID':'SDT','SIDN.01':None})
        SUbilnum = ord.get({'BOTSID':'MHD'},{'BOTSID':'SDT','SIDN.02':None})
        SUname = ord.get({'BOTSID':'MHD'},{'BOTSID':'SDT','SNAM':None})
        SUaddressline1 = ord.get({'BOTSID':'MHD'},{'BOTSID':'SDT','SADD.01':None})
        SUaddressline2 = ord.get({'BOTSID':'MHD'},{'BOTSID':'SDT','SADD.02':None})
        SUaddressline3 = ord.get({'BOTSID':'MHD'},{'BOTSID':'SDT','SADD.03':None})
        SUaddressline4 = ord.get({'BOTSID':'MHD'},{'BOTSID':'SDT','SADD.04':None})
        SUpcode = ord.get({'BOTSID':'MHD'},{'BOTSID':'SDT','SADD.05':None})
        SUvatnum = transform.useoneof(ord.get({'BOTSID':'MHD'},{'BOTSID':'SDT','VATN.02':None}),ord.get({'BOTSID':'MHD'},{'BOTSID':'SDT','VATN.01':None}))
        #get buyer
        BYgln = ord.get({'BOTSID':'MHD'},{'BOTSID':'CDT','CIDN.01':None})
        BYbilnum = ord.get({'BOTSID':'MHD'},{'BOTSID':'CDT','CIDN.02':None})
        BYname = ord.get({'BOTSID':'MHD'},{'BOTSID':'CDT','CNAM':None})
        BYaddressline1 = ord.get({'BOTSID':'MHD'},{'BOTSID':'CDT','CADD.01':None})
        BYaddressline2 = ord.get({'BOTSID':'MHD'},{'BOTSID':'CDT','CADD.02':None})
        BYaddressline3 = ord.get({'BOTSID':'MHD'},{'BOTSID':'CDT','CADD.03':None})
        BYaddressline4 = ord.get({'BOTSID':'MHD'},{'BOTSID':'CDT','CADD.04':None})
        BYpcode = ord.get({'BOTSID':'MHD'},{'BOTSID':'CDT','CADD.05':None})
        BYvatnum = transform.useoneof(ord.get({'BOTSID':'MHD'},{'BOTSID':'CDT','VATR.02':None}),ord.get({'BOTSID':'MHD'},{'BOTSID':'CDT','VATR.01':None}))
        #DNA/text
        headerbilas = []
        headertexts = []
        for DNA in ord.getloop({'BOTSID':'MHD'},{'BOTSID':'DNA'}):
            code = DNA.get({'BOTSID':'DNA','DNAC.01':None})
            val = DNA.get({'BOTSID':'DNA','DNAC.02':None})
            if code:
                headerbilas.append((code,val))
            for dataelement in [('RTEX.01','RTEX.02'),('RTEX.03','RTEX.04'),('RTEX.05','RTEX.06'),('RTEX.07','RTEX.08')]:
                code = DNA.get({'BOTSID':'DNA',dataelement[0]:None})
                val = DNA.get({'BOTSID':'DNA',dataelement[1]:None})
                if code:
                    headerbilas.append((code,val))
            for dataelement in ['GNAR.01','GNAR.02','GNAR.03','GNAR.04']:
                val = DNA.get({'BOTSID':'DNA',dataelement:None})
                if val:
                    headertexts.append(('ORDHDR',val))
        
    out.put({'BOTSID':'envelope'})  #needed to initialise the envelope
    #do the ORDERS
    for ord in inn.getloop({'BOTSID':'STX'},{'BOTSID':'MHD','TYPE.01':'ORDERS'}):
        xord = out.putloop({'BOTSID':'envelope'},{'BOTSID':'message'})
        #place envelope info in order
        xord.put({'BOTSID':'message','sender':sender})
        xord.put({'BOTSID':'message','sendername':sendername})
        xord.put({'BOTSID':'message','receiver':receiver})
        xord.put({'BOTSID':'message','receivername':receivername})
        xord.put({'BOTSID':'message','envid':envid})
        xord.put({'BOTSID':'message','envdtm':envdtm})
        xord.put({'BOTSID':'message','applref':applref})
        xord.put({'BOTSID':'message','orgeditype':orgeditype})
        xord.put({'BOTSID':'message','orgmessagetype':orgmessagetype})
        xord.put({'BOTSID':'message','type':type})
        xord.put({'BOTSID':'message','version':version})
        xord.put({'BOTSID':'message','docsrt':docsrt})
        xord.put({'BOTSID':'message','mesfunc':mesfunc})
        xord.put({'BOTSID':'message','mesnum':mesnum})
            
        #place order header info in order
        xord.put({'BOTSID':'message','mesnum':mesnum})
        xord.put({'BOTSID':'message','docsrt':docsrt})
        xord.put({'BOTSID':'message','mesfunc':mesfunc})
        #write supplier
        party = xord.putloop({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party'})
        party.put({'BOTSID':'party','qual':'SU'})
        party.put({'BOTSID':'party','gln':SUgln})
        party.put({'BOTSID':'party','bilnum':SUbilnum})
        party.put({'BOTSID':'party','name':SUname})
        party.put({'BOTSID':'party','addressline1':SUaddressline1})
        party.put({'BOTSID':'party','addressline2':SUaddressline1})
        party.put({'BOTSID':'party','addressline3':SUaddressline1})
        party.put({'BOTSID':'party','addressline4':SUaddressline1})
        party.put({'BOTSID':'party','pcode':SUpcode})
        party.put({'BOTSID':'party','vatnum':SUvatnum})
        #write buyer
        party = xord.putloop({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party'})
        party.put({'BOTSID':'party','qual':'BY'})
        party.put({'BOTSID':'party','gln':BYgln})
        party.put({'BOTSID':'party','bilnum':BYbilnum})
        party.put({'BOTSID':'party','name':BYname})
        party.put({'BOTSID':'party','addressline1':BYaddressline1})
        party.put({'BOTSID':'party','addressline2':BYaddressline1})
        party.put({'BOTSID':'party','addressline3':BYaddressline1})
        party.put({'BOTSID':'party','addressline4':BYaddressline1})
        party.put({'BOTSID':'party','pcode':BYpcode})
        party.put({'BOTSID':'party','vatnum':BYvatnum})
        #DNA/text
        for bila in headerbilas:
            regel = xord.putloop({'BOTSID':'message'},{'BOTSID':'bilas'},{'BOTSID':'bila'})
            regel.put({'BOTSID':'bila','qual':bila[0]})
            regel.put({'BOTSID':'bila','val':bila[1]})
        for txt in headertexts:
            regel = xord.putloop({'BOTSID':'message'},{'BOTSID':'txts'},{'BOTSID':'txt'})
            regel.put({'BOTSID':'txt','qual':txt[0]})
            regel.put({'BOTSID':'txt','val':txt[1]})
        #end order header info
        #write delivery place
        party = xord.putloop({'BOTSID':'message'},{'BOTSID':'partys'},{'BOTSID':'party'})
        party.put({'BOTSID':'party','qual':'DP'})
        party.put({'BOTSID':'party','gln':ord.get({'BOTSID':'MHD'},{'BOTSID':'CLO','CLOC.01':None})})
        party.put({'BOTSID':'party','bilnum':ord.get({'BOTSID':'MHD'},{'BOTSID':'CLO','CLOC.02':None})})
        party.put({'BOTSID':'party','intcustomernum':ord.get({'BOTSID':'MHD'},{'BOTSID':'CLO','CLOC.03':None})})
        party.put({'BOTSID':'party','name':ord.get({'BOTSID':'MHD'},{'BOTSID':'CLO','CNAM':None})})
        party.put({'BOTSID':'party','addressline1':ord.get({'BOTSID':'MHD'},{'BOTSID':'CLO','CADD.01':None})})
        party.put({'BOTSID':'party','addressline2':ord.get({'BOTSID':'MHD'},{'BOTSID':'CLO','CADD.02':None})})
        party.put({'BOTSID':'party','addressline3':ord.get({'BOTSID':'MHD'},{'BOTSID':'CLO','CADD.03':None})})
        party.put({'BOTSID':'party','addressline4':ord.get({'BOTSID':'MHD'},{'BOTSID':'CLO','CADD.04':None})})
        party.put({'BOTSID':'party','pcode':ord.get({'BOTSID':'MHD'},{'BOTSID':'CLO','CADD.05':None})})

        xord.put({'BOTSID':'message','docnum':ord.get({'BOTSID':'MHD'},{'BOTSID':'ORD','ORNO.01':None})})
        xord.put({'BOTSID':'message','docnumvv':ord.get({'BOTSID':'MHD'},{'BOTSID':'ORD','ORNO.02':None})})
        xord.put({'BOTSID':'message','docdtm':datewithcc(ord.get({'BOTSID':'MHD'},{'BOTSID':'ORD','ORNO.03':None}))})
        xord.put({'BOTSID':'message','docdtmvv':datewithcc(ord.get({'BOTSID':'MHD'},{'BOTSID':'ORD','ORNO.04':None}))})
        xord.put({'BOTSID':'message','classification':ord.get({'BOTSID':'MHD'},{'BOTSID':'ORD','CLAS':None})})
        xord.put({'BOTSID':'message','orcd':ord.get({'BOTSID':'MHD'},{'BOTSID':'ORD','ORCD':None})})
        xord.put({'BOTSID':'message','projectnum':ord.get({'BOTSID':'MHD'},{'BOTSID':'ORD','SCRF.01':None})})
        xord.put({'BOTSID':'message','contractnum':ord.get({'BOTSID':'MHD'},{'BOTSID':'ORD','SCRF.02':None})})
        xord.put({'BOTSID':'message','earldeldtm':datewithcc(ord.get({'BOTSID':'MHD'},{'BOTSID':'DIN','EDAT':None}))})
        xord.put({'BOTSID':'message','latedeldtm':datewithcc(ord.get({'BOTSID':'MHD'},{'BOTSID':'DIN','LDAT':None}))})
        xord.put({'BOTSID':'message','deltimefrom':ord.get({'BOTSID':'MHD'},{'BOTSID':'DIN','RATM.01':None})})
        xord.put({'BOTSID':'message','deltimetill':ord.get({'BOTSID':'MHD'},{'BOTSID':'DIN','RATM.02':None})})
        #DIN/text
        val = ord.get({'BOTSID':'MHD'},{'BOTSID':'DIN','DINN':None})
        if val:
            regel = xord.putloop({'BOTSID':'message'},{'BOTSID':'bilas'},{'BOTSID':'bila'})
            regel.put({'BOTSID':'bila','qual':'DELSTD'})
            regel.put({'BOTSID':'bila','val':val})
        for dataelement in ['DINS.01','DINS.02','DINS.03','DINS.04']:
            val = ord.get({'BOTSID':'MHD'},{'BOTSID':'DIN',dataelement:None})
            if val:
                regel = xord.putloop({'BOTSID':'message'},{'BOTSID':'txts'},{'BOTSID':'txt'})
                regel.put({'BOTSID':'txt','qual':'DEL'})
                regel.put({'BOTSID':'txt','val':val})
                        
        #DNA/text
        for DNA in ord.getloop({'BOTSID':'MHD'},{'BOTSID':'DNA'}):
            code = DNA.get({'BOTSID':'DNA','DNAC.01':None})
            val = DNA.get({'BOTSID':'DNA','DNAC.02':None})
            if code:
                regel = xord.putloop({'BOTSID':'message'},{'BOTSID':'bilas'},{'BOTSID':'bila'})
                regel.put({'BOTSID':'bila','qual':code})
                regel.put({'BOTSID':'bila','val':val})
            for dataelement in [('RTEX.01','RTEX.02'),('RTEX.03','RTEX.04'),('RTEX.05','RTEX.06'),('RTEX.07','RTEX.08')]:
                code = DNA.get({'BOTSID':'DNA',dataelement[0]:None})
                val = DNA.get({'BOTSID':'DNA',dataelement[1]:None})
                if code:
                    regel = xord.putloop({'BOTSID':'message'},{'BOTSID':'bilas'},{'BOTSID':'bila'})
                    regel.put({'BOTSID':'bila','qual':code})
                    regel.put({'BOTSID':'bila','val':val})
            for dataelement in ['GNAR.01','GNAR.02','GNAR.03','GNAR.04']:
                val = DNA.get({'BOTSID':'DNA',dataelement:None})
                if val:
                    regel = xord.putloop({'BOTSID':'message'},{'BOTSID':'txts'},{'BOTSID':'txt'})
                    regel.put({'BOTSID':'txt','qual':'ORDERS'})
                    regel.put({'BOTSID':'txt','val':val})
                    
        for lin in ord.getloop({'BOTSID':'MHD'},{'BOTSID':'OLD'}):
            xlin = xord.putloop({'BOTSID':'message'},{'BOTSID':'lines'},{'BOTSID':'line'})
            xlin.put({'BOTSID':'line','gtin':transform.useoneof(
                                                                lin.get({'BOTSID':'OLD','SPRO.01':None}),
                                                                lin.get({'BOTSID':'OLD','CPRO.01':None}),
                                                                lin.get({'BOTSID':'OLD','SPRO.03':None}),
                                                                )})
            xlin.put({'BOTSID':'line','gtincu':lin.get({'BOTSID':'OLD','SACU':None})})
            xlin.put({'BOTSID':'line','suart':lin.get({'BOTSID':'OLD','SPRO.02':None})})
            xlin.put({'BOTSID':'line','byart':lin.get({'BOTSID':'OLD','CPRO.02':None})})
            xlin.put({'BOTSID':'line','num':transform.useoneof(lin.get({'BOTSID':'OLD','OQTY.01':None}),lin.get({'BOTSID':'OLD','OQTY.02':None}))})
            xlin.put({'BOTSID':'line','ordqua':lin.get({'BOTSID':'OLD','UNOR.02':None})})
            xlin.put({'BOTSID':'line','ordunit':transform.useoneof(lin.get({'BOTSID':'OLD','OQTY.03':None}),lin.get({'BOTSID':'OLD','UNOR.03':None}))})
            xlin.put({'BOTSID':'line','numbergtincu':lin.get({'BOTSID':'OLD','UNOR.01':None})})
            xlin.put({'BOTSID':'line','desc':lin.get({'BOTSID':'OLD','TDES.01':None})})
            xlin.put({'BOTSID':'line','pdnum':lin.get({'BOTSID':'OLD','PIND':None})})
            xlin.put({'BOTSID':'line','projectnum':lin.get({'BOTSID':'OLD','SCRF.01':None})})
            xlin.put({'BOTSID':'line','contractnum':lin.get({'BOTSID':'OLD','SCRF.02':None})})
            price = lin.get({'BOTSID':'OLD','OUCT.01':None})
            if price:
                xpri = xlin.putloop({'BOTSID':'line'},{'BOTSID':'pris'},{'BOTSID':'pri'})
                xpri.put({'BOTSID':'pri','qual':'XXX'})
                xpri.put({'BOTSID':'pri','price':price})
                xpri.put({'BOTSID':'pri','unit':lin.get({'BOTSID':'OLD','OUCT.02':None})})
            #DNB/text line level
            for DNA in lin.getloop({'BOTSID':'OLD'},{'BOTSID':'DNB'}):
                code = DNA.get({'BOTSID':'DNB','DNAC.01':None})
                val = DNA.get({'BOTSID':'DNB','DNAC.02':None})
                if code:
                    regel = xlin.putloop({'BOTSID':'line'},{'BOTSID':'bilas'},{'BOTSID':'bila'})
                    regel.put({'BOTSID':'bila','qual':code})
                    regel.put({'BOTSID':'bila','val':val})
                for dataelement in [('RTEX.01','RTEX.02'),('RTEX.03','RTEX.04'),('RTEX.05','RTEX.06'),('RTEX.07','RTEX.08')]:
                    code = DNA.get({'BOTSID':'DNB',dataelement[0]:None})
                    val = DNA.get({'BOTSID':'DNB',dataelement[1]:None})
                    if code:
                        regel = xlin.putloop({'BOTSID':'line'},{'BOTSID':'bilas'},{'BOTSID':'bila'})
                        regel.put({'BOTSID':'bila','qual':code})
                        regel.put({'BOTSID':'bila','val':val})
                for dataelement in ['GNAR.01','GNAR.02','GNAR.03','GNAR.04']:
                    val = DNA.get({'BOTSID':'DNB',dataelement:None})
                    if val:
                        regel = xlin.putloop({'BOTSID':'line'},{'BOTSID':'txts'},{'BOTSID':'txt'})
                        regel.put({'BOTSID':'txt','qual':'ORDLINE'})
                        regel.put({'BOTSID':'txt','val':val})
        
    #do not use ORDTRL

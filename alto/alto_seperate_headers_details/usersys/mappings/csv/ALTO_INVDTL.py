# Mapping of Alto invoice detail to IDoc for bridge
# Mike Griffin 25/02/2010

import bots.transform as transform

def main(inn,out):

    # Constants to provide data not in input file
    customer   = '098765432' # E1EDKA1 AG & RE
    vendor     = '12345678'  # E1EDKA1 LF
    currency   = 'NZD'
    GSTpercent = '12.5'
    UOM        = 'PCE'

    # Set values for bridge idoc control record
    out.ta_info['MANDT'] = '200'
    out.ta_info['DOCNUM'] = ''
    out.put({'BOTSID':'EDI_DC40','IDOCTYP':'INVOIC02'  })
    out.put({'BOTSID':'EDI_DC40','MESTYP' :'INVOIC'    })
    out.put({'BOTSID':'EDI_DC40','DIRECT' :'2'         })
    out.put({'BOTSID':'EDI_DC40','SNDPRT' :'LS'        })
    out.put({'BOTSID':'EDI_DC40','SNDPRN' :'BOTS'      })
    out.put({'BOTSID':'EDI_DC40','RCVPOR' :'SAPPRH'    })
    out.put({'BOTSID':'EDI_DC40','RCVPRT' :'LS'        })
    out.put({'BOTSID':'EDI_DC40','RCVPRN' :'PRHCLNT200'})
    out.put({'BOTSID':'EDI_DC40','SNDPOR' :'APPZEDIPRP'})

    out.ta_info['topartner'] = out.get({'BOTSID':'EDI_DC40','RCVPRN':None})

    INVNUM = ''
    COUNT = 0
    for dtl in inn.getloop({'BOTSID':'DTL'}):

        # header processing first time through loop
        if (INVNUM == ''):
            INVNUM = dtl.get({'BOTSID':'DTL','INVNUM':None})
            BCHDATE   = get_hdr_value('BCHDATE',  INVNUM)
            INVDATE   = get_hdr_value('INVDATE',  INVNUM)
            ORDNUM    = get_hdr_value('ORDNUM',   INVNUM)
            TOTEXCGST = get_hdr_value('TOTEXCGST',INVNUM)
            TOTGSTAMT = get_hdr_value('TOTGSTAMT',INVNUM)
            TOTINCGST = get_hdr_value('TOTINCGST',INVNUM)

            # Header info
            out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E1EDK01','CURCY':currency,'BSART':'INV0','FKTYP':'L'})

            out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E1EDK01'},{'BOTSID':'E1EDKA1','PARVW':'AG','LIFNR':customer})
            out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E1EDK01'},{'BOTSID':'E1EDKA1','PARVW':'RE','LIFNR':customer,'PARTN':customer})
            out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E1EDK01'},{'BOTSID':'E1EDKA1','PARVW':'LF','LIFNR':vendor,'PARTN':vendor})

            out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E1EDK01'},{'BOTSID':'E1EDK02','QUALF':'009','BELNR':INVNUM})

            out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E1EDK01'},{'BOTSID':'E1EDK03','IDDAT':'012','DATUM':BCHDATE})
            out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E1EDK01'},{'BOTSID':'E1EDK03','IDDAT':'026','DATUM':INVDATE})

            out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E1EDK01'},{'BOTSID':'E1EDK04','MSATZ':GSTpercent,'MWSBT':TOTGSTAMT})


        # Line info
        COUNT = COUNT+1
        lou = out.putloop({'BOTSID':'EDI_DC40'},{'BOTSID':'E1EDK01'},{'BOTSID':'E1EDP01'})

        lou.put({'BOTSID':'E1EDP01','POSEX':dtl.get({'BOTSID':'DTL','INVLIN':None})})
        lou.put({'BOTSID':'E1EDP01','MENGE':dtl.get({'BOTSID':'DTL','INVQTY':None})})
        lou.put({'BOTSID':'E1EDP01','MENEE':UOM})
        lou.put({'BOTSID':'E1EDP01','VPREI':dtl.get({'BOTSID':'DTL','PRCPER':None})})
        lou.put({'BOTSID':'E1EDP01','NETWR':dtl.get({'BOTSID':'DTL','TOTAMT':None})})

        lou.put({'BOTSID':'E1EDP01'},{'BOTSID':'E1EDP02','QUALF':'001','BELNR':ORDNUM})
        #lou.put({'BOTSID':'E1EDP01'},{'BOTSID':'E1EDP02','QUALF':'001','ZEILE':???}) PO line number not known

        lou.put({'BOTSID':'E1EDP01'},{'BOTSID':'E1EDP19','QUALF':'001','IDTNR':dtl.get({'BOTSID':'DTL','MATNUM':None})})
        lou.put({'BOTSID':'E1EDP01'},{'BOTSID':'E1EDP19','QUALF':'002','IDTNR':dtl.get({'BOTSID':'DTL','MATNUM':None})})

        lou.put({'BOTSID':'E1EDP01'},{'BOTSID':'E1EDP26','QUALF':'003','BETRG':dtl.get({'BOTSID':'DTL','TOTAMT':None})})

        # Summary info
        out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E1EDK01'},{'BOTSID':'E1EDS01','SUMID':'001','SUMME':COUNT})
        out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E1EDK01'},{'BOTSID':'E1EDS01','SUMID':'010','WAERQ':currency,'SUMME':TOTEXCGST})
        out.put({'BOTSID':'EDI_DC40'},{'BOTSID':'E1EDK01'},{'BOTSID':'E1EDS01','SUMID':'011','WAERQ':currency,'SUMME':TOTINCGST})

# retrieve and delete a saved value from the header
def get_hdr_value(domain,key):
    value = transform.persist_lookup(domain,key)
    transform.persist_delete(domain,key)
    return value


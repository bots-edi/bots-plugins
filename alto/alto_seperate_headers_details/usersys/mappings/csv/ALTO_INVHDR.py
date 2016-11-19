# Mike Griffin 25/02/2010

import bots.transform as transform

def main(inn,out):

    transform.inn2out(inn,out)      #as bots needs an outgoing file, the file with header is just passed; goes to channel DISCARD; is not used

    for hdr in inn.getloop({'BOTSID':'HDR'}):
      INVNUM = hdr.get({'BOTSID':'HDR','INVNUM':None})

      save_hdr_value('BCHDATE',  INVNUM,hdr.get({'BOTSID':'HDR','BCHDATE':None}))
      save_hdr_value('INVDATE',  INVNUM,hdr.get({'BOTSID':'HDR','INVDATE':None}))
      save_hdr_value('ORDNUM',   INVNUM,hdr.get({'BOTSID':'HDR','ORDNUM':None}))
      save_hdr_value('TOTEXCGST',INVNUM,hdr.get({'BOTSID':'HDR','TOTEXCGST':None}))
      save_hdr_value('TOTGSTAMT',INVNUM,hdr.get({'BOTSID':'HDR','TOTGSTAMT':None}))
      save_hdr_value('TOTINCGST',INVNUM,hdr.get({'BOTSID':'HDR','TOTINCGST':None}))


# save header values for later use in detail mapping
def save_hdr_value(domain,key,value):
    try:
      transform.persist_add(domain,key,value)
    except: # this should not happen, but just in case...
      transform.persist_update(domain,key,value)


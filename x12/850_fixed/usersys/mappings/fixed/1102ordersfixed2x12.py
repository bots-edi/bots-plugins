#mapping-script
import time

def main(inn,out):
    #~ print 'translation script 11ordersfixed2x12.py'
    out.put({'BOTSID':'ST','ST02':out.ta_info['reference'],'ST01':'850'})
    out.put({'BOTSID':'ST'},{'BOTSID':'BEG','BEG01':'00','BEG02':'00','BEG03':'00','BEG05':time.strftime('%Y%m%d')})

    for regel in inn.getloop({'BOTSID':'HEA'},{'BOTSID':'LIN'}):
        lou = out.putloop({'BOTSID':'ST'},{'BOTSID':'PO1'})
        lou.put({'BOTSID':'PO1','PO101':regel.get({'BOTSID':'LIN','REGEL':None})})

    out.put({'BOTSID':'ST'},{'BOTSID':'SE','SE01':out.getcount()+1,'SE02':out.ta_info['reference']})  #last line (counts the segments produced in out-message)

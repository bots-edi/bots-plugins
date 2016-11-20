#mapping-script
import bots.transform as transform

def main(inn,out):
    #swap sender/receiver
    out.ta_info['topartner'] = inn.ta_info['frompartner']
    out.ta_info['frompartner'] = inn.ta_info['topartner']
    out.ta_info['testindicator'] = inn.ta_info['testindicator']
    
    out.put({'BOTSID':'UNH','0062':out.ta_info['reference'],'S009.0065':'APERAK','S009.0052':'D','S009.0054':'96A','S009.0051':'UN'})
    out.put({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':out.ta_info['reference']})
    out.put({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2379':'203','C507.2380':transform.strftime('%Y%m%d%H%M')})
    
    srtmes = inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':None})
    srtmes_converted = transform.ccode('aperakrff2qualifer',srtmes)
    mesdate = inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2380':None})
    mesformat = inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2379':None})
    out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':srtmes_converted,'C506.1154':inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':srtmes_converted},{'BOTSID':'DTM','C507.2005':'171','C507.2379':mesformat,'C507.2380':mesdate})
        
    #return same parties/NAD as in received message
    for nad in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'NAD'}):
        nad2 = out.putloop({'BOTSID':'UNH'},{'BOTSID':'NAD'})
        nad2.put({'BOTSID':'NAD','3035':nad.get({'BOTSID':'NAD','3035':None})})
        nad2.put({'BOTSID':'NAD','C082.3039':nad.get({'BOTSID':'NAD','C082.3039':None})})
        nad2.put({'BOTSID':'NAD','C082.3055':nad.get({'BOTSID':'NAD','C082.3055':None})})
    out.put({'BOTSID':'UNH'},{'BOTSID':'UNT','0074':out.getcount()+1,'0062':out.ta_info['reference']})

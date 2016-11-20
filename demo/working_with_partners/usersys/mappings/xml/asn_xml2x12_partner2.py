#mapping-script
import bots.transform as transform
import asn_xml2x12_default

def main(inn,out):
    #first do default 856 mapping
    asn_xml2x12_default.main(inn,out)
    
    #########################################################################################################
    #specific mapping for PARTNER2
    
    #the delivery date for this partner is not always OK, delete to prvent misinterpretation
    for shipment in out.getloop({'BOTSID':'ST'},{'BOTSID':'HL','HL03':'S'}):  
        shipment.delete({'BOTSID':'HL'},{'BOTSID':'DTM','DTM01':'017'})         #delete whole segment: delivery dates (qualier 17) in HL-shipments)

    
    ##requires different coded for buyers part number
    for lin in out.getloop({'BOTSID':'ST'},{'BOTSID':'HL','HL03':'I'},{'BOTSID':'LIN'}): 
        lin.change(where=({'BOTSID':'LIN'},),change={'LIN01':None})     #delete a field: line number in lin segments
        lin.change(where=({'BOTSID':'LIN','LIN06':'BP'},),change={'LIN06':'IN'})     #replace in segment. Note: 'where' has to be a tuple; python requires something like (1,) for tuple with one element
        lin.change(where=({'BOTSID':'LIN'},),change={'LIN08':'XX','LIN09':'ADD VALUE'})     #add fields

    
    out.change(where=({'BOTSID':'ST'},{'BOTSID':'SE'}),change={'SE01':str(out.getcount())})  #recalculate SE counter

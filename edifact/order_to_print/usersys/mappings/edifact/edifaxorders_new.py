#mapping-script

def main(inn,out):
    out.put({'BOTSID':'Orderheader','Sender':inn.ta_info['frompartner']})
    out.put({'BOTSID':'Orderheader','Receiver':inn.ta_info['topartner']})
    
    out.put({'BOTSID':'Orderheader','Order number':inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':None})})
    out.put({'BOTSID':'Orderheader','Order type':inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':None})})
    
    out.put({'BOTSID':'Orderheader','Order date':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2380':None})})
    out.put({'BOTSID':'Orderheader','Delivery date':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'2','C507.2380':None})})
    out.put({'BOTSID':'Orderheader','Earliest delivery date':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'64','C507.2380':None})})
    out.put({'BOTSID':'Orderheader','Latest delivery date':inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'63','C507.2380':None})})
    
    out.put({'BOTSID':'Orderheader','Buyer':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY','C082.3039':None})})
    out.put({'BOTSID':'Orderheader','Supplier':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3039':None})})
    out.put({'BOTSID':'Orderheader','Delivery place':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'DP','C082.3039':None})})
    out.put({'BOTSID':'Orderheader','Haul address':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SF','C082.3039':None})})
    out.put({'BOTSID':'Orderheader','Final destination':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'UC','C082.3039':None})})
    out.put({'BOTSID':'Orderheader','Invoice address':inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'IV','C082.3039':None})})
    
    for lin in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'LIN'}):
        lou = out.putloop({'BOTSID':'Orderheader'},{'BOTSID':'Lines'})
        lou.put({'BOTSID':'Lines','Line number':lin.get({'BOTSID':'LIN','1082':None})})
        lou.put({'BOTSID':'Lines','Item number':lin.get({'BOTSID':'LIN','C212.7140':None})})
        lou.put({'BOTSID':'Lines','Quantity':lin.get({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'21','C186.6060':None})})
        lou.put({'BOTSID':'Lines','Description':lin.get({'BOTSID':'LIN'},{'BOTSID':'IMD','C273.7008#1':None})})

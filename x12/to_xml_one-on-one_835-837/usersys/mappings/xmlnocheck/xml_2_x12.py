#mapping-script
import copy

def main(inn,out):
    for isa in inn.getloop({'BOTSID':'ISA'}):
        out.ta_info['frompartner'] = isa.get({'BOTSID':'ISA','ISA06':None})
        out.ta_info['topartner'] = isa.get({'BOTSID':'ISA','ISA08':None})
        for gs in isa.getloop({'BOTSID':'ISA'},{'BOTSID':'GS'}):
            version = gs.get({'BOTSID':'GS','GS08':None})
            for st in gs.getloop({'BOTSID':'GS'},{'BOTSID':'ST'}):
                out.ta_info['messagetype'] = st.get({'BOTSID':'ST','ST01':None}) + version  #set right x12 messagetype
                out.root = copy.deepcopy(st)

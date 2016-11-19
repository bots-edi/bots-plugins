#mapping-script
import bots.transform as transform

def xmltag2edifacttag(node):
    #edifact tags are numerical; xml does not allow numerical tags. This function fixed this
    if node.record is not None:
        for key,value in node.record.items():
            if key not in ['BOTSID','BOTSIDnr']:
                del node.record[key]
                key = key[1:].replace('_','#')
                node.record[key] = value
    for child in node.children:
        xmltag2edifacttag(child)


def main(inn,out):
    out.ta_info['frompartner'] = 'FAKE FROM PARTNER'   #only a demo
    out.ta_info['topartner'] = 'FAKE TO PARTNER'   #only a demo
    transform.inn2out(inn,out)
    xmltag2edifacttag(out.root)   #edifact tags are numerical; xml does not allow numerical tags. This function fixed this

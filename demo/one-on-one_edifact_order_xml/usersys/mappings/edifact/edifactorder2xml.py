#mapping-script
import bots.transform as transform

def tag2validxmltag(node):
    #edifact tags are numerical; xml does not allow numerical tags. This function fixed this
    if node.record is not None:
        for key,value in node.record.items():
            if key not in ['BOTSID', 'BOTSIDnr']:
                del node.record[key]            #delete old key
                key = key.replace('#','_')      #character '#' is not allowed in xml
                node.record['_' + key] = value
    for child in node.children:
        tag2validxmltag(child)


def main(inn,out):
    transform.inn2out(inn,out)
    tag2validxmltag(out.root)   #edifact tags are numerical; xml does not allow numerical tags. This function fixed this
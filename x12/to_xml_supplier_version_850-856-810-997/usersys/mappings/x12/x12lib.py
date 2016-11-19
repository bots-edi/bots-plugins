
def get_art_num(node, qualifier,start=6,end=25):
    ''' helper function to get to get art_nr with right qualifier in line segment (PO1, etc) .
    '''
    tag = node.record['BOTSID']
    list_searchable_elements = [('%s%02d'%(tag,i),'%s%02d'%(tag,i+1)) for i in range(start,end,2)]
    for qualifier_element,id_element in list_searchable_elements:
        result = node.get({'BOTSID':tag,qualifier_element:qualifier,id_element:None})
        if result:
            return result
    return None

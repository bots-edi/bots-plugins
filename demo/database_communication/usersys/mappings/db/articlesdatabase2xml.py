#mapping-script

def main(inn,out):
    out.put({'BOTSID':'articles'})          #have to put root element in first.
    for article in inn.root['articles']:    #map the data from the query to the xml message 
        art = out.putloop({'BOTSID':'articles'},{'BOTSID':'article'})       #make new xml entity 'article' within root
        art.put({'BOTSID':'article','ccodeid':article[0],'leftcode':article[1],'rightcode':article[2]})

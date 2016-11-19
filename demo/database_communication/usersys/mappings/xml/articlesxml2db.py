#mapping-script

def main(inn,out):
    #out.root will be passed to the db-connector
    #in this simple case: out.root is a list. In the list: a tuple for each article.
    out.root = []
    #loop over the articles in the xml-message
    for art in inn.getloop({'BOTSID':'articles'},{'BOTSID':'article'}):
        #for each article: make a tuple; this tuple is appended to out.root
        article = (art.get({'BOTSID':'article','ccodeid':None}),art.get({'BOTSID':'article','leftcode':None}),art.get({'BOTSID':'article','rightcode':None}))
        out.root.append(article)

    out.ta_info['merge'] = False    #files should not be merged

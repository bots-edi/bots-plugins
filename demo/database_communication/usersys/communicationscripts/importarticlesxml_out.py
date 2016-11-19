''' This communication script writes the article-inforamtion to the sqlite database. 
    A sqlite database is provided in this plugin.
    The parameters for the database-connection (in case of sqlite: only the path to the database) is in the channel (as configured in the GUI).
    For more information about the SQLite databas connector: see regular python documentation about this.
    For other databases there are other database connectors, google them for the right information.
'''
import sqlite3

def connect(channeldict):
    #open connection to the sqlite database
    #the connection is returned.
    return sqlite3.connect(database=channeldict['path'])


def outcommunicate(channeldict,dbconnection,db_object):
    #trick. If plugin is ran more than once, an error occurs complaining about not uniqueness of enties...of course ;-))********
    cursor = dbconnection.cursor()
    cursor.execute("DELETE FROM ccode")
    dbconnection.commit()
    cursor.close()
    #end of trick****************************************************
    
    #the edi-data is passed from the mapping script. In the case it is a list with tuples; each tuple is for one article. 
    cursor = dbconnection.cursor()
    for article in db_object:
        cursor.execute(u'''INSERT INTO ccode (ccodeid,leftcode,rightcode)
                            VALUES   (?, ?, ?)''',
                            article)
    dbconnection.commit()
    cursor.close()
    
    
def disconnect(channeldict,dbconnection):
    dbconnection.close()

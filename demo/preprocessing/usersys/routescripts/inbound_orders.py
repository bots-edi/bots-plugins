#imports for bots modules that are used:
import bots.preprocess as preprocess
import bots.botslib as botslib
import bots.botsglobal as botsglobal
from bots.botsconfig import *

def postincommunication(routedict,*args,**kwargs):
    ''' function is called after the communication in the route.
    '''
    preprocess.preprocess(routedict=routedict,function=my_preprocess_function)

def my_preprocess_function(ta_from,endstatus,*args,**kwargs):
    ''' 
        Problem here is that the edi-file starts with an number of '#' and '@'.
        This function removes these.
    ''' 
    content = botslib.readdata(filename=ta_from.filename)       #read content of incoming file.
    content = content.lstrip('#@\r\n')                              #convert content
    ta_to = ta_from.copyta(status=endstatus)    #make new transaction for bots database
    tofilename = str(ta_to.idta)                #generate filename to write converted data to
    tofile = botslib.opendata(tofilename,'wb')  #open file for converted data.
    tofile.write(content)                       #write the converted data
    tofile.close()                              #close the file
    ta_to.update(statust=OK,filename=tofilename) #update outmessage transaction with ta_info;
    botsglobal.logger.debug(u'        File written: "%s".',tofilename)   #do logging

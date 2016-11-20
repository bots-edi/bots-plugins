import os
import glob
import shutil

def connect(channeldict):
    print 'connect',channeldict['idchannel']

def main(channeldict,filename,*args,**kargs):
    if os.path.exists(filename):
        print 'main received:', filename
        #~ #you could eg copy file to other place
        #~ tofilename = os.path.join('some path',os.path.basename(filename))
        #~ shutil.copyfile(fromfilename,tofilename)
    else:
        print 'main did NOT receive:', filename

def disconnect(channeldict):
    print 'disconnect',channeldict['idchannel']

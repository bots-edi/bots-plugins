import os
import glob
import shutil

def connect(channeldict):
    print '\n\nconnect',channeldict['idchannel']
    
    #Place all files in right directory (channeldict['path'])
    #copies the edi files from an existing dir to the dir where bots picks them up....just testing
    for fromfilename in glob.glob('botssys/infile/demo_comscript/source/*'):
        tofilename = os.path.join(channeldict['path'],os.path.basename(fromfilename))
        print 'sends:', tofilename
        shutil.copyfile(fromfilename,tofilename)

#no 'main' method

def disconnect(channeldict):
    print 'disconnect',channeldict['idchannel']

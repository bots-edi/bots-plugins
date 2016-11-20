import os
import glob
import shutil

def connect(channeldict):
    print 'connect',channeldict['idchannel']

#no main method...so disconnect should pick up the files

def disconnect(channeldict):
    print 'disconnect',channeldict['idchannel']
    for filename in glob.glob(os.path.join(channeldict['path'], channeldict['filename'])):
        print 'main received:', filename

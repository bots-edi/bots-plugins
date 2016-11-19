import os
import glob
import shutil

def connect(channeldict):
    print '\n\nconnect',channeldict['idchannel']

def main(channeldict):
    print 'main',channeldict['idchannel']
    #for each file in directory: yield the filename
    for filename in glob.glob('botssys/infile/demo_comscript/source/*'):
        print 'sends:', filename
        yield filename

def disconnect(channeldict):
    print 'disconnect',channeldict['idchannel']

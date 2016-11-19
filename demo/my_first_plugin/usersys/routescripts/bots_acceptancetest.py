from __future__ import print_function
from __future__ import unicode_literals
import os
import sys
import shutil
import filecmp
import bots.botsglobal as botsglobal
import bots.botslib as botslib


def cleanoutputdir():
    ''' delete directory standard-out  'bots/botssys/out' (as indicated in bos.ini). ''' 
    botssys = botsglobal.ini.get('directories','botssys')
    shutil.rmtree(os.path.join(botssys,'outfile'),ignore_errors=True)    #remove whole output directory

def getreportlastrun():
    ''' Return the results of the last run as a dict.'''
    for row in botslib.query(u'''SELECT *
                            FROM    report
                            ORDER BY idta DESC
                            '''):
        return dict(row)
    raise Exception('no report')

def comparedicts(result_expect,result_run):
    error = ''
    for key,value in result_expect.items():
        if key not in result_run:
            error += 'Could not find key "%s" in results of run?\n'%(key)
        elif value != result_run[key]:
            error += 'Comparing key "%s": expect "%s" but got "%s"\n'%(key,value,result_run[key])
    if error:
        print('errors: %s,'%(error))

def comparerunresults(result_expect):
    ''' result_expect is a dict that contains the expected results of a run.
        These expected results are compared with the actual results. 
        Usage eg:
        CompareRunResults({'status':0,'lastreceived':6,'lasterror':0,'lastdone':6,'lastok':0,'lastopen':0,'send':4,'processerrors':0,'filesize':6638})
    '''
    result_run = getreportlastrun()
    comparedicts(result_expect,result_run)

#**************************************************************************
#**************************************************************************
#**************************************************************************

def pretest(routestorun):
    cleanoutputdir()
    #cleanpreviousruns: if ta-filereport-report have clean mark as acceptancetest!
    
    
def posttest(routestorun):
    #Compare run results
    comparerunresults({'status':0,'lastreceived':3,'lasterror':0,'lastdone':3,'lastok':0,'lastopen':0,'send':1,'processerrors':0,'filesize':1450})
    
    #Compare outgoing files.
    #Run run first, save results in 'botssys/outfile' in 'botssys/infile' (so there is a directory 'botssys/infile/outfile'....)
    #than run again; files in bot directories will be compared.
    botssys = botsglobal.ini.get('directories','botssys')
    outdir =    os.path.join(botssys,'outfile')
    compdir = os.path.join(botssys,'infile/outfile')
    cmpobj = filecmp.dircmp(outdir, compdir)
    cmpobj.report_full_closure()

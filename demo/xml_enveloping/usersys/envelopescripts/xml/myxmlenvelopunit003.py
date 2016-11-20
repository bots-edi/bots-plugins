from bots.botsconfig import *
import bots.botslib as  botslib
import bots.envelope as  envelope

class myxmlenvelopunit003(envelope.xml):
    ''' old xml enveloping; name is kept for upward comp. & as example for xml enveloping'''
    def run(self):
        ''' class for (test) xml envelope. There is no standardised XML-envelope!
            writes a new XML-tree; uses places-holders for XML-files to include; real enveloping is done by ElementTree's include'''
        include = '{http://www.w3.org/2001/XInclude}include'
        self._openoutenvelope()
        botslib.tryrunscript(self.userscript,self.scriptname,'ta_infocontent',ta_info=self.ta_info)
        
        #start filling out-tree
        self.out.put({'BOTSID':'root003'})     
        self.out.put({'BOTSID':'root003','sender':self.ta_info['topartner']})
        self.out.put({'BOTSID':'root003','receiver':self.ta_info['frompartner']})
        
        #include xml files that will be enveloped
        ta_list = self.filelist2absolutepaths() 
        for filename in ta_list:
            self.out.put({'BOTSID':'root003'},{'BOTSID':include,include + '__parse':'xml',include + '__href':filename})
        self.out.envelopewrite(self.out.root)   #'resolves' the included xml files 

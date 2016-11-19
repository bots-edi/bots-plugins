#mapping-script
#use out.data to add attributes.
#out.data is passed to the template.

def main(inn,out):
    out.data.header={}
    out.data.header['SOORT']='Edi-order versie D96A'
    out.data.header['EANZENDER']=inn.ta_info['frompartner']
    out.data.header['EANONTVANGER']=inn.ta_info['topartner']
    out.data.header['TEST']=inn.ta_info['testindicator']
    out.data.header['ORDERNUMMER']=inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','1004':None})
    out.data.header['SOORTORDER']=inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','C002.1001':None})
    out.data.header['EANAFNEMER']=inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'BY','C082.3039':None})
    out.data.header['EANLEVERANCIER']=inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SU','C082.3039':None})
    out.data.header['EANAFLEVER']=inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'DP','C082.3039':None})
    out.data.header['EANHAALADRES']=inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'SF','C082.3039':None})
    out.data.header['EANEINDBESTEMMING']=inn.get({'BOTSID':'UNH'},{'BOTSID':'NAD','3035':'UC','C082.3039':None})
    out.data.header['ORDERDATUM']=inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'137','C507.2380':None})
    out.data.header['LEVERDATUM']=inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'2','C507.2380':None})
    out.data.header['VLEVERDATUM']=inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'64','C507.2380':None})
    out.data.header['LLEVERDATUM']=inn.get({'BOTSID':'UNH'},{'BOTSID':'DTM','C507.2005':'63','C507.2380':None})
    out.data.header['ACCIJNSVRIJ']='accijnsvrij' if inn.get({'BOTSID':'UNH'},{'BOTSID':'TAX','5283':'7','C241.5153':'ACT','5305':'E'}) else None
    out.data.header['GEIMPROVISEERD']='geimproviseerd' if inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','1225':'46'}) else None
    out.data.header['INDICATIEONTVANGSTBEVESTIGING']='ontvangstbevestiging gevraagd' if inn.get({'BOTSID':'UNH'},{'BOTSID':'BGM','4343':'AB'}) else None
    out.data.header['BACKHAULING']='order wordt gehaald' if inn.get({'BOTSID':'UNH'},{'BOTSID':'TOD','4055':'4'}) else None
    out.data.header['SPOEDORDER']='spoedorder' if inn.get({'BOTSID':'UNH'},{'BOTSID':'TOD','4055':'3','C100.4053':'02E'}) else None
    out.data.header['WINKELINSTALLATIE']='winkelinstallatie' if inn.get({'BOTSID':'UNH'},{'BOTSID':'ALI','4183#1':'77E'}) else None
    out.data.header['RAAMORDERNUMMER']=inn.get({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'BO','C506.1154':None})
    out.data.header['ACTIENUMMER']=inn.get({'BOTSID':'UNH'},{'BOTSID':'RFF','C506.1153':'PD','C506.1154':None})
        
    out.data.lines=[]
    for lin in inn.getloop({'BOTSID':'UNH'},{'BOTSID':'LIN'}):
        out.data.lines.append({})
        out.data.lines[-1]['REGEL']=lin.get({'BOTSID':'LIN','1082':None})
        out.data.lines[-1]['ARTIKEL']=lin.get({'BOTSID':'LIN','C212.7140':None})
        out.data.lines[-1]['BESTELDAANTAL']=lin.get({'BOTSID':'LIN'},{'BOTSID':'QTY','C186.6063':'21','C186.6060':None})
        out.data.lines[-1]['PROMOTIECODE']=lin.get({'BOTSID':'LIN'},{'BOTSID':'RFF','C506.1153':'PD','C506.1154':None})
        out.data.lines[-1]['ARTIKELOMSCHRIJVING']=lin.get({'BOTSID':'LIN'},{'BOTSID':'IMD','C273.7008#1':None})

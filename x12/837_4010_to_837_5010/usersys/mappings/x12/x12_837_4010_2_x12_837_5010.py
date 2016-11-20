#mapping-script
import bots.transform as transform
def main(inn,out):
    transform.inn2out(inn,out)
    out.delete({'BOTSID':'ST'},{'BOTSID':'REF','REF01':'87'})
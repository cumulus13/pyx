import sys
import comtypes.client as cc
import comtypes
import argparse
import os
import argparse

class IDMan(object):
    def __init__(self):
        super(IDMan, self)
        self.tlb = r'c:\Program Files\Internet Download Manager\idmantypeinfo.tlb'

    def download(self, link, path_to_save=None, output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None):
        #print "link =", link
        #print "referrer =", referrer
        #print "postData =", postData
        #print "user     =", user
        #print "password =", password
        #print "path_to_save =", path_to_save
        #print "output   =", output
        #print "lflag    =", lflag
        if confirm:
            lflag = 0
        else:
            lflag = 5
        try:
            cc.GetModule(['{ECF21EAB-3AA8-4355-82BE-F777990001DD}', 1, 0])
        except:
            cc.GetModule(self.tlb)

        import comtypes.gen.IDManLib as idman 
        idman1 = cc.CreateObject(idman.CIDMLinkTransmitter, None, None, idman.ICIDMLinkTransmitter2)
        if path_to_save:
            os.path.realpath(path_to_save)
        idman1.SendLinkToIDM(link, referrer, cookie, postData, user, password, path_to_save, output, lflag)
    
    def usage(self):
        parse = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
        parse.add_argument('URL', action='store', help='url to download')
        parse.add_argument('-p', '--path', action='store', help='Path to save', default=os.getcwd())
        parse.add_argument('-o', '--output', help='Save with different name', action='store')
        parse.add_argument('-c', '--confirm', help='Confirm before download', action='store_true')
        if len(sys.argv) ==1:
            parse.print_help()
        else:
            args = parse.parse_args()
            self.download(args.URL, args.path, args.output, confirm=args.confirm)
        

if __name__ == '__main__':
    c = IDMan()
    c.usage()
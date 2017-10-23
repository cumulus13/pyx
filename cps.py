import shutil
import os
import sys
import argparse


class cps(object):

    def __init__(self):
        super(cps, self)

    def copy_file(self, fr, to):
        fr = os.path.abspath(fr)
        to = os.path.basename(to)
        dest_to = os.path.dirname(fr)
        dest_to = os.path.join(dest_to, to)
        print "copy file '{0}' --> '{1}'".format(fr, dest_to)
        shutil.copyfile(fr, dest_to)

    def copy_dir(self, fr, to):
        fr = os.path.abspath(fr)
        to = os.path.basename(to)
        dest_to = os.path.dirname(fr)
        dest_to = os.path.join(dest_to, to)
        if os.path.isdir(dest_to):
            q1 = raw_input(
                'Directory name to EXISTS !, overwrite [y/n]: ')
            if q1 == 'y':
                print "removes directory '{0}'".format(dest_to)
                os.removedirs(dest_to)
                if not os.path.isdir(dest_to):
                    print "copy dirs '{0}' --> '{1}'".format(fr, dest_to)
                    shutil.copytree(fr, dest_to)
                else:
                    print "Directory can't removed, may be it's locked !, please remove manually before !"

    def usage(self):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument(
            'FROM', help='Copy From', action='store')
        parser.add_argument(
            'TO', help='Copy To', action='store')
        if len(sys.argv) == 1:
            parser.print_help()
        else:
            args = parser.parse_args()
            if os.path.isfile(args.FROM):
                self.copy_file(args.FROM, args.TO)
            elif os.path.isfile(args.FROM):
                self.copy_dir(args.FROM, args.TO)
            else:
                print "[Bugs] it's not FILE or DIR !"

if __name__ == '__main__':
    c = cps()
    c.usage()

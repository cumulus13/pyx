import os
import sys
import argparse
import shutil
import cover

class coverin(object):
    def __init__(self, **kwargs):
        super(coverin, self)

    def listdir(self, path):
        paths = os.listdir(path)
        paths2 = []
        for i in paths:
            if os.path.isdir(i):
                paths2.append(os.path.join(path, i))
        return paths2

    def covers(self, path, filename = None):
        if isinstance(path, list) and len(path) == 1:
            path = path[0]
        #print "PATH =", path
        #print "type(PATH) =", type(path)
        if not isinstance(path, list) and os.path.isfile(path):
            s_path = os.path.dirname(path)
            s_file = os.path.basename(path)
            s_file_ext = os.path.splitext(s_file)[1]
            if s_file_ext.lower() != ".jpg":
                from PIL import Image
                im = Image.open(path)
                im.save(os.path.join(path, os.path.splitext(os.path.basename(path))[0]) + ".jpg")
                copyall(os.path.join(path, os.path.splitext(os.path.basename(path))[0]) + ".jpg", path, ".jpg")            
            #os.chdir(s_path)
            #if not os.path.isfile(os.path.join(s_path, 'cover.jpg')):
            cover.copyall(s_file, s_path)
        elif isinstance(path, list):
            #print "AAA"
            for i in path:
                if os.path.isfile(i):
                    s_path = os.path.dirname(i)
                    s_file = os.path.basename(i)
                    s_file_ext = os.path.splitext(s_file)[1]
                    if s_file_ext.lower() != ".jpg":
                        from PIL import Image
                        im = Image.open(i)
                        im.save(os.path.join(i, os.path.splitext(os.path.basename(i))[0]) + ".jpg")
                        copyall(os.path.join(i, os.path.splitext(os.path.basename(i))[0]) + ".jpg", path, ".jpg")            
                    cover.copyall(s_file, s_path)
                elif os.path.isdir(i):
                    if filename == None:
                        if os.path.isfile(os.path.join(i, 'cover.jpg')):
                            cover.copyall(os.path.join(i, 'cover.jpg'), i)
                        elif os.path.isfile(os.path.join(i, 'Cover.jpg')):
                            cover.copyall(os.path.join(i, 'Cover.jpg'), i)
                        elif os.path.isfile(os.path.join(i, 'Cover.png')):
                            from PIL import Image
                            im = Image.open(os.path.join(i, 'Cover.png'))
                            #print "os.path.join(i, os.path.splitext(os.path.join(i, 'Cover.png')[0])) =", os.path.join(i, os.path.splitext(os.path.join(i, 'Cover.png')[0]))
                            #if isinstance(path, list):
                                #print "AAA 0  =", os.path.join(i, os.path.splitext(os.path.join(i, 'Cover.png'))[0]) + ".jpg"
                                #print "PATH 0 =", path

                            #else:
                            im.save(os.path.join(i, os.path.splitext(os.path.join(i, 'Cover.png'))[0]) + ".jpg")
                            #print "AAA 1  =", os.path.join(i, os.path.splitext(os.path.join(i, 'Cover.png'))[0]) + ".jpg"
                            #print "PATH 1 =", path
                            cover.copyall(os.path.join(i, os.path.splitext(os.path.join(i, 'Cover.png'))[0]) + ".jpg", i, ".jpg")
                        elif os.path.isfile(os.path.join(i, 'cover.png')):
                            from PIL import Image
                            im = Image.open(os.path.join(i, 'cover.png'))
                            im.save(os.path.join(i, os.path.splitext(os.path.join(i, 'cover.png'))[0]) + ".jpg")
                            cover.copyall(os.path.join(i, os.path.splitext(os.path.join(i, 'cover.png'))[0]) + ".jpg", i, ".jpg")                                    
                    else:
                        if os.path.isfile(filename):
                            ext = os.path.splitext(filename)[1]
                            if ext.lower() != ".jpg":
                                from PIL import Image
                                im = Image.open(i)
                                im.save(os.path.join(filename, os.path.splitext(os.path.basename(i))[0]) + ".jpg")
                                cover.copyall(os.path.join(filename, os.path.splitext(os.path.basename(i))[0]) + ".jpg", i, ".jpg")
                            else:
                                cover.copyall(filename, i)
    def usage(self):
        parser = argparse.ArgumentParser(formatter_class= argparse.RawTextHelpFormatter)
        parser.add_argument('-f', '--filename', help = 'File image copy to', action = 'store')
        parser.add_argument('PATH', help = 'List of dirs contain image cover or file cover', action = 'store', nargs = '*')
        parser.add_argument('-r', '--recursive', help = 'Rename all of file cover image in all folders', action = 'store_true')
        
        if len(sys.argv) == 1:
            parser.print_help()
        else:
            args = parser.parse_args()
            if args.PATH:
                if args.recursive:
                    for i in args.PATH:
                        dirs = self.listdir(os.path.abspath(i))
                        #print "Dirs =", dirs
                        self.covers(dirs, args.filename)
                else:
                    dirs = args.PATH
                    self.covers(dirs, args.filename)
            else:
                dirs = None
                
            #if dirs:
                #self.covers(dirs, args.filename)
            if not dirs:
                print "\n"
                print "NOT DIRS"
                parser.print_help()
                
if __name__ == '__main__':
    c = coverin()
    c.usage()
                

import os
import optparse
import sys


class rnx(object):

    def __init__(self):
        super(rnx, self)

    def rename(self, path, dest=None, upper=None, lower=None, title=None, ext=None, allchange=None, overwrite=None, replace=None):
        path = os.path.abspath(path)
        if ext != None:
            if "." not in ext[0]:
                ext = "." + ext
        if dest == None:
            dest = path

        dest_ext = os.path.splitext(os.path.abspath(dest))[1]
        dest_dir = os.path.dirname(dest)
        dest_name = os.path.basename(dest)

        path_ext = os.path.splitext(path)[1]
        path_dir = os.path.dirname(path)
        path_name = os.path.basename(path)
        if dest_dir == '':
            dest_dir = path_dir
        if dest_ext == '' or dest_ext == None or len(dest_ext) > 8:
            dest_ext = path_ext
        else:
            dest_name = os.path.splitext(dest)[0]
        if ext:
            dest_ext = ext
        if upper:
            dest_name = str(dest_name).upper()
            if allchange:
                dest_ext = str(dest_ext).upper()
        if lower:
            dest_name = str(dest_name).lower()
            if allchange:
                dest_ext = str(dest_ext).lower()
        if title:
            dest_name = str(dest_name).title()
            if allchange:
                dest_ext = str(dest_ext).title()
        file_dest = os.path.join(dest_dir, dest_name + dest_ext)
        print "file_dest 1 =", file_dest
        if replace:
            file_dest = self.replace(replace, file_dest)
        print "file_dest 2 =", file_dest
        # if isinstance(replace, list):
        #     if len(replace) > 0:
        #         for i in replace:
        #             if isinstance(i, dict):
        #                 file_dest = str(os.path.basename(file_dest)).replace(i.get('from'), i.get('to'))
        if os.path.exists(file_dest):
            if overwrite:
                os.remove(file_dest)
        ren = ''
        try:
            ren = os.rename(path, file_dest)
        except:
            pass
        while 1:
            if ren != None:
                try:
                    ren = os.rename(path, file_dest)
                except:
                    pass
            else:
                break
        print "\n"
        print "rename : \"" + path + "\" ---> " + file_dest

    def _multi_rename(self, path, dest, upper, lower, title, ext, allchange, count=None, overwrite=None, replace=None):
        if isinstance(dest, str):
            if "|" in dest:
                dest1 = []
                dest = str(dest).split("|")
                for i in dest:
                    dest1.append(str(i).strip())
                dest = dest1
            else:
                dest = [dest]
        if isinstance(path, list):
            if len(path) > 0:
                for i in path:
                    if "*" in path:
                        self.start_rename(path, dest, upper,
                                          lower, title, ext, allchange, count)
                    if len(path) == len(dest):
                        self.rename(i, dest[path.index(i)],
                                    upper, lower, title, ext, allchange)
                    else:
                        if count:
                            if len(str(path.index(i))) == 1:
                                n = "0" + str(path.index(i) + 1)
                            else:
                                n = str(path.index(i) + 1)
                            self.rename(i, dest[0] + n, upper,
                                        lower, title, ext, allchange, overwrite, replace)

    def multi_ren(self, path, dest, upper, lower, title, ext, allchange, count=True, recursive=None, overwrite=None, replace=None):
        if os.path.isdir(path):
            list_path1 = os.listdir(path)
            list_path = []
            for i in list_path1:
                list_path.append(os.path.join(os.path.abspath(path), i))
            if recursive:
                list_path = []
                for root, dirs, files in os.walk(path):
                    if len(files) > 0:
                        for i in files:
                            f = os.path.join(root, i)
                            list_path.append(f)
            self._multi_rename(list_path, dest, upper, lower,
                               title, ext, allchange, count, overwrite, replace)

    def start_rename(self, path, dest, upper, lower, title, ext, allchange, count=True, recursive=None, overwrite=None, replace=None):
        list_dir = []
        ends = ''
        if "*" in path:
            if os.path.dirname(path) != '':
                dirname = os.path.dirname(path)
            else:
                dirname = os.getcwd()
            index_start = path.index('*')
            if len(path) != index_start + 1:
                ends = path[(index_start + 1):]
            if recursive:
                list_dir = []
                for root, dirs, files in os.walk(dirname):
                    if len(files) > 0:
                        for i in files:
                            list_dir.append(os.path.join(root, i))
            else:
                list_dir = []
                list_dir0 = os.listdir(dirname)
                for i in list_dir0:
                    list_dir.append(os.path.join(root, i))
            list_dir1 = []
            for i in list_dir:
                if ends != '':
                    if str(i).endswith(ends):
                        list_dir1.append(i)
            if len(list_dir1) > 0:
                list_dir = list_dir1

            self.multi_ren(list_dir, dest, upper, lower, title,
                           ext, allchange, count, recursive, overwrite, replace)

    def replace(self, data, filename):
        filename, ext = os.path.splitext(filename)
        if isinstance(data, list):
            for i in data:
                fr, to = i.split(":")
                if to == '':
                    to = ' '
                filename = str(filename).replace(fr, to)
        else:
            fr, to = data.split(":")
            if to == '':
                to = ' '
            filename = str(filename).replace(fr, to)
        return filename + ext

    def usage(self):
        parser = optparse.OptionParser()
        parser.add_option(
            '-u', '--upper', help='Rename to upper case too', action='store_true')
        parser.add_option(
            '-l', '--lower', help='Rename to lower case too', action='store_true')
        parser.add_option(
            '-t', '--title', help='Rename to title case too', action='store_true')
        parser.add_option(
            '-e', '--ext', help='Destination Extention to', action='store')
        parser.add_option(
            '-a', '--all', help='Rename all (name + ext) to case to', action='store_true')
        parser.add_option(
            '-c', '--count', help='Rename all + count (start from 01), use with -i', action='store_true', default=True)
        parser.add_option(
            '-R', '--recursive', help='Recursive Rename, use with -i', action='store_true')
        parser.add_option(
            '-i', '--inside', help='Rename inside', action='store_true')
        parser.add_option(
            '-d', '--dest', help='Options destination name, separator "|" with quota, example: "aaa|bbb|ccc"', action='store')
        parser.add_option(
            '-o', '--overwrite', help='Overwrite if exists', action='store_true')
        parser.add_option(
            '-r', '--replace', help='Replace string format is [string from]:[strong to], example: -R data01:data02, this will change string "data01" to "data02"')

        options, args = parser.parse_args()
        print "args =", args
        if len(sys.argv) == 1:
            parser.print_help()
        else:
            if not len(args) == 2:
                if not len(args) == 1:
                    print "Please definition your path file to rename ! \n"
                    parser.print_help()
                else:
                    args.append(None)
            if options.inside:
                if os.path.isdir(args[0]):
                    if options.dest:
                        try:
                            self.multi_ren(args[0], options.dest, options.upper, options.lower, options.title,
                                           options.ext, options.all, options.count, options.recursive, options.overwrite, options.replace)
                        except KeyboardInterrupt:
                            print "CANCEL"
                    else:
                        try:
                            self.multi_ren(args[0], args[1], options.upper, options.lower, options.title,
                                           options.ext, options.all, options.count, options.recursive, options.overwrite, options.replace)
                        except KeyboardInterrupt:
                            print "CANCEL"
                else:
                    print "Please definition inside path dir(ectory) NOT a FILE !\n"
                    parser.print_help()
                    sys.exit(0)
            else:
                try:
                    self.rename(args[0], args[1], options.upper,
                                options.lower, options.title, options.ext, options.all, options.overwrite, options.replace)
                except KeyboardInterrupt:
                    print "CANCEL"

if __name__ == '__main__':
    c = rnx()
    c.usage()

import win32api
import os
import sys
import argparse
import cmdw
MAX_LENGTH = cmdw.getWidth()
MAX_LENGTH = MAX_LENGTH - 1
#==============================================================================


def getFileProperties(fname):
    #=========================================================================
    """
    Read all properties of the given file return them as a dictionary.
    """
    propNames = ('Comments', 'InternalName', 'ProductName',
                 'CompanyName', 'LegalCopyright', 'ProductVersion',
                 'FileDescription', 'LegalTrademarks', 'PrivateBuild',
                 'FileVersion', 'OriginalFilename', 'SpecialBuild')

    props = {'FixedFileInfo': None,
             'StringFileInfo': None, 'FileVersion': None}

    try:
        # backslash as parm returns dictionary of numeric info corresponding to
        # VS_FIXEDFILEINFO struc
        fixedInfo = win32api.GetFileVersionInfo(fname, '\\')
        props['FixedFileInfo'] = fixedInfo
        props['FileVersion'] = "%d.%d.%d.%d" % (fixedInfo['FileVersionMS'] / 65536, fixedInfo[
                                                'FileVersionMS'] % 65536, fixedInfo['FileVersionLS'] / 65536, fixedInfo['FileVersionLS'] % 65536)

        # \VarFileInfo\Translation returns list of available (language, codepage)
        # pairs that can be used to retreive string info. We are using only the
        # first pair.
        lang, codepage = win32api.GetFileVersionInfo(
            fname, '\\VarFileInfo\\Translation')[0]

        # any other must be of the form \StringfileInfo\%04X%04X\parm_name, middle
        # two are language/codepage pair returned from above

        strInfo = {}
        for propName in propNames:
            strInfoPath = u'\\StringFileInfo\\%04X%04X\\%s' % (
                lang, codepage, propName)
            # print str_info
            strInfo[propName] = win32api.GetFileVersionInfo(fname, strInfoPath)

        props['StringFileInfo'] = strInfo
    except:
        pass

    return props


def rename(path, props, verbosity=None):
    name = ''
    version = ''
    if os.path.exists(path):
        for i in props:
            if isinstance(props.get(i), dict):
                for j in props.get(i):
                    if j == 'ProductVersion':
                        version = props.get(i).get(j).strip()
                    elif j == 'ProductName':
                        name = props.get(i).get(j).strip()
            else:
                if i == 'ProductVersion':
                    version = props.get(i).strip()
                elif i == 'ProductName':
                    name = props.get(i).strip()
    if verbosity:
        print "NAME    =", name
        print "VERSION =", version
        print "-" * MAX_LENGTH
        print "RENAME:", path, " --> \"" + str(name) + " v" + str(version) + os.path.splitext(path)[1] + '"'
    os.rename(path, str(str(name) + " v" +
                        str(version) + os.path.splitext(path)[1]))

def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument('PATH', help='Path File/Directory rename to', action='store')
    parser.add_argument('-r', '--rename', help='Rename File to "Filename version.ext"', action='store_true')
    parser.add_argument('-v', '--verbosity', help='Print Detail Running Process', action='store_true')
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        props = getFileProperties(args.PATH)
        if args.rename:
            rename(args.PATH, props, args.verbosity)
        else:
            if args.verbosity:
                print "props =", props
                print "-" * MAX_LENGTH
            for i in props:
                if isinstance(props.get(i), dict):
                    for j in props.get(i):
                        print j, " " * (20 - len(j)), " =", props.get(i).get(j)
                        # print j
                else:
                    print i, " " * (20 - len(i)), " =", props.get(i)

if __name__ == "__main__":
    usage()
    # import sys
    # props = getFileProperties(sys.argv[1])
    # rename(sys.argv[1], props, True)
    # print "props =", props
    # print "-" * MAX_LENGTH
    # print 'ProductVersion' in props
    # print "-" * MAX_LENGTH
    # for i in props:
    #     if isinstance(props.get(i), dict):
    #         # print "i =", props.get(i)
    #         # print "-" * MAX_LENGTH
    #         for j in props.get(i):
    #             print j, " " * (20 - len(j)), " =", props.get(i).get(j)
    #             # print j
    #     else:
    #         print i, " " * (20 - len(i)), " =", props.get(i)

#!/usr/bin/env python

from msvcrt import getch
import sys
import os
import requests
from bs4 import BeautifulSoup as bs
import argparse
import platform
if platform.uname()[0] == 'Windows':
    import cmdw
    MAX_LENGTH = int(cmdw.getWidth())
else:
    MAX_LENGTH = 180
import agl
import clipboard
import wget


class youtube(object):

    def __init__(self):
        super(youtube, self)
        # https://www.youtube.com/results?search_query=superbob&page=1
        self.youtubeURL = 'https://www.youtube.com'
        self.youtubeURLSearch = self.youtubeURL + \
            '/results?search_query={0}&page={1}'

    def getVersion(self):
        try:
            from . import __version__, __test__
            return str(__version__) + "." + str(__test__)
        except:
            import __init__
            return str(__init__.__version__) + "." + str(__init__.__test__)

    def checkReq(self, url, username=None, password=None):
        try:
            requests.get(url, auth=(username, password))
            return (True, requests.get(url, auth=(username, password)))
        except:
            return (False, None)

    def search(self, query, page=1, quality=2, index=1):
        # https://www.youtube.com/results?search_query=example
        data_search = {}
        page = str(page)
        url = self.youtubeURLSearch.format(query, page)
        r = self.checkReq(url)
        while 1:
            if not r[0]:
                r = self.checkReq(url)
            else:
                r = self.checkReq(url)[1]
                break
        s = bs(r.text)
        a = s.find_all('div', {'class': 'yt-lockup-content'})
        # print "a =", a
        # print "-"*MAX_LENGTH
        for i in a:
            b = i.find_all_next(
                'a', {'class': 'yt-uix-sessionlink yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2       spf-link '})
            # print "b =", b
            # print "-"*220
            if not b == []:
                data_search.update(
                    {index: {
                        'name': unicode(b[0].text).encode('utf-8'),
                        'title': b[0].get('title'),
                        'url': self.youtubeURL + b[0].get('href')}
                     }
                )
                index = index + 1
        index = 1
        from texttable import Texttable
        table = Texttable()
        table.set_cols_align(["l", "l", "l", "c"])
        table.set_cols_valign(["t", "m", "m", "b"])
        table.set_cols_width([
            int(MAX_LENGTH * 0.03),
            int(MAX_LENGTH * 0.30),
            int(MAX_LENGTH * 0.30),
            int(MAX_LENGTH * 0.30),
        ])
        table.header(['No', 'Name', 'Title', 'Url'])
        sys.dont_write_bytecode = True
        for i in data_search:
            try:
                name = data_search.get(i).get('name')
            except:
                name = "Error"
            try:
                title = data_search.get(i).get('title')
            except:
                title = "Error"
            try:
                url = data_search.get(i).get('url')
            except:
                url = "Error"
            # sys.stdout.write("| " + str(index) + " |" + name + "|" + title + "|" + url + "|" + "\n")
            # table.add_row([str(index), name, title, url])
            try:
                table.add_row([str(index), name, title, url])
            except:
                try:
                    table.add_row([str(index), unicode(name).encode(
                        'utf-8'), unicode(title).encode('utf-8'), unicode(url).encode('utf-8')])
                except:
                    table.add_row([str(index), self.checkName(
                        name), self.checkName(title), self.checkName(url)])
            index = index + 1
        print table.draw()
        return data_search, index

    def checkName(self, check):
        new = ''
        for i in check:
            try:
                unicode(i).decode('utf-8')
            except:
                try:
                    i = ord(i)
                except:
                    i = " "
            new = new + str(i)
        return new

    def run(self, query, page=1, quality=2, download_path=".", verbosity=None):
        index = 1
        data, index = self.search(query, page, quality, index)
        sys.stdout.write(
            "Press n for next page; b for previous page; [1-9] for page 1-9; p for custom page; d for start download; s for stop/exit [page: %s]" % str(page))
        q = getch()
        print "\n"
        while True:
            for i in range(1, 9):
                if str(q) == str(i):
                    data, index = self.search(query, q, quality, index)
                    index = index + 1
                    sys.stdout.write(
                        "Press n for next page; b for previous page; [1-9] for page 1-9; p for custom page; d for start download; s for stop/exit [page: %s]" % str(q))
                    q = getch()
                    print "\n"
            if q == 'n':
                page = page + 1
                page = int(page)
                data, index = self.search(query, page, quality, index)
                index = index + 1
                sys.stdout.write(
                    "Press n for next page; b for previous page; [1-9] for page 1-9; p for custom page; d for start download; s for stop/exit [page: %s]" % str(page))
                q = getch()
                print "\n"
            elif q == 'b':
                page = page - 1
                page = int(page)
                if page == 0:
                    page = 1
                data, index = self.search(query, page, quality, index)
                index = index + 1
                sys.stdout.write(
                    "Press n for next page; b for previous page; [1-9] for page 1-9; p for custom page; d for start download; s for stop/exit [page: %s]" % str(page))
                q = getch()
                print "\n"
            elif q == 'p':
                page = raw_input('Page Number: ')
                page = int(page)
                if page == 0:
                    page = 1
                data, index = self.search(query, page, quality, index)
                index = index + 1
                sys.stdout.write(
                    "Press n for next page; b for previous page; [1-9] for page 1-9; p for custom page; d for start download; s for stop/exit [page: %s]" % str(page))
                q = getch()
                print "\n"
            elif q == 'd':
                # print "data =", data
                # print "-"*MAX_LENGTH
                q1 = raw_input('Select Number: ')
                print "downloading ..."
                if q1 == 'all':
                    q3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                          12, 13, 14, 15, 16, 17, 18, 19, 20]
                else:
                    # print "len(q1)  =", len(q1)
                    # print "q1       =", q1
                    if len(q1) > 2:
                        q2 = str(q).split("\n")
                        q3 = []
                        for a in q2:
                            if a != '':
                                q3.append(a)
                        for x in q3:
                            self.download(data.get(int(x)).get('url'),
                                          quality, download_path, verbosity)
                            # sys.stdout.write("Press n for next page; b for previous page; [1-9] for page 1-9; d for start download; s for stop/exit")
                    else:
                        # print "downloading ..."
                        self.download(data.get(int(q1)).get('url'),
                                  quality, download_path, verbosity)
                sys.stdout.write(
                    "Press n for next page; b for previous page; [1-9] for page 1-9; d for start download; s for stop/exit")
                q = getch()
                print "\n"
            elif q == 's':
                print "[EXIT]"
                break
            elif q == 'q':
                print "[EXIT]"
                break
            else:
                print "[EXIT]"
                break
        sys.exit(0)

    def download(self, url, quality=2, download_path=".", verbosity=None):
        # print "url =", url
        a = agl.autogeneratelink()
        # b = a.generate(url, quality=quality, verbosity=verbosity, no_support=True)
        b = a.generate(url, quality=quality,
                       verbosity=verbosity, no_support=True)
        # print "type(b) =", type(b)
        # print "-" * MAX_LENGTH
        # print "b =", b
        clipboard.copy(str(b[0]))
        # print "URL Download =", b
        filename = wget.download(b[0], download_path)
        # print "-" * MAX_LENGTH
        print "has been download %s" % (os.path.abspath(filename))

    def usage(self, print_help=None):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('SEARCH', help='Query Text search', action='store')
        parser.add_argument(
            '-p', '--path', help='Path download to', action='store')
        parser.add_argument(
            '-v', '--version', help='-v = version | -vv = verbosity process', action='count')
        parser.add_argument(
            '-q', '--quality', help='Quality Video download to, default is High Quality(2)', action='store', default=2)
        parser.add_argument(
            '-P', '--page', help='Direct page go, default is page 1', action='store', type=int, default=1)
        parser.add_argument(
            '-n', '--number', help='Number for download | all = for download all', action='store', nargs='*')
        if len(sys.argv) == 1:
            parser.print_help()
        elif print_help:
            parser.print_help()
        elif sys.argv[1] == '-v':
            print "version:", self.getVersion()
        else:
            args = parser.parse_args()
            self.run(args.SEARCH, args.page, int(
                args.quality), args.path, args.version)

if __name__ == '__main__':
    c = youtube()
    # c.search(sys.argv[1])
    # c.run(sys.argv[1])
    c.usage()

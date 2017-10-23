#!/usr/bin/python

def shorted(url):
    import requests
    #http://link.safelinkconverter.com/apishorten.php?user=48234&type=cpm&url=https://my.pcloud.com/publink/show?code=XZ2qTAZO8XHCOpJTd4oFllJ3cNi1VK2msqV
    return requests.get('http://link.safelinkconverter.com/apishorten.php?user=48234&type=cpm&url={0}'.format(url)).content

if __name__ == '__main__':
    import sys
    import os
    if len(sys.argv) == 1:
        print "Usage: " + os.path.basename(__file__) + ' [URL]'
    else:
        link = shorted(sys.argv[1])
        import clipboard
        clipboard.copy(link)
        print "link =", unicode(link).encode('utf8')
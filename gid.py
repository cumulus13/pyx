import os
import sys
import time
from urllib import FancyURLopener
import urllib2
import simplejson

def search(text, limit):
    if text == None:
        print "Insert search text !!"
        sys.exit(0)
    # Define search term
    searchTerm = text

    # Replace spaces ' ' in search term for '%20' in order to comply with request
    searchTerm = searchTerm.replace(' ', '%20')


    # Start FancyURLopener with defined version
    class MyOpener(FancyURLopener):
        version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
    myopener = MyOpener()

    # Set count to 0
    count = 0

    for i in range(0, 20):
        print "I =", i
        # Notice that the start changes for each iteration in order to request a
        # new set of images for each loop
        url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
               'v=1.0&q='+searchTerm+'&start='+str(i*4)+'&userip=MyIP')
        print url
        request = urllib2.Request(url, None, {'Referer': 'testing'})
        response = urllib2.urlopen(request)

        # Get results using JSON
        results = simplejson.load(response)
        data = results['responseData']
        dataInfo = data['results']

        # Iterate for each result and get unescaped url
        for myUrl in dataInfo:
            count = count + 1
            print myUrl['unescapedUrl']
            if not os.path.exists(os.path.join(os.getcwd(), 'images')):
                os.makedirs(os.path.join(os.getcwd(), 'images'))
            try:
                myopener.retrieve(myUrl['unescapedUrl'], os.path.join('images', str(count)+'.jpg'))
            except:
                pass
            if count == 20:
                break
        # Sleep for one second to prevent IP blocking from Google
        time.sleep(1)
        if i == limit:
          sys.exit(0)

def usage():
    import argparse
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('SEARCH', help='Search String image', action='store')
    parser.add_argument('-l', '--limit', help='Limit', action='store', type=int, default=5)
    
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        options = parser.parse_args()
        search(options.SEARCH, options.limit)

if __name__ == '__main__':
    usage()
        
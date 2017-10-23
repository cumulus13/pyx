import mutagen
import sys

def tag(music_file):
    from mutagen.easyid3 import EasyID3
    a = EasyID3(music_file)
    #print "a =", a
    #for i in a:
    #    if i == 'APIC:':
    #        pass
    #    else:
    #        print str(i).upper(), "=", a.get(i)[0]
    print "ARTIST  =", a.get('artist')[0]
    print "TITLE   =", a.get('title')[0]
    print "ALBUM   =", a.get('album')[0]
    print "YEAR    =", a.get('date')[0]
    print "TRACK   =", a.get('tracknumber')[0]
    print "GENRE   =", a.get('genre')[0]
             
if __name__ == '__main__':
	tag(sys.argv[1])
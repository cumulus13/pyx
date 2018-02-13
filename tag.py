import sys
import os
import traceback
#def excepthook(etype, value, tb):
    #traceback.format_exc(etype = etype, value = value, tb = tb)

#sys.excepthook = excepthook
import tracert
import datetime
import math
import mutagen
from mutagen import id3
from mutagen.id3 import TOPE, WXXX, TDRC, TPE4, TPE3, TPE2, TPE1, TALB, TKEY, TCOP, USLT, TRCK, TIT3, TIT2, TSRC, TCON, TCOM, COMM, TPUB, TPOS, TBPM, TIT1, TENC, APIC
try:
    from tinytag import TinyTag
except:
    sys.exit('PLEASE INSTALL "mutagen" or "tinytag" before ! :)')
import argparse
from make_colors import make_colors
import debug as debugger
debugger.DEBUG = os.getenv('DEBUG')
debug = debugger.debug
#debug(DEBUG = debugger.DEBUG)
import textwrap as _textwrap
max_file_length = 50
debugger.FILENAME = os.path.abspath(__file__)
#print "debugger.FILENAME =", debugger.FILENAME
#if os.getenv('TRACEBACK_DEBUG_SERVER') == '1' or os.getenv('TRACEBACK_DEBUG_SERVER') == 'True' or os.getenv('TRACEBACK_DEBUG_SERVER') == True or os.getenv('TRACEBACK_DEBUG_SERVER') == 1:
    #TRACEBACK_DEBUG_SERVER = True
TAGGER = {
    'original_artist': TOPE, 
    'original artist': TOPE, 
    'originalartist': TOPE, 
    'url': WXXX, 
    'year': TDRC, 
    'remixed': TPE4, 
    'conductor': TPE3, 
    'album_artist': TPE2, 
    'album artist': TPE2, 
    'albumartist': TPE2, 
    'artist': TPE1, 
    'album': TALB, 
    'key': TKEY, 
    'copyright': TCOP, 
    'lyric': USLT, 
    'track': TRCK, 
    'subtitle': TIT3, 
    'title': TIT2, 
    'isrc': TSRC, 
    'genre': TCON, 
    'composer': TCOM, 
    'comment': COMM, 
    'publisher': TPUB, 
    'disc': TPOS, 
    'bpm': TBPM, 
    'group': TIT1, 
    'encoded': TENC, 
    'image': APIC,
    'cover': APIC,
    'picture': APIC,
}

k = mutagen.id3.PictureType()
instance_pictype = dir(mutagen.id3.PictureType)[0:21]
COVER_TYPE = {}
for i in instance_pictype:
    COVER_TYPE.update({
            str(i).lower(): k.__getattribute__(str(i).upper())
        })
debug(COVER_TYPE = COVER_TYPE)

class SmartFormatter(argparse.HelpFormatter):

    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)


class MultilineFormatter(argparse.HelpFormatter):
    def _fill_text(self, text, width, indent):
        text = self._whitespace_matcher.sub(' ', text).strip()
        paragraphs = text.split('|n ')
        multiline_text = ''
        for paragraph in paragraphs:
            formatted_paragraph = _textwrap.fill(paragraph, width, initial_indent=indent, subsequent_indent=indent) + '\n\n'
            multiline_text = multiline_text + formatted_paragraph
        return multiline_text

class DefaultListAction(argparse.Action):
    CHOICES = ['a', 'l', 'L', 'g', 't', 'b', 'f', 'e', 'd', 'y', \
                   'artists', 'albums', 'album-artists', 'genres', \
                    'lengths', 'bitrates', 'filsizes', 'tracks', 'discs', 'years']
    def __call__(self, parser, namespace, values, option_string=None):
        if values:
            for value in values:
                if value not in self.CHOICES:
                    message = ("invalid choice: {0!r} (choose from {1})"
                                                   .format(value,
                                                           ', '.join([repr(action)
                                                                                                   for action in self.CHOICES])))

                    raise argparse.ArgumentError(self, message)
            setattr(namespace, self.dest, values)


class tag(object):
    def __init__(self):
        super(tag, self)
        self.check_same = {}
        self.dict_tags = {}
        self.list_cover_n = [0]
        self.has_check_same = 0		

    def tag(self, music_file):
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

    def getTag(self, music_file):
        from mutagen.mp3 import MP3
        from mutagen.id3 import ID3
        from mutagen.easyid3 import EasyID3
        a = MP3(music_file)
        #print "aaaaaaaaa =", a
        b = EasyID3(music_file)
        c = ID3(music_file)
        #~ for i in a:
            #~ if i == 'APIC:':
                #~ pass
            #~ else:
                #~ print i, "=", a.get(i)

        return a.info.length, b, a, c

    def getCover(self, music_file, imgstring = ''):
        from mutagen.mp3 import MP3
        x = MP3(music_file)
        ext = ''
        if len(x.keys()) > 0:
            length, tag, mp3tag, id3tag = self.getTag(music_file)
            #print "tag 0 =", tag
        else:
            length = x.info.length
            tag = None
            mp3tag = None
            id3tag = None
        if imgstring:
            ext = ".jpg"
            with open(os.path.join(os.getenv('TMP'), os.path.splitext(os.path.basename(music_file))[0] + ext), 'wb') as imgdata:
                imgdata.write(imgstring.data)
                imgdata.close()
                coverart = os.path.join(os.getenv('TMP'), os.path.splitext(os.path.basename(music_file))[0] + ext)
                return coverart
        else:
            if id3tag and id3tag.get(u'APIC:'):
                imgstring = id3tag.get(u'APIC:')
                #print imgstring.mime
                if 'jpeg' in imgstring.mime:
                    ext = ".jpg"
                elif 'png' in imgstring.mime:
                    ext = ".png"
            if ext and imgstring:
                with open(os.path.join(os.getenv('TMP'), os.path.splitext(os.path.basename(music_file))[0] + ext), 'wb') as imgdata:
                    imgdata.write(imgstring.data)
                    imgdata.close()
                coverart = os.path.join(os.getenv('TMP'), os.path.splitext(os.path.basename(music_file))[0] + ext)
                return coverart
        return False

    def guess_images_mime(self, image_file):
        import mimetypes
        mime = mimetypes.guess_type(image_file)
        if mime[0]:
            if len(mimetypes.guess_all_extensions(mime[0])) > 1:
                return mime[0], mimetypes.guess_all_extensions(mime[0])[1]
            else:
                return mime[0], mimetypes.guess_all_extensions(mime[0])[0]
        else:
            return mime

    def setCover(self, image_file, music_file, cover = 'front', desc = None):
        if not desc:
            desc = cover.title()
        if os.path.isfile(image_file):
            mime, ext = self.guess_images_mime(image_file)
            if mime:
                try:
                    from PIL import Image
                    Image.open(image_file).save(os.path.join(os.getenv('TMP'), 'cover.jpg'))
                    image_file = os.path.join(os.getenv('TMP'), 'cover.jpg')
                    #imgstr = open(image_file, 'rb').read()
                except:
                    pass
            else:
                imgstr = open(image_file, 'rb').read()
                img = APIC(id3.Encoding.LATIN1, unicode(mime), COVER_TYPE.get(cover), desc, imgstr)
                a = id3.ID3(music_file)
                a.update({'APIC:'})
                a.save()

        elif not os.path.isfile(image_file) and isinstance(image_file, str) or not os.path.isfile(image_file) and isinstance(img_string, unicode):
            img = APIC(id3.Encoding.LATIN1, unicode(mime), COVER_TYPE.get(cover), desc, image_file)
            a = id3.ID3(music_file)
            a.update({'APIC:'})
            a.save()

    def preCover(self, image_file, cover = 'cover_front', desc = None):
        debug(cover = cover)
        debug(COVER_TYPE_get_cover = COVER_TYPE.get(cover))
        debug(image_file = image_file)
        
        if not desc:
            desc = cover.title()
        if os.path.isfile(image_file):
            mime, ext = self.guess_images_mime(image_file)
            debug(mime = mime)
            debug(ext = ext)
            if mime:
                try:
                    from PIL import Image
                    Image.open(image_file).save(os.path.join(os.getenv('TMP'), 'cover.jpg'))
                    image_file = os.path.join(os.getenv('TMP'), 'cover.jpg')
                    debug(image_file = image_file)
                    #imgstr = open(image_file, 'rb').read()
                except:
                    pass
                imgstr = open(image_file, 'rb').read()
                img = APIC(id3.Encoding.LATIN1, unicode(mime), COVER_TYPE.get(cover), desc, imgstr)
                return img				
            else:
                imgstr = open(image_file, 'rb').read()
                img = APIC(id3.Encoding.LATIN1, unicode(mime), COVER_TYPE.get(cover), desc, imgstr)
                return img

        elif not os.path.isfile(image_file) and isinstance(image_file, str) or not os.path.isfile(image_file) and isinstance(img_string, unicode):
            img = APIC(id3.Encoding.LATIN1, unicode(mime), COVER_TYPE.get(cover), desc, image_file)
            return img
        return APIC(id3.Encoding.LATIN1, unicode(mime), COVER_TYPE.get(cover), u'', '')

    def run_check_same(self, filename, data, dtag, show_different_only = False, length_separate = 15):
        #debug(filename = filename)
        #debug(data = data)
        #debug(dtag = dtag)
        #debug(show_different_only = show_different_only)
        if not self.check_same.get(filename):
            self.check_same.update({filename:{}})
        #debug(check_same = self.check_same)
        check_data = 0

        if show_different_only == True:
            for i in self.check_same:
                if self.check_same.get(i).get(dtag) == data:
                    if data == 'None':
                        data = u''
                    self.check_same.get(filename).update({dtag: u'',})
                    #print "%s" % dtag.title() + " " * (length_separate - len(dtag)) + ":"        # print dtype
                    return data
                else:
                    #self.check_same.get(filename).update({dtag: data,})
                    check_data = 1
            #debug(check_data = check_data)
            if check_data == 1:  #not same or not found
                self.check_same.get(filename).update({dtag: data,})
                #print "tag        :", dtag
                #print "data       :", data
                #print "type(data) :", type(data)
                if not data == "None":
                    print "%s" % dtag.title() + " " * (length_separate - len(dtag)) + ":", data        # print dtype
                return data
        else:
            if data == 'None':
                data = u''
            print "%s" % dtag.title() + " " * (length_separate - len(dtag)) + ":", data        # print dtype
            return data

    def check_none(self, data):
        if data == None:
            return u''
        if data == "None":
            return u''
        else:
            return data

    def get_tag(self, music_file, print_tag = False, show_full_path = True, max_file_length = 50, numbers_separators = 15, images = False, show_different_only = False):
        coverart = ''
        imgstring = ''
        ext = '.jpg'
        comment = ''

        try:
            tag = TinyTag.get(unicode(music_file).decode('UTF-8'), image= True)
            tag_length, tag_easyid3, tag_mp3, tag_id3 = self.getTag(music_file)
            if tag_id3.get('COMM::eng'):
                comment = " ".join(tag_id3.get('COMM::eng').text)
            if len(comment) > max_file_length + 20:
                comment = _textwrap.wrap(comment, int(max_file_length + 20))
                if len(comment) > 1:
                    comment1 = [comment[0]]
                    for c in comment[1:]:
                        comment1.append(" " * numbers_separators + c)
                    comment = "\n".join(comment1)					
            file_music = music_file
            #tag = TinyTag.get(glob.glob(music_file)[0], image= True)
            #file_music = [unicode(x, fse) for x in glob.glob(music_file)][0]
            #tag = TinyTag.get(glob.glob(file_music)[0], image= True)
            #imgstring = tag.get_image()
            if images:				
                coverart = self.getCover(file_music)
                if not coverart:
                    imgstring = tag.get_image()

                    try:
                        if imgstring:
                            with open(os.path.join(os.getenv('TMP'), os.path.splitext(os.path.basename(file_music))[0] + ext), 'wb') as imgdata:
                                imgdata.write(imgstring.data)
                                imgdata.close()
                            coverart = os.path.join(os.getenv('TMP'), os.path.splitext(os.path.basename(file_music))[0] + ext)
                            #print "coverart 1 =", coverart
                            if not os.path.isfile(coverart):
                                coverart = r'F:\ICONS\Phuzion_Icon_Pack\PNG\Devices\Headphones2.png'
                        else:
                            #print "not ext"
                            coverart = r'F:\ICONS\Phuzion_Icon_Pack\PNG\Devices\Headphones2.png'
                    except:
                        coverart = r'F:\ICONS\Phuzion_Icon_Pack\PNG\Devices\Headphones2.png'
            if show_full_path:
                music_file = make_colors(os.path.dirname(music_file), 'magenta') + '\\' + make_colors(os.path.basename(music_file), 'green')
            else:
                music_file = make_colors(os.path.basename(music_file), 'blue')
            if print_tag:
                if not show_different_only:
                    print "\n"
                print '"%s"' % music_file
                #print "Title          :", unicode(str(tag.track)).encode('UTF-8') + "/" + unicode(tag.disc).encode('UTF-8') + "/" + unicode(tag.disc_total).encode('UTF-8') + ". " + unicode(tag.title).encode('UTF-8')         									   # title of the song
                print "Title          :", unicode(tag.title).encode('UTF-8')         									   # title of the song
                #print "TAG =", tag
                if show_different_only:
                    self.run_check_same(music_file, unicode(tag.artist).encode('UTF-8'), 'artist', show_different_only)
                    self.run_check_same(music_file, unicode(tag.album).encode('UTF-8'), 'album', show_different_only)
                    self.run_check_same(music_file, unicode(tag.albumartist).encode('UTF-8'), 'album artist', show_different_only)
                    self.run_check_same(music_file, unicode(tag.disc).encode('UTF-8'), 'disc', show_different_only)
                    self.run_check_same(music_file, unicode(tag.disc_total).encode('UTF-8'), 'total disc', show_different_only)
                    self.run_check_same(music_file, unicode(tag.genre).encode('UTF-8'), 'genre', show_different_only)
                    self.run_check_same(music_file, str(datetime.timedelta(seconds = float(tag.duration))), 'duration', show_different_only)
                    self.run_check_same(music_file, unicode(tag.bitrate).encode('UTF-8'), 'bitrate', show_different_only)
                    self.run_check_same(music_file, unicode(tag.filesize).encode('UTF-8'), 'filesize', show_different_only)
                    self.run_check_same(music_file, unicode(tag.track).encode('UTF-8'), 'track', show_different_only)
                    self.run_check_same(music_file, unicode(tag.track_total).encode('UTF-8'), 'track total', show_different_only)
                    self.run_check_same(music_file, unicode(str(tag.year)).encode('UTF-8'), 'year', show_different_only)
                    self.run_check_same(music_file, unicode(comment).encode('UTF-8'), 'comment', show_different_only)
                    self.run_check_same(music_file, unicode(tag.audio_offset).encode('UTF-8'), 'audio offset', show_different_only)
                    self.run_check_same(music_file, unicode(tag.samplerate).encode('UTF-8'), 'sample rate', show_different_only)
                    self.run_check_same(music_file, self.check_none(tag_id3.get(TAGGER.get('original_artist').__name__)), 'original artist', show_different_only)
                    self.run_check_same(music_file, self.check_none(tag_id3.get(TAGGER.get('composer').__name__)), 'composer', show_different_only)
                    self.run_check_same(music_file, self.check_none(tag_id3.get(TAGGER.get('remixed').__name__)), 'remixed', show_different_only)
                    self.run_check_same(music_file, self.check_none(tag_id3.get(TAGGER.get('conductor').__name__)), 'conductor', show_different_only)
                    self.run_check_same(music_file, self.check_none(tag_id3.get(TAGGER.get('bpm').__name__)), 'bpm', show_different_only)
                    self.run_check_same(music_file, self.check_none(tag_id3.get(TAGGER.get('group').__name__)), 'group', show_different_only)
                    self.run_check_same(music_file, self.check_none(tag_id3.get(TAGGER.get('subtitle').__name__)), 'subtitle', show_different_only)
                    self.run_check_same(music_file, self.check_none(tag_id3.get(TAGGER.get('isrc').__name__)), 'isrc', show_different_only)
                    self.run_check_same(music_file, self.check_none(tag_id3.get(TAGGER.get('publisher').__name__)), 'publisher', show_different_only)
                    self.run_check_same(music_file, self.check_none(tag_id3.get(TAGGER.get('copyright').__name__)), 'copyright', show_different_only)
                    self.run_check_same(music_file, self.check_none(tag_id3.get(TAGGER.get('url').__name__)), 'url', show_different_only)
                    self.run_check_same(music_file, self.check_none(tag_id3.get(TAGGER.get('encoded').__name__)), 'encoded by', show_different_only)
                else:
                    print "Artist         :", unicode(tag.artist).encode('UTF-8')        # artist name as string
                    print "Album          :", unicode(tag.album).encode('UTF-8')         # album as string
                    print "Album Artist   :", unicode(tag.albumartist).encode('UTF-8')   # album artist as string
                    print "Disc           :", unicode(tag.disc).encode('UTF-8')          # disc number
                    print "Total Disc     :", unicode(tag.disc_total).encode('UTF-8')    # the total number of discs
                    print "Genre          :", unicode(tag.genre).encode('UTF-8')         # genre as string
                    #print "Duration     :", unicode(tag.duration).encode('UTF-8')      # duration of the song in seconds
                    print "Duration       :", str(datetime.timedelta(seconds = float(tag.duration)))      # duration of the song in seconds					
                    print "Bitrate        :", unicode(tag.bitrate).encode('UTF-8')       # bitrate in kBits/s
                    print "Filesize       :", unicode(tag.filesize).encode('UTF-8')      # file size in bytes
                    print "Track          :", unicode(tag.track).encode('UTF-8')         # track number as string
                    print "Track Total    :", unicode(tag.track_total).encode('UTF-8')   # total number of tracks as string
                    print "Year           :", unicode(tag.year).encode('UTF-8')          # year or data as string
                    print "Comment        :", unicode(comment)                           # comment or data as string
                    print "Audio Offset   :", unicode(tag.audio_offset).encode('UTF-8')  # number of bytes before audio data begins
                    print "Sample Rate    :", unicode(tag.samplerate).encode('UTF-8')    # samples per second
                    print "Orignal Artist :", self.check_none(tag_id3.get(TAGGER.get('original_artist').__name__))
                    print "Composer       :", self.check_none(tag_id3.get(TAGGER.get('composer').__name__))
                    print "Remixed        :", self.check_none(tag_id3.get(TAGGER.get('remixed').__name__))
                    print "Conductor      :", self.check_none(tag_id3.get(TAGGER.get('conductor').__name__))
                    print "BPM            :", self.check_none(tag_id3.get(TAGGER.get('bpm').__name__))
                    print "Grouping       :", self.check_none(tag_id3.get(TAGGER.get('group').__name__))
                    print "Subtitle       :", self.check_none(tag_id3.get(TAGGER.get('subtitle').__name__))
                    print "ISRC           :", self.check_none(tag_id3.get(TAGGER.get('isrc').__name__))
                    print "Publisher      :", self.check_none(tag_id3.get(TAGGER.get('publisher').__name__))
                    print "Copyright      :", self.check_none(tag_id3.get(TAGGER.get('copyright').__name__))
                    print "URL            :", self.check_none(tag_id3.get(TAGGER.get('url').__name__))
                    print "Encoded by     :", self.check_none(tag_id3.get(TAGGER.get('encoded').__name__))
                    picture = "NO"
                    if tag_id3.getall('APIC'):
                        picture = "YES"
                    print "Cover          :", picture

            data_tags = {
                'track': unicode(str(tag.track)).encode('UTF-8'),
                'title': unicode(tag.title).encode('UTF-8'),        									   # title of the song
                'tracks': unicode(str(tag.track)).encode('UTF-8') + "/" + unicode(tag.track_total).encode('UTF-8'),
                'disc': unicode(tag.disc).encode('UTF-8'),          # disc number,
                'discs': unicode(tag.disc).encode('UTF-8') + "/" + unicode(tag.disc_total).encode('UTF-8'),
                'artist': unicode(tag.artist).encode('UTF-8'),        # artist name as string
                'album': unicode(tag.album).encode('UTF-8'),         # album as string
                'album_artist': unicode(tag.albumartist).encode('UTF-8'),   # album artist as string
                'total_disc': unicode(tag.disc_total).encode('UTF-8'),    # the total number of discs
                'total disc': unicode(tag.disc_total).encode('UTF-8'),    # the total number of discs
                'disc total': unicode(tag.disc_total).encode('UTF-8'),    # the total number of discs
                'disc_total': unicode(tag.disc_total).encode('UTF-8'),    # the total number of discs
                'genre': unicode(tag.genre).encode('UTF-8'),         # genre as string
                'duration': str(datetime.timedelta(seconds = float(tag.duration))),      # duration of the song in seconds
                'audio_offset': unicode(tag.audio_offset).encode('UTF-8'),  # number of bytes before audio data begins
                'audio offset': unicode(tag.audio_offset).encode('UTF-8'),  # number of bytes before audio data begins
                'encode': unicode(tag.bitrate).encode('UTF-8'),       # bitrate in kBits/s
                'filesize': unicode(tag.filesize).encode('UTF-8'),      # file size in bytes
                'samplerate': unicode(tag.samplerate).encode('UTF-8'),    # samples per second
                'total_track': unicode(tag.track_total).encode('UTF-8'),   # total number of tracks as string
                'total track': unicode(tag.track_total).encode('UTF-8'),   # total number of tracks as string
                'track total': unicode(tag.track_total).encode('UTF-8'),   # total number of tracks as string
                'track_total': unicode(tag.track_total).encode('UTF-8'),   # total number of tracks as string
                'year': unicode(tag.year).encode('UTF-8'),          # year or data as string
                'comment': unicode(comment).encode('UTF-8'),           # comment or data as string
                'original_artist': self.check_none(tag_id3.get(TAGGER.get('original_artist').__name__)),
                'original artist': self.check_none(tag_id3.get(TAGGER.get('original_artist').__name__)),
                'composer': self.check_none(tag_id3.get(TAGGER.get('composer').__name__)),
                'remixed': self.check_none(tag_id3.get(TAGGER.get('remixed').__name__)),
                'conductor': self.check_none(tag_id3.get(TAGGER.get('conductor').__name__)),
                'bpm': self.check_none(tag_id3.get(TAGGER.get('bpm').__name__)),
                'group': self.check_none(tag_id3.get(TAGGER.get('group').__name__)),
                'subtitle': self.check_none(tag_id3.get(TAGGER.get('subtitle').__name__)),
                'isrc': self.check_none(tag_id3.get(TAGGER.get('isrc').__name__)),
                'publisher': self.check_none(tag_id3.get(TAGGER.get('publisher').__name__)),
                'copyright': self.check_none(tag_id3.get(TAGGER.get('copyright').__name__)),
                'url': self.check_none(tag_id3.get(TAGGER.get('url').__name__)),
                'encoded': self.check_none(tag_id3.get(TAGGER.get('encoded').__name__)),
            }
            debug(data_tags = data_tags)
            return tag, coverart, data_tags
        except:
            if debugger.DEBUG:
                traceback.format_exc()
            traceback.format_exc(print_msg= False)
            return False, False, False

    def show_tags(self, music_file, max_file_length, artist = False, album = False, album_artist = False, genre = False, length = False, bitrate = False, filesize = False, track = False, year = False, disc = False, comment = False, show_all = False, show_full_path = True, print_info = True, show_different_only = False):
        if comment:
            numbers_separators = 54
        else:
            numbers_separators = 15
        tags, coverart, data_tags = self.get_tag(music_file, show_all, show_full_path, max_file_length, numbers_separators, False, show_different_only)
        debug(music_file = music_file)
        debug(data_tags = data_tags)
        if print_info:
            if show_full_path:
                music_file = os.path.dirname(music_file) + "\\" + make_colors(os.path.basename(music_file), 'green')
            else:
                music_file = os.path.basename(music_file)
            if not show_all:
                print '"' + make_colors(music_file, "blue") + '"'
        if print_info:
            if artist:
                print make_colors("Artist      ", 'white') + " = " + make_colors(data_tags[1], 'yellow')
            if album:
                print make_colors("Album       ", 'white') + " = " + make_colors(data_tags[2], 'magenta')
            if album_artist:
                print make_colors("Album Artist", 'white') + " = " + make_colors(data_tags[3], 'green')
            if disc:
                print make_colors("Disc        ", 'white') + " = " + make_colors(str(data_tags[4]) + "/" + str(data_tags[5]), 'blue')
            if genre:
                print make_colors("Genre       ", 'white') + " = " + make_colors(data_tags[6], 'cyan')
            if length:
                print make_colors("Length      ", 'white') + " = " + make_colors(str(data_tags[7]) + " ~ " + str(data_tags[11]), 'blue') + " ~ " + make_colors(str(data_tags[8]))
            if bitrate:
                print make_colors("Bitrate     ", 'white') + " = " + make_colors(str(data_tags[9]) + " kbps", 'blue')
            if filesize:
                print make_colors("Filesize    ", 'white') + " = " + make_colors(data_tags[10], 'yellow')
            if track:
                print make_colors("Track       ", 'white') + " = " + make_colors(str(data_tags[13]) + "/" + str(data_tags[13]), 'magenta')
            if year:
                print make_colors("Year        ", 'white') + " = " + make_colors(str(data_tags[14]), 'white')
            if comment:
                print make_colors("Comment     ", 'white') + " = " + make_colors(str(data_tags[15]), 'cyan')

            print make_colors("-" * max_file_length, 'red')
        return tags, coverart, data_tags

    def tagging(self, music_file, args_tag, tag_instance, total_tag = u'', encoding = id3.Encoding.UTF16, cover = 'front', cover_desc = u'', cover_image_file = '', dont_save = False):
        debug(tag_instance_0 = tag_instance)
        debug(music_file_0 = music_file)
        debug(encoding_0 = encoding)
        tag_instance1 = TAGGER.get(tag_instance)
        '''
			it accept one list value first and two or more than values of list data
			example: self.tagging(music_file, args.track, 'track', args.total_track, 'track')
		'''
        tags = ''
        if args_tag == None:
            args_tag = []
        if not isinstance(music_file, list) and os.path.isfile(music_file):
            debug(tagging = "process 001")
            if not self.dict_tags.get(os.path.basename(music_file)):
                debug(check_self_dict_tags = "make")
                self.dict_tags.update({os.path.basename(music_file): {'fullpath': music_file,},})
            if not self.dict_tags.get(os.path.basename(music_file)).get(tag_instance):
                debug(check_self_dict_tags_tag_intance = "make")
                self.dict_tags.get(os.path.basename(music_file)).update({tag_instance: [],})
                debug(dict_tags_make = self.dict_tags)
            if args_tag == None:
                args_tag = []

            tag_length, tag_easyid3, tag_mp3, tag_id3 = self.getTag(music_file)
            
            if tag_instance == 'image' or tag_instance == 'picture' or tag_instance == 'cover':
                try:
                    img_apic = self.preCover(cover_image_file, cover, cover_desc)
                    if not self.dict_tags.get(os.path.basename(music_file)):
                        self.dict_tags.update({os.path.basename(music_file): {max(self.list_cover_n) + 1: {'fullpath': music_file,},},})
                    if dont_save:
                        self.dict_tags.get(os.path.basename(music_file)).get(max(self.dict_tags.get(os.path.basename(music_file)).keys())).update({tag_instance: [img_apic],})
                    else:
                        tag_id3.update({'APIC:': img_apic})
                        tag_id3.save()
                except:
                    if debugger.DEBUG:
                        traceback.format_exc()
                    else:
                        traceback.format_exc(print_msg= False)
                        
            elif tag_instance == 'url':
                print "is URL"
                try:
                    url = tag_instance1(encoding, desc = 'Official Decode', url = args_tag)
                    if not self.dict_tags.get(os.path.basename(music_file)):
                        self.dict_tags.update({os.path.basename(music_file): {max(self.list_cover_n) + 1: {'fullpath': music_file,},},})

                    if dont_save:
                        self.dict_tags.get(os.path.basename(music_file)).update({tag_instance: [url],})
                    else:
                        tag_id3.setall(tag_instance1.__name__, [url])
                        tag_id3.save()
                except:
                    if debugger.DEBUG:
                        traceback.format_exc()
                    else:
                        traceback.format_exc(print_msg= False)
                        
            elif args_tag == 'remove' or tag_instance == 'remove':
                try:
                    args_tag = ''
                    tags = tag_instance1(encoding, text = [args_tag])
                    if dont_save:
                        self.dict_tags.get(os.path.basename(music_file)).update({tag_instance: [tags],})
                    else:
                        tag_id3.setall(tag_instance1.__name__, [tags])
                        tag_id3.save()
                except:
                    try:
                        args_tag = ''
                        tags = tag_instance1(encoding, text = args_tag)
                        if dont_save:
                            self.dict_tags.get(os.path.basename(music_file)).update({tag_instance: [tags],})
                        else:
                            tag_id3.setall(tag_instance1.__name__, [tags])
                            tag_id3.save()
                    except:
                        if debugger.DEBUG:
                            traceback.format_exc()
                        else:
                            traceback.format_exc(print_msg= False)
                        
            elif tag_instance == 'tracks' or tag_instance == 'tracks' or tag_instance == 'disc' or tag_instance == 'discs':
                try:
                    #print "tag_instance  =", tag_instance
                    #print "tag_instance1 =", tag_instance1
                    #print "args_tag      =", args_tag
                    #print "total_tag     =", total_tag
                    #print "encoding      =", encoding
                    tags = tag_instance1(encoding, text = [args_tag + "/" + total_tag])
                    if dont_save:
                        self.dict_tags.get(os.path.basename(music_file)).update({tag_instance: [tags],})
                    else:
                        tag_id3.setall(tag_instance1.__name__, [tags])
                        tag_id3.save()
                except:
                    if debugger.DEBUG:
                        traceback.format_exc()
                    else:
                        traceback.format_exc(print_msg= False)
                                    
            elif tag_instance == 'comment' or tag_instance == 'comments':
                try:
                    
                    tags = tag_instance1(encoding = encoding, lang = 'eng', desc = u'', text = [args_tag])
                    if dont_save:
                        self.dict_tags.get(os.path.basename(music_file)).update({tag_instance: [tags],})
                    else:
                        tag_id3.setall(tag_instance1.__name__, [tags])
                        tag_id3.save()
                except:
                    if debugger.DEBUG:
                        traceback.format_exc()
                    else:
                        traceback.format_exc(print_msg= False)
                        
            elif "?" in args_tag:
                self.tagging_sep(music_file, args_tag, tag_instance, total_tag, encoding, cover, cover_desc, dont_save)

            else:
                debug(tag_instance_x = tag_instance)
                try:
                    #if not self.dict_tags.get(os.path.basename(music_file)).get(tag_instance):
                        #self.dict_tags.get(os.path.basename(music_file)).update({tag_instance: [],})
                    debug(tag_instance1 = tag_instance1)
                    debug(args_tag = args_tag)
                    debug(encoding = encoding)
                    tags = tag_instance1(encoding, args_tag)
                    debug(type_tags = type(tags))
                    debug(tags = tags)
                    if dont_save:
                        #self.dict_tags.get(os.path.basename(i)).update({tag_instance1.__name__: [tags],})
                        self.dict_tags.get(os.path.basename(music_file)).update({tag_instance: [tags],})
                        debug(dict_tags = self.dict_tags)
                    else:
                        tag_id3.setall(tag_instance1.__name__, [tags])
                        tag_id3.save()
                except:
                    if debugger.DEBUG:
                        traceback.format_exc()
                    else:
                        traceback.format_exc(print_msg= False)
                        
        else:
            debug(tagging = "process 002 ...")
            self.tagging_multi(music_file, args_tag, tag_instance, total_tag, encoding, cover, cover_desc, cover_image_file, dont_save)
        #print "=" * 200
        #return tags, tag_instance1, tag_instance1.__name__, self.dict_tags
                
    def tagging_sep(self, music_file, args_tag, tag_instance, total_tag = u'', encoding = id3.Encoding.UTF16, cover = 'front', cover_desc = u'', cover_image_file = u'', dont_save = False):
        tag_instance1 = TAGGER.get(tag_instance)
        
        if "?" in args_tag:
            music_file1, args_tags1 = str(args_tag).split('?')
            
            if os.path.isfile(music_file):
                cover_image_file = music_file1
                cover = args_tags1
                if tag_instance == 'image' or tag_instance == 'picture' or tag_instance == 'cover':
                    self.tagging(music_file, args_tag, tag_instance, total_tag, encoding, cover, cover_desc, cover_image_file, dont_save)
                else:
                    self.tagging(music_file, args_tag, tag_instance, total_tag, encoding= encoding, dont_save = dont_save)
                
    def tagging_multi(self, list_file, args_tag, tag_instance, total_tag = u'', encoding = id3.Encoding.UTF16, cover = 'front', cover_desc = u'', cover_image_file = '', dont_save = False):
        tag_instance1 = TAGGER.get(tag_instance)
        '''
			it accept one list value first and two or more than values of list data
			example: self.tagging(list_file, args.track, 'track', args.total_track, 'track')
		'''
        
        ttype_list = ['track', 'disc']
        if len(list_file) > 0:
            if args_tag == None:
                args_tag = []
            for lf in list_file:
                self.dict_tags.update({os.path.basename(lf): {'fullpath': lf,},})

            if len(args_tag) == 1 and isinstance(args_tag, list) and tag_instance in ttype_list or str(args_tag).isdigit() and isinstance(args_tag, list) and tag_instance in ttype_list:
                debug(tagging_multi = "process 001 ...")
                try:
                    if args_tag[0] == 'all' or args_tag[0] == 'a':
                        list_args_tag1 = []
                        for t in range(len(list_file)):
                            list_args_tag1.append(t)
                        for i in list_file:
                            tagged = list_args_tag1[list_file.index(i)] + 1
                            debug(tagged0 = tagged)
                            if len(str(tagged)) == 1:
                                tagged = "0" + str(tagged)
                            debug(tagged1 = tagged)
                            if not total_tag:
                                total_tag = str(len(list_file))
                            if len(total_tag) == 1:
                                total_tag = "0" + total_tag
                            
                            self.tagging(i, tagged, tag_instance, total_tag, encoding, cover, cover_desc, cover_image_file, dont_save)
                            
                    elif args_tag[0] == 'remove':
                        args_tag = ['', ]
                        
                        for i in list_file:
                            self.tagging(i, args_tag)
                    else:
                        args_tags = args_tag[0]
                        if len(str(args_tag)) == 1:
                            args_tags = "0" + str(args_tag)

                        if not total_tag:
                            total_tag = str(len(list_file))
                        if len(total_tag) == 1:
                            total_tag = "0" + total_tag

                        for i in list_file:
                            debug(i = i)
                            self.tagging(i, args_tag[0], tag_instance, total_tag, encoding, cover, cover_desc, cover_image_file, dont_save)
                except:
                    if debugger.DEBUG:
                        traceback.format_exc()
                    else:
                        traceback.format_exc(print_msg= False)
                        
            elif len(args_tag) > 1 and isinstance(args_tag, list) and tag_instance in ttype_list or str(args_tag).isdigit() and isinstance(args_tag, list) and tag_instance in ttype_list:
                debug(tagging_multi = "process 002 ...")
                for i in range(len(args_tag)):
                    try:
                        if "?" in args_tag[i]:
                            
                            if len(args_tags1) == 1:
                                args_tags1 = "0" + args_tags1
                            else:
                                args_tags1 = args_tags1
                            total_tag1 = u''
                            if not total_tag:
                                total_tag = str(len(list_file))
                            if len(total_tag) == 1:
                                total_tag = "0" + total_tag
                                
                            self.tagging_sep(i, args_tag1[i], tag_instance, total_tag, encoding, cover, cover_desc, dont_save)
                            
                        else:
                            if len(args_tag[i]) == 1:
                                args_tags1 = "0" + args_tag[i]
                            else:
                                args_tags1 = args_tag[i]

                            if not total_tag:
                                total_tag = str(len(list_file))
                            if len(total_tag) == 1:
                                total_tag = "0" + total_tag                                                        
                            
                            self.tagging(list_file[i], args_tag1, tag_instance, total_tag, encoding, cover, cover_desc, cover_image_file, dont_save)
                            
                    except:
                        if debugger.DEBUG:
                            traceback.format_exc()
                        else:
                            traceback.format_exc(print_msg= False)

            elif isinstance(args_tag, list) and len(args_tag) > 1 and tag_instance not in ttype_list:
                debug(tagging_multi = "process 003 ...")
                for i in range(len(args_tag)):
                    try:
                        if "?" in args_tag[i]:
                            self.tagging_sep(i, args_tag[i], tag_instance, total_tag, encoding, cover, cover_desc, cover_image_file, dont_save)

                        else:
                            debug(list_file = list_file)
                            if os.path.isfile(list_file[i]):
                                self.tagging(list_file[i], args_tag[i], tag_instance, total_tag, encoding, cover, cover_desc, cover_image_file, dont_save)
                    except:
                        if debugger.DEBUG:
                            traceback.format_exc()
                        else:
                            traceback.format_exc(print_msg= False)

            elif len(args_tag) == 1 and isinstance(args_tag, list) and tag_instance not in ttype_list:
                debug(tagging_multi = "process 004 ...")
                for i in list_file:
                    try:
                        if "?" in args_tag[0]:
                            self.tagging_sep(i, args_tag[0], tag_instance, total_tag, encoding, cover, cover_desc, cover_image_file, dont_save)
                        else:
                            debug(list_file = list_file)
                            if os.path.isfile(i):
                                self.tagging(i, args_tag[0], tag_instance, total_tag, encoding, cover, cover_desc, cover_image_file, dont_save)
                    except:
                        if debugger.DEBUG:
                            traceback.format_exc()
                        else:
                            traceback.format_exc(print_msg= False)

            else:
                debug(tagging_multi = "process 005 ...")
                try:
                    for i in list_file:
                        self.tagging(i, args_tag, tag_instance, total_tag, encoding, cover, cover_desc, cover_image_file, dont_save)
                except:
                    if debugger.DEBUG:
                        traceback.format_exc()
                    else:
                        traceback.format_exc(print_msg= False)

    def tagging2(self, list_file, args_tag, tag_instance, total_tag = None, ttype = None, encoding = id3.Encoding.UTF16):
        '''
        	it accept one list value first and two or more than values of list data
        '''
        ttype_list = ['track', 'disc']
        if len(list_file) > 0:
            if len(args_tag) == 1 and isinstance(args_tag, list) and ttype in ttype_list or str(args_tag).isdigit() and isinstance(args_tag, list) and ttype in ttype_list:
                try:
                    if len(args_tag[0]) == 1:
                        args_tags1 = "0" + args_tag[0]
                    else:
                        args_tags1 = args_tag[0]
                    if total_tag:
                        if len(total_tag) == 1:
                            total_tag1 = "0" + total_tag
                    else:
                        total_tag1 = total_tag
                    if args_tag[0] == 'remove':
                        args_tag1 = ''
                        total_tag1 = ''
                    for i in list_file:
                        tag_length, tag_easyid3, tag_mp3, tag_id3 = self.getTag(i)
                        if total_tag:
                            tags = tag_instance(encoding, args_tags1 + "/" + total_tag1)
                        else:
                            tags = tag_instance(encoding, args_tags1)
                        tag_id3.setall(tag_instance.__name__, [tags])
                        tag_id3.save()
                except:
                    if debugger.DEBUG:
                        traceback.format_exc()
                    else:
                        traceback.format_exc(print_msg= False)
            elif len(args_tag) > 1 and isinstance(args_tag, list) and ttype in ttype_list or str(args_tag).isdigit() and isinstance(args_tag, list) and ttype in ttype_list:
                for i in range(len(args_tag)):
                    try:
                        if "?" in args_tag[i]:
                            music_file, args_tags1 = str(args_tag[i]).split('?')
                            if os.path.isfile(music_file):
                                tag_length, tag_easyid3, tag_mp3, tag_id3 = self.getTag(music_file)
                                if len(args_tags1) == 1:
                                    args_tags1 = "0" + args_tags1
                                else:
                                    args_tags1 = args_tags1
                                if total_tag:
                                    if len(total_tag) == 1:
                                        total_tag1 = "0" + total_tag
                                    else:
                                        total_tag1 = total_tag
                                if args_tag1 == 'remove':
                                    args_tag1 = ''
                                    total_tag1 = ''
                                if total_tag:
                                    tags = tag_instance(encoding, args_tags1 + "/" + total_tag1)
                                else:
                                    tags = tag_instance(encoding, args_tags1)
                                tag_id3.setall(tag_instance.__name__, [tags])
                                tag_id3.save()							
                        else:
                            if len(args_tag[i]) == 1:
                                args_tags1 = "0" + args_tag[i]
                            else:
                                args_tags1 = args_tag[i]
                            if total_tag:
                                if len(total_tag) == 1:
                                    total_tag1 = "0" + total_tag
                                else:
                                    total_tag1 = total_tag
                            if os.path.isfile(list_file[i]):
                                tag_length, tag_easyid3, tag_mp3, tag_id3 = self.getTag(list_file[i])
                                if total_tag:
                                    tags = tag_instance(encoding, args_tags1 + "/" + total_tag1)
                                else:
                                    tags = tag_instance(encoding, args_tags1 + "/" + total_tag1)
                                tag_id3.setall(tag_instance.__name__, [tags])
                                tag_id3.save()							
                    except:
                        if debugger.DEBUG:
                            traceback.format_exc()
                        else:
                            traceback.format_exc(print_msg= False)

            elif isinstance(args_tag, list) and ttype not in ttype_list or isinstance(args_tag, list) and ttype not in ttype_list:
                for i in range(len(args_tag)):
                    try:
                        if "?" in args_tag[i]:
                            music_file, args_tags1 = str(args_tag[i]).split('?')
                            if os.path.isfile(music_file):
                                tag_length, tag_easyid3, tag_mp3, tag_id3 = self.getTag(music_file)
                                if args_tag1 == 'remove':
                                    args_tag1 = ''
                                tags = tag_instance(encoding, args_tags1)
                                tag_id3.setall(tag_instance.__name__, [tags])
                                tag_id3.save()							
                        else:
                            if os.path.isfile(list_file[i]):
                                tag_length, tag_easyid3, tag_mp3, tag_id3 = self.getTag(list_file[i])
                                tags = tag_instance(encoding, args_tags1)
                                tag_id3.setall(tag_instance.__name__, [tags])
                                tag_id3.save()							
                    except:
                        if debugger.DEBUG:
                            traceback.format_exc()
                        else:
                            traceback.format_exc(print_msg= False)
            else:
                try:
                    for i in list_file:
                        tag_length, tag_easyid3, tag_mp3, tag_id3 = self.getTag(i)
                        tags = tag_instance(encoding, args_tags)
                        tag_id3.setall(tag_instance.__name__, [tags])
                        tag_id3.save()
                except:
                    if debugger.DEBUG:
                        traceback.format_exc()
                    else:
                        traceback.format_exc(print_msg= False)

    def usage(self):
        parse = argparse.ArgumentParser(version= 'version: 0.1')
        scan_help = '''Get All tags on current or spesific folder
a || artists
l || albums
L || album-artists
g || genres
t || lengths
b || bitrates
f || filesizes
e || tracks
d || discs
y || years
c || comments
i || cover/image/picture
all
		'''
        scan_choices = ['a', 'l', 'L', 'g', 't', 'b', 'f', 'e', 'd', 'y', 'c', \
                                'artists', 'albums', 'album-artists', 'genres', \
                                'lengths', 'bitrates', 'filsizes', 'tracks', 'discs', 'years', 'comments', 'all']
        parse.add_argument('-s', '--scan', action = 'store', help = scan_help, choices = scan_choices, nargs = '*')
        parse.formatter_class = argparse.RawTextHelpFormatter
        parse.add_argument('-p', '--path', action = 'store', help = 'use spesific folder', nargs = '*', default = [os.getcwd()])
        parse.add_argument('-r', '--recursive', action = 'store_true', help = 'Scan subdirectory Recursive')
        parse.add_argument('--all', action = 'store_true', help = 'Get All tag on current or spesific folder')
        parse.add_argument('-F', '--fast', action = 'store_true', help = 'Fast scan')
        parse.add_argument('-f', '--show-full-path', action = 'store_true', help = 'Show full path of file')
        usage_track = "Set track file or all file on current or spesific folder\nexample: * set track only: -t 01\n\t * set track and total: -t 01/01\n\t * set all track: -t all|a"
        parse.add_argument('-t', '--track', action = 'store', help = usage_track, type = unicode, nargs = '*')
        parse.add_argument('-T', '--total-track', action = 'store', help = "Set total track tag or all total track tag on current or spesific folder", type = unicode, default = u'')
        parse.add_argument('-d', '--disc', action = 'store', help = "Set disc track tag or all disc track tag on current or spesific folder", type = unicode, nargs = '*', default = [u'01'])
        parse.add_argument('-D', '--total-disc', action = 'store', help = "Set total disc track tag or all total disc track tag on current or spesific folder", type = unicode, default = u'01')
        parse.add_argument('-a', '--artist', action = 'store', help = 'Set artist tag or All artist tag on current or spesific folder', type = unicode)
        parse.add_argument('-A', '--album-artist', action = 'store', help = 'Set album artist tag or All album artist tag on current or spesific folder', type = unicode)
        parse.add_argument('-l', '--album', action = 'store', help = 'Set album tag or All album tag on current or spesific folder', type = unicode)
        parse.add_argument('-y', '--year', action = 'store', help = 'Set year tag or All year tag on current or spesific folder', type = unicode)
        parse.add_argument('-g', '--genre', action = 'store', help = 'Set genre tag or All genre tag on current or spesific folder', type = unicode)
        parse.add_argument('-c', '--comment', action = 'store', help = 'Set comment tag or All comment tag on current or spesific folder', type = unicode)
        parse.add_argument('-C', '--composer', action = 'store', help = 'Set composer tag or All composer tag on current or spesific folder', type = unicode)
        parse.add_argument('-o', '--original-artist', action = 'store', help = 'Set original artist tag or All original artist tag on current or spesific folder', type = unicode)
        parse.add_argument('-R', '--remixed', action = 'store', help = 'Set remixed tag or All remixed tag on current or spesific folder', type = unicode)
        parse.add_argument('-n', '--conductor', action = 'store', help = 'Set conductor tag or All conductor tag on current or spesific folder', type = unicode)
        parse.add_argument('-S', '--subtitle', action = 'store', help = 'Set subtitle tag or All subtitle tag on current or spesific folder', type = unicode)
        parse.add_argument('-i', '--isrc', action = 'store', help = 'Set subtitle ISRC tag or All ISRC tag on current or spesific folder', type = unicode)
        parse.add_argument('-P', '--publisher', action = 'store', help = 'Set publisher tag or All publisher tag on current or spesific folder', type = unicode)
        parse.add_argument('-O', '--copyright', action = 'store', help = 'Set copyright tag or All copyright tag on current or spesific folder', type = unicode)
        parse.add_argument('-u', '--url', action = 'store', help = 'Set url tag or All url tag on current or spesific folder', type = unicode)
        parse.add_argument('-e', '--encoded', action = 'store', help = 'Set encoded tag or All encoded tag on current or spesific folder', type = unicode)
        parse.add_argument('-m', '--image', action = 'store', help = 'Set image tag or All image tag on current or spesific folder', type = unicode, nargs = '*')
        parse.add_argument('-Y', '--lyric', action = 'store', help = 'Set lyric tag or All lyric tag on current or spesific folder', type = file)
        parse.add_argument('-b', '--show-different-only', action = 'store_true', help = 'Show ALl tag on current or spesific folder which not same with other files')
        #parse.add_argument('-cc', '--picture', action = 'store', help = 'file path picture of cover or image')
        parse.add_argument('-ct', '--cover', action = 'store', help = 'Type of Cover Image', choices = COVER_TYPE.keys(), default = 'cover_front')
        parse.add_argument('-cd', '--cover-description', action = 'store', help = 'Description of Cover Image', default = u'')
        parse.add_argument('-cl', '--list-cover', action = 'store_true', help = 'Get List Type of Cover Image')
        parse.add_argument('--licface', action = 'store_true', help = 'for LICFACE Only')

        if len(sys.argv) == 1:
            parse.print_help()
        else:
            args = parse.parse_args()
            #print "ARGS =", args
            debug(args = args)

            exts = [".mp3", ".wav", ".mp4", ".m4a"]
            list_max_length = []

            if args.path:
                path = args.path
            else:
                path = os.getcwdu()
            list_file = []
            max_length = 50
            if args.path:
                for p in path:
                    if os.path.isdir(p):
                        if args.fast:
                            if args.recursive:
                                #if " " in path:
                                    #list_dist1 = os.popen('dir /s /b %s' % path)
                                #else:
                                list_dist = os.popen('dir /s /b "%s"' % p)
                            else:
                                list_dist = os.listdir(p)
                            for d in list_dist:
                                for e in exts:
                                    if str(d).endswith(e):
                                        list_file.append(os.path.abspath(d))
                        else:
                            if args.recursive:
                                for root, dirs, files in os.walk(p):
                                    if files:
                                        for i in files:
                                            if len(os.path.splitext(i)) == 2 and os.path.splitext(i)[1] in exts:
                                                list_file.append(os.path.abspath(os.path.join(root, i)))
                            else:
                                list_dist = os.listdir(p)
                                for d in list_dist:
                                    for e in exts:
                                        if str(d).endswith(e):
                                            list_file.append(os.path.abspath(d))								
                    elif os.path.isfile(p):
                        list_file.append(p)

                debug(list_file = list_file)
                for i in list_file:
                    list_max_length.append(len(i))
                debug(list_max_length = list_max_length)
                max_length = max(list_max_length)
                if args.show_full_path:
                    max_length = max(list_max_length) + 9

            if args.list_cover:
                print COVER_TYPE.keys()

            if args.scan and len(list_file) > 0:
                ALLS, ARTISTS, ALBUMS, ALBUM_ARTISTS, GENRES, LENGTHS, BITRATES, FILESIZES, TRACKS, DISCS, YEARS, COMMENTS = False, False, False, False, False, False, False, False, False, False, False, False
                for scan in args.scan:
                    if scan == 'a' or scan == 'artists' or scan == 'artist':
                        ARTISTS = True
                    elif scan == 'l' or scan == 'albums' or scan == 'album':
                        ALBUMS = True
                    elif scan == 'L' or scan == 'album-artists' or scan == 'album-artist':
                        ALBUM_ARTISTS = True
                    elif scan == 'g' or scan == 'genres' or scan == 'genre':
                        GENRES = True
                    elif scan == 't' or scan == 'lengths' or scan == 'length':
                        LENGTHS = True
                    elif scan == 'b' or scan == 'bitrate' or scan == 'bitrates':
                        BITRATES = True
                    elif scan == 'f' or scan == 'filesize' or scan == 'filesizes':
                        FILESIZES = True
                    elif scan == 'e' or scan == 'tracks' or scan == 'track':
                        TRACKS = True
                    elif scan == 'd' or scan == 'discs' or scan == 'disc':
                        DISCS = True
                    elif scan == 'y' or scan == 'years' or scan == 'year':
                        YEARS = True
                    elif scan == 'c' or scan == 'comment' or scan == 'comments':
                        COMMENTS = True
                    elif scan == 'all' or scan == 'alls':
                        ALLS = True

                for i in list_file:
                    self.show_tags(i, max_length, ARTISTS, ALBUMS, ALBUM_ARTISTS, GENRES, LENGTHS, BITRATES, FILESIZES, TRACKS, YEARS, DISCS, COMMENTS, ALLS, args.show_full_path, show_different_only= args.show_different_only)

            if args.track:
                self.tagging(list_file, args.track, 'track', args.total_track)
            if args.total_track:
                self.tagging(list_file, 'all', 'track', args.total_track)
            if args.disc:
                self.tagging(list_file, args.disc, 'disc', args.total_disc)
            if args.total_disc:
                self.tagging(list_file, '01', 'disc', args.total_disc)
            if args.album:
                self.tagging(list_file, args.album, 'album')
            if args.artist:
                self.tagging(list_file, args.artist, 'artist')
            if args.album_artist:
                self.tagging(list_file, args.album_artist, 'album_artist')
            if args.original_artist:
                if args.original_artist == 'artist' and args.artist:
                    self.tagging(list_file, args.artist, 'original_artist')
                else:
                    self.tagging(list_file, args.original_artist, 'original_artist')
            if args.year:
                self.tagging_multi(list_file, args.year, 'year')
            if not args.year:
                for i in list_file:
                    tags, cover, data_tags = self.show_tags(i, max_file_length, print_info= False)
                    debug(data_tags_get_year = data_tags.get('year'))
                    if not data_tags.get('year'):
                        self.tagging(list_file, datetime.datetime.strftime(datetime.datetime.now(), '%Y'), 'year')
            if args.copyright:
                self.tagging(list_file, args.copyright, 'copyright')
            if not args.copyright:
                tags, cover, data_tags = self.show_tags(i, max_file_length, print_info= False)
                debug(data_tags_get_copyright = data_tags.get('year'))
                if not data_tags.get('copyright'):
                    self.tagging(list_file, datetime.datetime.strftime(datetime.datetime.now(), '%Y'), 'copyright')            
            if args.genre:
                self.tagging(list_file, args.genre, 'genre')
            if args.comment:
                self.tagging(list_file, args.comment, 'comment')
            if args.composer:
                self.tagging(list_file, args.composer, 'composer')
            if args.remixed:
                self.tagging(list_file, args.remixed, 'remixed')
            if args.conductor:
                self.tagging(list_file, args.conductor, 'conductor')
            if args.subtitle:
                self.tagging(list_file, args.subtitle, 'subtitle')
            if args.isrc:
                self.tagging(list_file, args.isrc, 'isrc')
            if args.publisher:
                self.tagging(list_file, args.publisher, 'publisher')
            if args.url:
                self.tagging(list_file, args.url, 'url')
            if args.encoded:
                self.tagging(list_file, args.encoded, 'encoded')
            if args.image:
                debug(process = "set image cover ...")
                self.tagging(list_file, args.image, 'image', cover= args.cover)
            if args.lyric:
                self.tagging(list_file, args.lyric, 'lyric')
            if args.licface:
                try:
                    self.tagging_multi(list_file, 'all', 'track', args.total_track, dont_save= True)
                    self.tagging_multi(list_file, args.disc, 'disc', args.total_disc, dont_save= True)
                    #self.tagging(list_file, args.album, 'album')
                    #self.tagging(list_file, args.artist, 'artist')
                    #self.tagging(list_file, args.album_artist, 'album_artist')
                    #self.tagging(list_file, args.original_artist, 'original_artist')
                    self.tagging_multi(list_file, datetime.datetime.strftime(datetime.datetime.now(), '%Y'), 'year', dont_save= True)
                    #self.tagging(list_file, args.genre, 'genre')
                    self.tagging_multi(list_file, "LICFACE (licface@yahoo.com)", 'comment', dont_save= True)
                    #self.tagging(list_file, args.composer, 'composer')
                    self.tagging_multi(list_file, '', 'remixed', dont_save= True)
                    self.tagging_multi(list_file, '', 'conductor', dont_save= True)
                    self.tagging_multi(list_file, '', 'subtitle', dont_save= True)
                    self.tagging_multi(list_file, '', 'isrc', dont_save= True)
                    self.tagging_multi(list_file, "LICFACE", 'publisher', dont_save= True)
                    self.tagging_multi(list_file, datetime.datetime.strftime(datetime.datetime.now(), '%Y'), 'copyright', dont_save= True)
                    self.tagging_multi(list_file, "licface@yahoo.com", 'url', dont_save= True)
                    self.tagging_multi(list_file, "BLACKID", 'encoded', dont_save= True)
                    if args.image:                    
                        self.tagging_multi(list_file, args.image, 'image', cover = args.cover, cover_desc= args.cover_description, cover_image_file= args.image, dont_save= True)
                    debug(self_dict_tags = self.dict_tags)
                    #debug(self_dict_tags_1 = self.dict_tags.get('07. Goldbrun VII.mp3'))
                    import clipboard
                    clipboard.copy(unicode(self.dict_tags))                    
                    for i in self.dict_tags:
                        tag_id3 = id3.ID3(self.dict_tags.get(i).get('fullpath'))
                        self.dict_tags.get(i).pop('fullpath')
                        for x in self.dict_tags.get(i).keys():
                            debug(i = i)
                            debug(x = x)
                            debug(self_dict_tags_get_i = self.dict_tags.get(i))
                            debug(self_dict_tags_get_i_get_x = self.dict_tags.get(i).get(x))
                            tags = self.dict_tags.get(i).get(x)
                            debug(tags = tags)
                            tag_instance = TAGGER.get(x)
                            debug(tag_instance = tag_instance)
                            #print "tag_id3_0 =", tag_id3
                            #debug(tag_id3_0 = tag_id3)
                            tag_id3.setall(tag_instance.__name__, tags)
                            #print "tag_id3_1 =", tag_id3
                            #debug(tag_id3_1 = tag_id3)
                        tag_id3.save()
                        debug(s = "*" * 40)
                except:
                    traceback.format_exc(print_msg= True)
                

if __name__ == '__main__':
    pid = os.getpid()
    print "PID:", pid
    print make_colors("=" * max_file_length, 'magenta')
    c = tag()
    c.usage()
    #k = mutagen.id3.PictureType()
    #instance_pictype = dir(mutagen.id3.PictureType)[0:20]
    #covertype = {}
    #for i in instance_pictype:
        #covertype.update({
            #str(i).lower(): k.__getattribute__(str(i).upper())
        #})

    #import pprint
    #pprint.pprint(covertype)
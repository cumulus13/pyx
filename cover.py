import os
import sys
import shutil


def copyall(filename, path, ext = '.jpg', numbers = 0):
    if numbers == 1:
        if not os.path.isfile(os.path.join(path, 'Cover') + ext):
            print "COPY: %s --> %s" % (filename, os.path.join(path, 'Cover') + ext)
            shutil.copyfile(os.path.abspath(filename), os.path.join(path, 'Cover') + ext)
    if numbers == 2:
        if not os.path.isfile(os.path.join(path, 'Folder') + ext):
            print "COPY: %s --> %s" % (filename, os.path.join(path, 'Folder') + ext)
            shutil.copyfile(os.path.abspath(filename), os.path.join(path, 'Folder') + ext)
    if numbers == 3:
        if not os.path.isfile(os.path.join(path, 'Folder1') + ext):
            print "COPY: %s --> %s" % (filename, os.path.join(path, 'Folder1') + ext)
            shutil.copyfile(os.path.abspath(filename), os.path.join(path, 'Folder1') + ext)
    if numbers == 4:
        if not os.path.isfile(os.path.join(path, 'Front') + ext):
            print "COPY: %s --> %s" % (filename, os.path.join(path, 'Front') + ext)
            shutil.copyfile(os.path.abspath(filename), os.path.join(path, 'Front') + ext)
    if numbers == 5:
        if not os.path.isfile(os.path.join(path, 'Poster') + ext):
            print "COPY: %s --> %s" % (filename, os.path.join(path, 'Poster') + ext)
            shutil.copyfile(os.path.abspath(filename), os.path.join(path, 'Poster') + ext)
    if numbers == 0:
        #print "path =", path
        #print "type(path) =", type(path)
        if not os.path.isfile(os.path.join(path, 'Cover') + ext):
            print "COPY: %s --> %s" % (filename, os.path.join(path, 'Cover') + ext)
            shutil.copyfile(os.path.abspath(filename), os.path.join(path, 'Cover') + ext)
        if not os.path.isfile(os.path.join(path, 'Folder') + ext):
            print "COPY: %s --> %s" % (filename, os.path.join(path, 'Folder') + ext)
            shutil.copyfile(os.path.abspath(filename), os.path.join(path, 'Folder') + ext)
        if not os.path.isfile(os.path.join(path, 'Folder1') + ext):
            print "COPY: %s --> %s" % (filename, os.path.join(path, 'Folder1') + ext)
            shutil.copyfile(os.path.abspath(filename), os.path.join(path, 'Folder1') + ext)
        if not os.path.isfile(os.path.join(path, 'Front') + ext):
            print "COPY: %s --> %s" % (filename, os.path.join(path, 'Front') + ext)
            shutil.copyfile(os.path.abspath(filename), os.path.join(path, 'Front') + ext)
        if not os.path.isfile(os.path.join(path, 'Poster') + ext):
            print "COPY: %s --> %s" % (filename, os.path.join(path, 'Poster') + ext)
            shutil.copyfile(os.path.abspath(filename), os.path.join(path, 'Poster') + ext)        

if len(sys.argv) > 1:
    if os.path.isfile(sys.argv[1]):
        path = os.path.dirname(os.path.abspath(sys.argv[1]))
        # print "PATH =", path
        ext = os.path.splitext(sys.argv[1])
        copyall(os.path.basename(sys.argv[1]), path, ext[1])
        if ext[1].lower() != ".jpg":
            from PIL import Image
            im = Image.open(sys.argv[1])
            im.save(os.path.join(path, os.path.splitext(os.path.basename(sys.argv[1]))[0]) + ".jpg")
            copyall(os.path.join(path, os.path.splitext(os.path.basename(sys.argv[1]))[0]) + ".jpg", path, ".jpg")

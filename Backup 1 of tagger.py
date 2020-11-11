import sys
path = r"d:\PROJECTS"
sys.path.insert(0, path)
from tagger.tagger import Tagger

t = Tagger()
t.usage()
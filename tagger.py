#!/usr/bin/env python3
import sys
path = r"D:\PROJECTS2"
sys.path.insert(0, path)
from tagger.tagger import Tagger

t = Tagger()
t.usage()
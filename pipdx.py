import os
import sys
import argparse

class pipd(object):
    def __init__(self, **kwargs):
        super(pipd, self)
        if len(kwargs) > 0:
            for i in kwargs:
                setattr(self, i, kwargs.get(i))
        self.PYTHON_PATH = r'c:\Python27\Scripts\pip.exe'
                    
    
    def usage(self):
        pass
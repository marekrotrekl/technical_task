#!/usr/bin/env python3
"""
This module contains RandomFileTest class.
"""

from .TestCase import TestCase, StopExecution
import os, tempfile
import psutil as p

class RandomFileTest(TestCase):
    """
    •	[prep] If the current host’s RAM is less than one gigabyte, interrupt the test case.
    •	[run] Create a file test of size 1024 KB with random contents.
    •	[clean_up] Remove the file test.
    """

    def prep(self):
        self._tempfile = tempfile.gettempdir()+'\\test.bin'
        mem = p.virtual_memory()
        if mem.total < (1024.**3):
            raise StopExecution(("Prerequisities Error: Current host’s RAM " + 
            "(%s GB) is less than one gigabyte.") % (mem.total/(1024.**3)))

    def run(self):
        with open(os.path.join(self._tempfile), 'wb') as fh:
                fh.write(os.urandom(1024**2))                

    def clean_up(self):
        if os.path.exists(self._tempfile):
            os.remove(self._tempfile)
  
if __name__ == "__main__":
    import doctest
    doctest.testmod()

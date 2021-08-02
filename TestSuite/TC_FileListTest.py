#!/usr/bin/env python3
"""
This module contains FileListTest class.
"""

from .TestCase import TestCase, StopExecution
import time, os

class FileListTest(TestCase):
    """
    •	[prep] If the current system time taken as an integer since the Unix Epoch is not divisible by 2, interrupt the test case.
    •	[run] List all files in the user’s home directory.
    •	[clean_up] (do nothing).
    """

    def prep(self):
        t = int(time.time())
        if (t % 2) != 0:
            raise StopExecution("Prerequisities Error: Current system time taken as" + 
            "an integer since the Unix Epoch is not divisible by 2.")

    def run(self):
        home_dir = os.path.expanduser('~')
        print("User’s home directory (%s):" % home_dir)
        print()
        for _ in os.listdir(home_dir):
            print(_)
        print()

    def clean_up(self):
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
#!/usr/bin/env python3

from TestSuite.TC_FileListTest import FileListTest
from TestSuite.TC_RandomFileTest import RandomFileTest

def main():
    prvni = FileListTest("x1", "prvni")
    prvni.execute()

    druhy = RandomFileTest("x2", "druhy")
    druhy.execute()

if __name__ == '__main__':
    main()





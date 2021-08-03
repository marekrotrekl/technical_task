#!/usr/bin/env python3

from TestSuite.TC_FileListTest import FileListTest
from TestSuite.TC_RandomFileTest import RandomFileTest

def main():
    first_test = FileListTest("T1", "File list")
    first_test.execute()

    second_test = RandomFileTest("T2", "Random Files")
    second_test.execute()

if __name__ == '__main__':
    main()





# technical_task

xcopy.py

Copies files according to the provided configuration file. Configuration file must be in XML format. Each entry in the configuration file should contain file name, source path and destination path parameters. File with specified name must be copied from source to destination.


int_check.py

Input file contains file names, hash algorithms (one of MD5, SHA1, SHA256) and file contents’ hash sums, that are computed using corresponding algorithm. Write a program that reads the input file and checks integrity of the files listed there.


TestSuite

Prototype of an automated test system that has two test cases. We do not recommend using an external test automation module here.
Test system should be implemented as class hierarchy, where test cases are implemented as different classes. 
Each test case has:
•	Unique ID (tc_id) and a name (name)
•	Separate methods for preparing the system (prep), running the test (run) and cleaning up after the test (clean_up). 
•	Method execute that defines the common workflow of a test and handles all exceptions. 
All stages of all test cases along with any exceptions should be logged to a log file or to the stdout.
Test case 1: File list
•	[prep] If the current system time taken as an integer since the Unix Epoch is not divisible by 2, interrupt the test case.
•	[run] List all files in the user’s home directory.
•	[clean_up] (do nothing).
Test case 2: Random file
•	[prep] If the current host’s RAM is less than one gigabyte, interrupt the test case.
•	[run] Create a file test of size 1024 KB with random contents.
•	[clean_up] Remove the file test.








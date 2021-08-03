#!/usr/bin/env python3
"""
This module contains the TestCase class. The methods prep(), run() and clean_up() need to be reimplemented each time.

>>> from TestCase import TestCase
>>> first_test = TestCase("ID25", "Functional test")
>>> second_test = TestCase("ID26", "")
Traceback (most recent call last):
AssertionError: Test case name must have at least one character
"""
import logging

LOGGING_FORMAT = "%(asctime)s:%(levelname)s:%(message)s"

class StopExecution(Exception): pass

class TestCase:
    """
    Each test case has:
    •	Unique ID (tc_id) and a name (name)
    •	Separate methods for preparing the system (prep), running the test (run) and cleaning up after the test (clean_up). 
    •	Method execute that defines the common workflow of a test and handles all exceptions. 

    """

    def __init__(self, tc_id = '', name = '', log_file = 'test_exec.log'):
        assert len(str(tc_id)) > 0, "Test case ID must have at least one character"
        self._tc_id = str(tc_id)
        assert len(str(name)) > 0, "Test case name must have at least one character"
        self._name = str(name)
        self._log_file = log_file

    @property
    def tc_id(self):
        return self._tc_id

    @property
    def name(self):
        return self._name

    @property
    def log_file(self):
        return self._log_file

    def log_info(self, msg):
        logging.info("{} ({}): {}".format(self.name, self.tc_id, msg))

    def log_error(self, err):
        logging.error(err, exc_info=False)

    def prep(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def clean_up(self):
        raise NotImplementedError

    def _do_prep(self):        
        self.log_info("Starting system preparation")
        try:
            self.prep()
        except Exception as err:
            self.log_error(err)
            self.log_info("Interrupting system preparation")
            print(err)
            print("Interrupting test {} ({}) execution, see log file {}.".format(
                self.name, self.tc_id, self._log_file))
            print()
            raise StopExecution
        else:
            self.log_info("System preparation completed")

    def _do_run(self):
        self.log_info("Starting test execution")
        try:
            self.run()
        except Exception as err:
            self.log_error(err)
            self.log_info("Interrupting test execution")
        else:
            self.log_info("Test execution completed")
            
    def _do_clean_up(self):   
        self.log_info("Starting clean up")
        try:                
            self.clean_up()
        except Exception as err:
            self.log_error(err)
            self.log_info("Interrupting clean up")
        else:
            self.log_info("Clean up completed\n")

    def execute(self):
        logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT,
        filename=self._log_file)        
        try:
            self._do_prep()
        except StopExecution:
            #In case of system preparation error the test shall not be executed.
            pass
        else:
            self._do_run()
        finally:
            #System clean up should be performed in all cases.
            self._do_clean_up() 

if __name__ == "__main__":
    import doctest
    doctest.testmod()
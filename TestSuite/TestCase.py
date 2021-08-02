#!/usr/bin/env python3
"""
This module contains TestCase class.

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

    def prep(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def clean_up(self):
        raise NotImplementedError

    def _do_prep(self):        
        logging.info("Test %s %s: Starting system preparation" % (self.name, self.tc_id))
        try:
            self.prep()
        except Exception as err:
            logging.error(err, exc_info=False)
            logging.info("Interrupting %s %s system preparation" % (self.name, self.tc_id))
            raise StopExecution
        else:
            logging.info("Test %s %s: System preparation completed" % (self.name, self.tc_id))

    def _do_run(self):
        logging.info("Test %s %s: Starting test execution" % (self.name, self.tc_id))
        try:
            self.run()
        except Exception as err:
            logging.error(err, exc_info=False)
            logging.info("Test %s %s: Interrupting test execution" % (self.name, self.tc_id))                                     
        else:
            logging.info("Test %s %s: Test execution completed" % (self.name, self.tc_id))
            
    def _do_clean_up(self):   
        logging.info("Test %s %s: Starting clean up" % (self.name, self.tc_id))
        try:                
            self.clean_up()
        except Exception as err:
            logging.exception(err, exc_info=False)
            logging.info("Test %s %s: Interrupting clean up" % (self.name, self.tc_id))
        else:
            logging.info("Test %s %s: Clean up completed\n" % (self.name, self.tc_id))

    def execute(self):
        logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT,
        filename=self._log_file)        
        try:
            self._do_prep()
        except StopExecution:
            print("Interrupting test %s %s execution, see log file %s." % (
                self.name, self.tc_id, self._log_file))
        else:
            self._do_run()
        finally:
            self._do_clean_up() 

if __name__ == "__main__":
    import doctest
    doctest.testmod()
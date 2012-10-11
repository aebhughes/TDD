#!/usr/bin/python -tt
import sys
# A framework for simple TDD (Test Driven Development). Test cases for
# each module are written in the tests() module as part of the *design*
# and *before* the actual modules themselves are constructed.
#
# Tests are constructed in the form:
#    test(mod_name(parameters), <expected result>)
#
# The script is run in "test mode" with the command line argument
# --test as the first argument. This will return on on-screen report
# showing which tests passed - indicated with a yellow tick or check
# mark - and which ones failed - shown with a red cross.
# 
# The completed, user end code is put in main(), which is executed
# when the --test argument is omitted.

def string1(mys):
    '''Basic skeleton module. Please replace'''
    return mys

fmt_str = '\033[%dm%s\033[0m'

def test(got, expected):
    '''
    Simple (but effective) reporting method called from tests()
    that compares actual output with expected output. Unicode-2714
    is a tick or check-mark.
    '''
    if got == expected:
        prefix = fmt_str % (33, u"\u2714")   #Unicode 'tick/check' mark in yellow
    else:
        prefix = fmt_str % (31, u"X")        #Unicode 'X' mark in red
    print '  %s returned: %s expected: %s' % (prefix, repr(got), repr(expected))


def tests():
    '''
    module tests, in which you code the called module with parameters and
    the expected results as the second parameter.
    '''
    print 'Test check marks'
    test(string1('Hello'), 'Hello')
    test(string1('hello'), 'Hello')

def main():
    '''
    actual (result) code here
    '''
    print 'run with --test'

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        tests()
    else:
        main()

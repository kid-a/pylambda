##------------------------------------------------------------------------------
## tests.py
## 
## Unit tests for pylambda
##------------------------------------------------------------------------------

##------------------------------------------------------------------------------
## local imports
##------------------------------------------------------------------------------
from lexer import *
from parser import *
from terms import *
from algorithms import *

##------------------------------------------------------------------------------
## global imports
##------------------------------------------------------------------------------
import ply.lex as lex
import ply.yacc as yacc
import unittest

##------------------------------------------------------------------------------
## class PyLambdaTest
##------------------------------------------------------------------------------
class PyLambdaTest(unittest.TestCase):

    def test_bound_vars_variable (self):
        self.assertEqual (set([]), bound_vars (Variable ('a')))
        self.assertEqual (set(['b']), 
                          bound_vars (Abstraction 
                                      ('b',
                                       Application 
                                       (Variable ('a'),
                                        Variable ('b')))))


    def test_free_vars (self):
        self.assertEqual (set (['a']), free_vars (Variable ('a')))
        self.assertEqual (set (['a']),
                          free_vars (Abstraction 
                                     ('b',
                                      Application 
                                      (Variable ('a'),
                                       Variable ('b')))))
                          
    def test_substitute (self):
        return

    def test_beta_reduce (self):
        return

    def test_multi_step_beta_reduce (self):
        return
        
##
##------------------------------------------------------------------------------
##  Main
##------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()

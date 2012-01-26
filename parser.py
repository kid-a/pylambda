#!/usr/bin/python

import copy
import ply.yacc as yacc

from terms import Variable as Variable
from terms import Application as Application
from terms import Abstraction as Abstraction 

from operations import bound_vars

# GRAMMAR SPECIFICATION
# Program ::= Term
#
# Term ::= "(" Term ")"
#        | VARIABLE
#        | Term Term
#        | '\\' VARIABLE '.' Term


def p_start (p):
    ''' Program : Term '''
    # print "Bound Variables are: ", bound_vars (p[1])
    # print "Free Variables are: ", free_vars (p[1])
    # print multi_step_beta_reduce (p[1])
    print bound_vars (p[1])


def p_paren (p):
    ''' Term : '(' Term ')' '''
    p[0] = p[2]

def p_variable (p):
    ''' Term : VARIABLE '''
    p[0] = Variable (p[1])

def p_application (p):
    ''' Term : Term Term '''
    p[0] = Application (p[1], p[2])

def p_abstraction (p):
    ''' Term : BACKSLASH VARIABLE '.' Term '''
    p[0] = Abstraction (p[2], p[4])

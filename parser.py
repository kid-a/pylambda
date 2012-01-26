#!/usr/bin/python

import copy
import ply.yacc as yacc

from terms import Variable as Variable
from terms import Application as Application
from terms import Abstraction as Abstraction 

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
    print p[1]


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

## !FIXME move anything but the rules out of here

def bound_vars (uTerm):
    if isinstance (uTerm, Variable):
        return set([])

    elif isinstance (uTerm, Application):
        return bound_vars (uTerm._first).union (bound_vars (uTerm._second))

    elif isinstance (uTerm, Abstraction):
        return set ([uTerm._variable]).union (bound_vars (uTerm._body))


def free_vars (uTerm):
    if isinstance (uTerm, Variable):
        return set([uTerm._name])

    elif isinstance (uTerm, Application):
        return free_vars (uTerm._first).union (free_vars (uTerm._second))

    elif isinstance (uTerm, Abstraction):
        return free_vars (uTerm._body).difference (uTerm._variable)


def substitute (uTerm, uToSubstitute, uNewTerm):
    if isinstance (uTerm, Variable):
        if uTerm._name == uToSubstitute._name:
            return copy.deepcopy (uNewTerm)

    elif isinstance (uTerm, Application):
        uTerm._first = substitute (uTerm._first, uToSubstitute, uNewTerm)
        uTerm._second = substitute (uTerm._second, uToSubstitute, uNewTerm)

    elif isinstance (uTerm, Abstraction):
        if uTerm._variable == uToSubstitute:
            uTerm._variable = substitute (uTerm._variable, uToSubstitute, uNewTerm)
        uTerm._body = substitute (uTerm._body, uToSubstitute, uNewTerm)

    return copy.deepcopy (uTerm)


def beta_reduce (uTerm):
    if isinstance (uTerm, Variable):
        return uTerm

    elif isinstance (uTerm, Abstraction):
        return uTerm

    ## leftmost-outermost choice of redex
    elif isinstance (uTerm, Application):
        ## outermost
        if isinstance (uTerm._first, Abstraction):
            return substitute (uTerm._first._body,
                               uTerm._first._variable,
                               uTerm._second)
        else:
            ## leftmost
            new_first = beta_reduce (uTerm._first)
            ##print new_first, " ", uTerm._first
            if new_first != uTerm._first:
                uTerm._first = new_first
                return uTerm
            else:
                uTerm._second = beta_reduce (uTerm._second)
                return uTerm



def multi_step_beta_reduce (uTerm):
    if isinstance (uTerm, Variable) or isinstance (uTerm, Abstraction):
        return uTerm

    elif isinstance (uTerm, Application):
        t = uTerm
        reductions = []

        while (True):
            t_str = str(t)
            new_t = beta_reduce (t)
            new_t_str = str(new_t)

            if t_str == new_t_str:
                for b, a in reductions:
                    print b, " -> ", a
                return t

            else:
                reductions.append ((t_str, new_t_str))
                t = new_t

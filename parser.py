#!/usr/bin/python

import ply.lex as lex
import ply.yacc as yacc
from lexer import *

# GRAMMAR SPECIFICATION
# Program ::= Term
#
# Term ::= "(" Term ")"
#        | VARIABLE
#        | Term Term
#        | '\\' VARIABLE '.' Term

class Variable:
    def __init__ (self, uName):
        self._name = uName

    def __str__ (self):
        return str (self._name)

    def __eq__ (self, other):
        if isinstance (other, Variable):
            if other._name == self._name:
                return True
        return False

class Application:
    def __init__ (self, uFirst, uSecond):
        self._first = uFirst
        self._second = uSecond
        
    def __str__ (self):
        #return '(' + str (self._first) + ')' + '(' + str (self._second) + ')'
        return str (self._first) + str (self._second)

    def __eq__ (self, other):
        if isinstance (other, Application):
            return (other._first == self._first) and \
                (other._second == self._second)
        return False

class Abstraction:
    def __init__ (self, uVariable, uBody):
        self._variable = uVariable
        self._body = uBody

    def __str__ (self):
        return '(\\' + str (self._variable) + '.' + str (self._body) + ')'

    def __eq__ (self, other):
        if isinstance (other, Abstraction):
            return (other._variable == self._variable) and \
                (other._body == self._body)
        return False
        

def p_start (p):
    ''' Program : Term '''
    # print "Bound Variables are: ", bound_vars (p[1])
    # print "Free Variables are: ", free_vars (p[1])
    print multi_step_beta_reduce (p[1])
    

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
        if uTerm._name == uToSubstitute:
            return uNewTerm

    elif isinstance (uTerm, Application):
        uTerm._first = substitute (uTerm._first, uToSubstitute, uNewTerm)
        uTerm._second = substitute (uTerm._second, uToSubstitute, uNewTerm)

    elif isinstance (uTerm, Abstraction):
        if uTerm._variable == uToSubstitute:
            uTerm._body = substitute (uTerm._body, uToSubstitute, uNewTerm)

    return uTerm


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
        
if __name__ == "__main__":
    lexer = lex.lex ()
    parser = yacc.yacc ()
    
    while True:
        try: s = raw_input ('>>>')
        except EOFError: break
        parser.parse (s)

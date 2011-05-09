#!/usr/bin/python

import ply.lex as lex
import ply.yacc as yacc
from lexer import *

# GRAMMAR SPECIFICATION
# Term ::= "(" Term ")"
#        | VARIABLE
#        | Term Term
#        | '\\' VARIABLE '.' Term  

class Variable:
    def __init__ (self, uName):
        self._name = uName

    def __str__ (self):
        return str (self._name)

class Application:
    def __init__ (self, uFirst, uSecond):
        self._first = uFirst
        self._second = uSecond
        
    def __str__ (self):
        return '(' + str (self._first) + ')' + '(' + str (self._second) + ')'

class Abstraction:
    def __init__ (self, uVariable, uBody):
        self._variable = uVariable
        self._body = uBody

    def __str__ (self):
        return '\\' + str (self._variable) + '.' + str (self._body)

def p_start (p):
    ''' Program : Term '''
    print "Bound Variables are: ", bound_vars (p[1])
    print "Free Variables are: ", free_vars (p[1])
    print beta_reduce (p[1])
    

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

    elif isinstance (uTerm, Application):
        uTerm._first = beta_reduce (uTerm._first)
        uTerm._second = beta_reduce (uTerm._second)
        
        if isinstance (uTerm._first, Abstraction):
            return beta_reduce (substitute (uTerm._first._body,
                                            uTerm._first._variable,
                                            uTerm._second))
        else: return uTerm
        
        
if __name__ == "__main__":
    lexer = lex.lex ()
    parser = yacc.yacc ()
    
    while True:
        try: s = raw_input ('>>>')
        except EOFError: break
        parser.parse (s)

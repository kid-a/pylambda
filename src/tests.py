#!/usr/bin/python

## !FIXME convert this tests into unit tests asap...

from parser import *

## tests
## unify tests
def tests ():
    substitute_test_1 ()
    unify_test_1 ()
    unify_test_2 ()
    unify_test_3 ()

def substitute_test_1 ():
    term1 = Abstraction (Variable('y'), Variable ('y'))
    term1 = substitute (term1, Variable ('y'), Variable('z'))
    print term1


def unify_test_1 ():
    term1 = Variable ('a')
    term2 = Variable ('b')
    unification_result = term1.unify (term2)

    for term_to_substitute in unification_result:
        new_term = unification_result [term_to_substitute]
        term1 = substitute (term1, term_to_substitute, new_term)
        
    print term1

def unify_test_2 ():
    term1 = Abstraction (Variable ('x'), Variable ('x'))
    term2 = Abstraction (Variable ('y'), Variable ('y'))
    unification_result = term1.unify (term2)

    for term_to_substitute in unification_result:
        new_term = unification_result [term_to_substitute]
        term1 = substitute (term1, term_to_substitute, new_term)
        
    print term1 

def unify_test_3 (): ## ! FIXME not working
    term1 = Abstraction (Variable ('x'), Variable ('a'))
    term2 = Abstraction (Variable ('y'), Variable ('y'))
    unification_result = term1.unify (term2)

    print unification_result

    for term_to_substitute in unification_result:
        new_term = unification_result [term_to_substitute]
        term1 = substitute (term1, term_to_substitute, new_term)
        
    print term1
    
def hash_test_1 ():
    term1 = Variable ('x')
    term2 = Variable ('x')
    print term1.__hash__ ()
    print term2.__hash__ ()
    d = { term1 : '1',
          term2 : '2' }
    print d

if __name__ == "__main__":
    ## create a parser
    pass
    

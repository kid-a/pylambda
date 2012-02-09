#!/usr/bin/python

import ply.lex as lex
import ply.yacc as yacc

from lexer import *
from parser import *

from operations import bound_vars

l = """
                      o                  o         o
 ##                   O                  O         O
#  #                  o                  O         o
#  #                  O                  o         o
   #      .oOo. O   o o  .oOoO' `oOOoOO. OoOo. .oOoO  .oOoO'
   #      O   o o   O O  O   o   O  o  o O   o o   O  O   o
   ##     o   O O   o o  o   O   o  O  O o   O O   o  o   O
  ###     oOoO' `OoOO Oo `OoO'o  O  o  o `OoO' `OoO'o `OoO'o
  # #     O         o
 #  #     o'     OoO'                                        
 #   ##

Welcome to pylambda 0.01 (2011-11-23) <http://github.com/kid-a/pylambda>
Press CTRL+D to exit
"""


if __name__ == "__main__":
    print l

    lexer = lex.lex ()
    parser = yacc.yacc ()

    while True:
        try:
            s = raw_input ('>>>')
            if s == "": continue
            term = parser.parse (s)
            print "Bound Variables are: ", bound_vars (term)
            

        except EOFError:
            #print "\nExiting. Bye!"
            break

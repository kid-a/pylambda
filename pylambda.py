#!/usr/bin/python

#pip3 install ply
#python3 pylambda


import ply.lex as lex
import ply.yacc as yacc

from lexer import *
from parser import *

from algorithms import multi_step_beta_reduce

import cmd
import time

PROMPT = '>>>'
INTRO_STR = \
"""
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

Welcome to pylambda 0.02 (2011-02-21) <http://github.com/kid-a/pylambda>
Press CTRL+D to exit
"""

lexer = None
parser = None

class PyLambdaREPL (cmd.Cmd):
    """A REPL for PyLambda."""
    def __init__(self, *args, **kwargs):
        cmd.Cmd.__init__ (self)
        self.prompt = PROMPT
        self.intro = INTRO_STR

    def emptyline (self):
        pass
        
    def default (self, s):
        start_time = time.time ()
        term = parser.parse (s)
        reduced_term = multi_step_beta_reduce (term)
        elapsed_time = time.time () - start_time
        print(reduced_term)
        print("One term reduced in (" + str(round(elapsed_time, 2)) + ") seconds")

    def do_EOF(self, line):
        print("")
        print("Bye!")
        return True


if __name__ == "__main__":
    lexer = lex.lex ()
    parser = yacc.yacc ()
    PyLambdaREPL ().cmdloop ()

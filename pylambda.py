#!/usr/bin/python

import ply.lex as lex
import ply.yacc as yacc

from lexer import *
from parser import *
from utilities import *

from algorithms import bound_vars

# import cmd

# lexer = None
# parser = None

# class PLCommandLine (cmd.Cmd):
#     """Command line processor for PyLambda."""
#     def __init__(self, *args, **kwargs):
#         cmd.Cmd.__init__ (self)
#         self.prompt = '>>>'
#         self.intro = \
# """
#                       o                  o         o
#  ##                   O                  O         O
# #  #                  o                  O         o
# #  #                  O                  o         o
#    #      .oOo. O   o o  .oOoO' `oOOoOO. OoOo. .oOoO  .oOoO'
#    #      O   o o   O O  O   o   O  o  o O   o o   O  O   o
#    ##     o   O O   o o  o   O   o  O  O o   O O   o  o   O
#   ###     oOoO' `OoOO Oo `OoO'o  O  o  o `OoO' `OoO'o `OoO'o
#   # #     O         o
#  #  #     o'     OoO'                                        
#  #   ##

# Welcome to pylambda 0.01 (2011-11-23) <http://github.com/kid-a/pylambda>
# Press CTRL+D to exit
# """
        
#     def default (self, s):
#         term = parser.parse (s)
#         print term
#         print "Bound Variables are: ", bound_vars (term)


if __name__ == "__main__":
    lexer = lex.lex ()
    parser = yacc.yacc ()
    #print (parser.productions)
    print parser.parse ('\\x.x')
    print parser.parse ('a')
    #PLCommandLine ().cmdloop ()

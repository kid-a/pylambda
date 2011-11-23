#!/usr/bin/python

import ply.lex as lex
from ply.lex import LexError

tokens = [
    'VARIABLE',
    'LPAREN',
    'RPAREN',
    'BACKSLASH'
    ]

literals = ['(', ')', '\\', '.']

def t_VARIABLE (t):
    r'[a-z]'
    return t

def t_BACKSLASH (t):
    r'\\'
    return t

if __name__ == "__main__":
    lexer = lex.lex ()
    
    while True:
        try: s = raw_input ('>>>')
        except EOFError: break
        lexer.input (s)

        while True:
            try: tok = lexer.token()
            except LexError: 
                print "Illegal expression"
                break
            if not tok: break
            print tok
        


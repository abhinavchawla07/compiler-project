import ply.lex as lex
import sys

class tokens(object):

    def __init__(self):
        self.reserved = self.getReserved()
        self.tokens = self.getTokens()

    def getTypes(arg):
        return {
            'int':'INT',
            'short':'SHORT',
            'float':'FLOAT',
            'double':'DOUBLE',
            'char':'CHAR',
            'boolean':'BOOLEAN',
            'void':'VOID'
        }

    def getKeywords(arg):
        return {
            'null':'NULL',
            'return':'RETURN',
            'for':'FOR',
            'while':'WHILE',
            'do':'DO',
            'if':'IF',
            'else':'ELSE',
            'break':'BREAK',
            'continue':'CONTINUE',
            'default':'DEFAULT',
            'final':'FINAL',
            'finally':'FINALLY',
            'import':'IMPORT',
            'instanceof':'INSTANCEOF',
            'this':'THIS',
            'throw':'THROW',
            'throws':'THROWS',
            'try':'TRY',
            'catch':'CATCH',
            'byte':'BYTE',
            'case':'CASE',
            'class':'CLASS',
            'const':'CONST',
            'extends':'EXTENDS',
            'new':'NEW',
            'package':'PACKAGE',
            'static':'STATIC',
            'super':'SUPER',
            'switch':'SWITCH',    
        }

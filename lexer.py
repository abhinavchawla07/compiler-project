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

    def getSeperators(self):
        return [
            'L_PAREN',
            'R_PAREN',
            'BLOCK_OPENER',
            'BLOCK_CLOSER',
            'L_SQBR',
            'R_SQBR',
            'SEMICOLON',
            'COMMA',
        ]

    def getOperators(self):
        return [
            'PLUS',
            'MINUS',
            'MULT',
            'DIV',
            'MOD',
            'GREATER',
            'LESSER',
            'GREQ',
            'LESEQ',
            'EQUALS',
            'ASSIGN',
            'NOTEQ',
            'LOGIC_AND',
            'LOGIC_OR',
            'LOGIC_NOT',
            'BIT_AND',
            'BIT_OR',
            'BIT_NOT',
            'BIT_XOR',
            'INCR',
            'DECR',
            'DOT',
            'PLUSEQ',
            'MINUSEQ',
            'MULTEQ',
            'DIVEQ',
            'MODEQ',
            'COLON',
            'QUES',
            'LSHIFT',
            'RSHIFT',
            'LSHIFTEQ',
            'RSHIFTEQ',
        ]

    def getMisc(self):
        return [
                'IDENTIFIER',
                'INT_CONSTANT',
                'FLOAT_CONSTANT',
                'CHAR_CONSTANT',
                'STR_CONSTANT',
                'INLINE_COMMENT',
                'BLOCK_COMMENT',
        ]

    def getReserved(self):
        types = self.getTypes()
        keywords = self.getKeywords()
        return dict(list(types.items()) + list(keywords.items()))

    def getTokens(self):
        operators = self.getOperators()
        separators = self.getSeperators()
        misc = self.getMisc()
        reserved = list(self.reserved.values())
        return operators + separators + misc + reserved


# rules for tokens

# identifiers
def t_INT_CONSTANTS(t):
    r'\-?\d+'
    return int(t.value)

def t_FLOAT_CONSTANTS(t):
    r'\d*\.\d+'
    return float(t.value)

t_STR_CONSTANTS =  r'\"([^\\\n]|(\\.))*?\"'
t_CHAR_CONSTANTS = r"\'([^\\\n]|(\\.))?\'"

# separators
t_L_PAREN = r'\('
t_R_PAREN = r'\)'
t_BLOCK_OPENER = r'\{'
t_BLOCK_CLOSER = r'\}'
t_L_SQBR = r'\['
t_R_SQBR = r'\]'
t_SEMICOLON = r';'
t_COMMA = r','

# operators
PLUS = r'\+'
MINUS = r'\-'
MULT = r'\*'
DIV = r'/'
MOD = r'%'
GREATER = r'>'
LESSER = r'<'
GREQ = r'>='
LESEQ = r'<='
EQUALS = r'=='
ASSIGN = r'='
NOTEQ = r'!='
LOGIC_AND = r'&&'
LOGIC_OR = r'\|\|'
LOGIC_NOT = r'!'
BIT_AND = r'&'
BIT_OR = r'\|'
BIT_NOT = r'~'
BIT_XOR = r'\^'
INCR = r'\+\+'
DECR = r'\-\-'
DOT = r'\.'
PLUSEQ = r'\+='
MINUSEQ = r'\-='
MULTEQ = r'\*='
DIVEQ = r'/='
MODEQ = r'%='
COLON = r':'
QUES = r'\?'
LSHIFT = r'<<'
RSHIFT = r'>>'
LSHIFTEQ = r'<<='
RSHIFTEQ = r'>>='

t_ignore = '\t'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = toks.reserved.get(t.value,'IDENTIFIER')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_INLINE_COMMENT(t):
    r'//.*'
    pass
    # return t

def t_BLOCK_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass
    # return t

def t_error(t):
    print("Illegal Character '%s'" % t.value[0])
    t.lexer.skip(1)

tokObj = Tokens()
tokens = tokObj.getTokens()

lexer = lex.lex()

import ply.lex as lex
import sys

class Tokens(object):

    def __init__(self):
        self.reserved = self.getReserved()
        self.tokens = self.getTokens()

    def getTypes(self):
        return {
            'int':'INT',
            'short':'SHORT',
            'float':'FLOAT',
            'double':'DOUBLE',
            'char':'CHAR',
            'boolean':'BOOLEAN',
            'void':'VOID'
        }

    def getKeywords(self):
        return {
            'abstract': 'ABSTRACT',
            'assert': 'ASSERT',
            'break': 'BREAK',
            'byte': 'BYTE',
            'case': 'CASE',
            'catch': 'CATCH',
            'class': 'CLASS',
            'const': 'CONST',
            'continue': 'CONTINUE',
            'default': 'DEFAULT',
            'do': 'DO',
            'else': 'ELSE',
            'extends': 'EXTENDS',
            'final': 'FINAL',
            'finally': 'FINALLY',
            'for': 'FOR',
            'if': 'IF',
            'import': 'IMPORT',
            'instanceof': 'INSTANCEOF',
            'native': 'NATIVE',
            'new': 'NEW',
            'package': 'PACKAGE',
            'return': 'RETURN',
            'static': 'STATIC',
            'super': 'SUPER',
            'switch': 'SWITCH',
            'this': 'THIS',
            'throw': 'THROW',
            'throws': 'THROWS',
            'try': 'TRY',
            'while': 'WHILE',
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
                'NULL'
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


def main():

    # rules for tokens
    # identifiers
    def t_INT_CONSTANT(t):
        r'\-?\d+'
        return int(t.value)

    def t_FLOAT_CONSTANT(t):
        r'\d*\.\d+'
        return float(t.value)

    t_STR_CONSTANT =  r'\"([^\\\n]|(\\.))*?\"'
    t_CHAR_CONSTANT = r"\'([^\\\n]|(\\.))?\'"

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
    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_MULT = r'\*'
    t_DIV = r'/'
    t_MOD = r'%'
    t_GREATER = r'>'
    t_LESSER = r'<'
    t_GREQ = r'>='
    t_LESEQ = r'<='
    t_EQUALS = r'=='
    t_ASSIGN = r'='
    t_NOTEQ = r'!='
    t_LOGIC_AND = r'&&'
    t_LOGIC_OR = r'\|\|'
    t_LOGIC_NOT = r'!'
    t_BIT_AND = r'&'
    t_BIT_OR = r'\|'
    t_BIT_NOT = r'~'
    t_BIT_XOR = r'\^'
    t_INCR = r'\+\+'
    t_DECR = r'\-\-'
    t_DOT = r'\.'
    t_PLUSEQ = r'\+='
    t_MINUSEQ = r'\-='
    t_MULTEQ = r'\*='
    t_DIVEQ = r'/='
    t_MODEQ = r'%='
    t_COLON = r':'
    t_QUES = r'\?'
    t_LSHIFT = r'<<'
    t_RSHIFT = r'>>'
    t_LSHIFTEQ = r'<<='
    t_RSHIFTEQ = r'>>='
    t_INSTANCEOF = r'instanceof'

    t_ignore = ' \t'

    def t_IDENTIFIER(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = tokObj.reserved.get(t.value,'IDENTIFIER')
        return t

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_INLINE_COMMENT(t):
        r'//.*'
        return t

    def t_BLOCK_COMMENT(t):
        r'/\*(.|\n)*?\*/'
        t.lexer.lineno += t.value.count('\n')
        return t

    def t_error(t):
        print("Illegal Character '%s'" % t.value[0])
        t.lexer.skip(1)


    tokObj = Tokens()
    tokens = tokObj.getTokens()
    lexer = lex.lex()
    code = open(sys.argv[1],"r").read()
    lexer.input(code)

    tokenDict = dict()
    for token in tokens:
        tokenDict[token] = [0,[]]

    while True:
        tok = lexer.token()
        if not tok:
            break
        tokenDict[tok.type][0]+=1
        if tok.value not in tokenDict[tok.type][1]:
            tokenDict[tok.type][1].append(str(tok.value))
    # print(tokenDict)
    for key in tokenDict:
        if(tokenDict[key][0]!=0):
            print(key + " " + str(tokenDict[key][0]) + " "  + ",".join(tokenDict[key][1]))

if __name__ == '__main__':
    main()

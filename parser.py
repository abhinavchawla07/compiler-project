import sys
import lexer
import ply.lex as lex
import ply.yacc as yacc

rules_stored = []

# list of rules

def p_Goal(t):
    '''Goal : CompilationUnit'''
    rules_stored.append(t.slice)

def p_Literal(t):
    '''Literal: INT_CONSTANT
                |FLOAT_CONSTANT
                |CHAR_CONSTANT
                |STR_CONSTANT
                |NULL'''
    rules_stored.append(t.slice)

# data types
def p_Type(t):
    rules_stored.append(t.slice)
    ''' Type : PrimitiveType|ReferenceType'''

def p_PrimitiveType(t):
    '''PrimitiveType: NumericType|BOOLEAN'''
    rules_stored.append(t.slice)

def p_NumericType(t):
    '''NumericType: IntegralType|FloatingPointType'''
    rules_stored.append(t.slice)

def p_IntegralType(t):
    '''IntegralType: BYTE
                    |SHORT
                    |INT
                    |CHAR
                    |LONG'''
    rules_stored.append(t.slice)

def p_FloatingPointType(t):
    '''FloatingPointType: FLOAT|DOUBLE'''
    rules_stored.append(t.slice)

def p_ReferenceType(t):
    '''ReferenceType: ClassType|ArrayType'''
    rules_stored.append(t.slice)

def p_ClassType(t):
    '''ClassType:Name'''
    rules_stored.append(t.slice)

def p_ArrayType(t):
    '''ArrayType: Name L_SQBR R_SQBR
                | PrimitiveType L_SQBR R_SQBR
                | ArrayType L_SQBR R_SQBR'''
    rules_stored.append(t.slice)

def p_Name(t):
    '''Name: SimpleName|QualifiedName'''
    rules_stored.append(t.slice)

def p_SimpleName(t):
    '''SimpleName: IDENTIFIER'''
    rules_stored.append(t.slice)

def p_QualifiedName(t):
    '''QualifiedName: Name DOT IDENTIFIER'''
    rules_stored.append(t.slice)

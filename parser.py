import sys
import lexer
import ply.lex as lex
import ply.yacc as yacc

rules_stored = []

# list of rules

def p_Goal(t):
    "Goal : CompilationUnit"
    rules_stored.append(t.slice)

def p_Literal(t):
    '''Literal : INT_CONSTANT
    | FLOAT_CONSTANT
    | CHAR_CONSTANT
    | STR_CONSTANT
    | NULL'''
    rules_stored.append(t.slice)

# data types
def p_Type(t):
    ''' Type : PrimitiveType
    | ReferenceType'''
    rules_stored.append(t.slice)

def p_PrimitiveType(t):
    '''PrimitiveType : NumericType
    | BOOLEAN'''
    rules_stored.append(t.slice)

def p_NumericType(t):
    '''NumericType : IntegralType
    | FloatingPointType'''
    rules_stored.append(t.slice)

def p_IntegralType(t):
    '''IntegralType : BYTE
    | SHORT
    | INT
    | CHAR
    | LONG'''
    rules_stored.append(t.slice)

def p_FloatingPointType(t):
    '''FloatingPointType : FLOAT
    | DOUBLE'''
    rules_stored.append(t.slice)

def p_ReferenceType(t):
    '''ReferenceType : ClassType
    | ArrayType'''
    rules_stored.append(t.slice)

def p_ClassType(t):
    '''ClassType : Name'''
    rules_stored.append(t.slice)

def p_ArrayType(t):
    '''ArrayType : Name L_SQBR R_SQBR
    | PrimitiveType L_SQBR R_SQBR
    | ArrayType L_SQBR R_SQBR'''
    rules_stored.append(t.slice)

def p_Name(t):
    '''Name : SimpleName
    | QualifiedName'''
    rules_stored.append(t.slice)

def p_SimpleName(t):
    '''SimpleName : IDENTIFIER'''
    rules_stored.append(t.slice)

def p_QualifiedName(t):
    '''QualifiedName : Name DOT IDENTIFIER'''
    rules_stored.append(t.slice)

# compile unit

def p_CompilationUnit(t):
    '''
    CompilationUnit : PackageDeclaration ImportDeclarations TypeDeclarations
    | PackageDeclaration ImportDeclarations
    | PackageDeclaration TypeDeclarations
    | ImportDeclarations TypeDeclarations
    | PackageDeclaration
    | ImportDeclarations
    | TypeDeclarations'''
    rules_stored.append(t.slice)

# declarations

def p_PackageDeclaration(t):
    '''PackageDeclaration : PACKAGE Name SEMICOLON'''
    rules_stored.append(t.slice)

def p_ImportDeclarations(t):
    '''ImportDeclarations : ImportDeclarations ImportDeclaration
    | ImportDeclaration'''
    rules_stored.append(t.slice)

def p_TypeDeclarations(t):
    '''TypeDeclarations : TypeDeclaration
    | TypeDeclarations TypeDeclaration'''
    rules_stored.append(t.slice)

def p_ImportDeclaration(t):
    '''ImportDeclaration : SingleTypeImportDeclaration
    | TypeImportOnDemandDeclaration'''
    rules_stored.append(t.slice)

def p_SingleTypeImportDeclaration(t):
    '''SingleTypeImportDeclaration : IMPORT Name SEMICOLON'''
    rules_stored.append(t.slice)

def p_TypeImportOnDemandDeclaration(t):
    '''TypeImportOnDemandDeclaration : IMPORT Name DOT MULT SEMICOLON'''
    rules_stored.append(t.slice)

def p_TypeDeclaration(t):
    '''TypeDeclaration : ClassDeclaration
    | SEMICOLON'''
    rules_stored.append(t.slice)

# class
def p_Modifiers(t):
    '''Modifiers : Modifier
    | Modifiers Modifier'''
    rules_stored.append(t.slice)

def p_modifier(t):
    '''Modifier : FINAL
    | STATIC'''
    rules_stored.append(t.slice)

def p_ClassDeclaration(t):
    '''ClassDeclaration : Modifiers CLASS IDENTIFIER Super ClassBody
    | Modifiers CLASS IDENTIFIER ClassBody
    | CLASS IDENTIFIER Super ClassBody
    | CLASS IDENTIFIER ClassBody'''
    rules_stored.append(t.slice)

def p_Super(t):
    '''Super : EXTENDS ClassType'''
    rules_stored.append(t.slice)

def p_ClassBody(t):
    '''ClassBody : BLOCK_OPENER ClassBodyDeclarations BLOCK_CLOSER
    | BLOCK_OPENER BLOCK_CLOSER'''
    rules_stored.append(t.slice)

def p_ClassBodyDeclarations(t):
    '''ClassBodyDeclarations : ClassBodyDeclarations ClassBodyDeclaration
    | ClassBodyDeclaration'''
    rules_stored.append(t.slice)

def p_ClassBodyDeclaration(t):
    '''ClassBodyDeclaration : ClassMemberDeclaration
    | StaticInitializer
    | ConstructorDeclaration'''
    rules_stored.append(t.slice)

def p_ClassMemberDeclaration(t):
    '''ClassMemberDeclaration : MethodDeclaration
    | FieldDeclaration'''
    rules_stored.append(t.slice)

def p_MethodDeclaration(t):
    '''MethodDeclaration : MethodHeader MethodBody'''
    rules_stored.append(t.slice)

def p_MethodHeader(t):
    '''MethodHeader : Modifiers Type MethodDeclarator Throws
    | Modifiers VOID MethodDeclarator Throws
    | Type MethodDeclarator Throws
    | VOID MethodDeclarator Throws
    | Modifiers Type MethodDeclarator
    | Modifiers VOID MethodDeclarator
    | Type MethodDeclarator
    | VOID MethodDeclarator'''
    rules_stored.append(t.slice)

def p_MethodDeclarator(t):
    '''MethodDeclarator : IDENTIFIER L_PAREN R_PAREN
    | IDENTIFIER L_PAREN FormalParameterList R_PAREN'''
    rules_stored.append(t.slice)

def p_FormalParametersList(t):
    '''FormalParameterList : FormalParameter
    | FormalParameterList COMMA FormalParameter'''
    rules_stored.append(t.slice)

def p_FormalParameter(t):
    '''FormalParameter : Type VariableDeclaratorId'''
    rules_stored.append(t.slice)

def p_Throws(t):
    '''Throws : THROWS ClassTypeList'''
    rules_stored.append(t.slice)

def p_ClassTypeList(t):
    '''ClassTypeList : ClassType
    | ClassTypeList COMMA ClassType'''
    rules_stored.append(t.slice)

def p_MethodBody(t):
    '''MethodBody : Block
    | SEMICOLON'''
    rules_stored.append(t.slice)

def p_FieldDeclaration(t):
    '''FieldDeclaration : Modifiers Type VariableDeclarators SEMICOLON
    | Type VariableDeclarators SEMICOLON'''
    rules_stored.append(t.slice)

def p_VariableDeclarators(t):
    '''VariableDeclarators : VariableDeclarator
    | VariableDeclarators COMMA VariableDeclarator'''
    rules_stored.append(t.slice)

def p_VariableDeclarator(t):
    '''VariableDeclarator : VariableDeclaratorId
    | VariableDeclaratorId ASSIGN VariableInitializer'''
    rules_stored.append(t.slice)

def p_VariableDeclaratorId(t):
    '''VariableDeclaratorId : IDENTIFIER
    | VariableDeclaratorId L_SQBR R_SQBR'''
    rules_stored.append(t.slice)

def p_VariableInitializer(t):
    '''VariableInitializer : Expression
    | ArrayInitializer'''
    rules_stored.append(t.slice)

def p_StaticInitializer(t):
    '''StaticInitializer : STATIC Block'''
    rules_stored.append(t.slice)

def p_ConstructorDeclaration(t):
    '''ConstructorDeclaration : Modifiers ConstructorDeclarator Throws ConstructorBody
    | Modifiers ConstructorDeclarator ConstructorBody
    | ConstructorDeclarator Throws ConstructorBody
    | ConstructorDeclarator ConstructorBody'''
    rules_stored.append(t.slice)

def p_ConstructorDeclarator(t):
    '''ConstructorDeclarator : SimpleName L_PAREN FormalParameterList R_PAREN
    | SimpleName L_PAREN R_PAREN'''
    rules_stored.append(t.slice)

def p_ConstructorBody(t):
    '''ConstructorBody : BLOCK_OPENER ExplicitConstructorInvocation BlockStatements BLOCK_CLOSER
    | BLOCK_OPENER ExplicitConstructorInvocation BLOCK_CLOSER
    | BLOCK_OPENER BlockStatements BLOCK_CLOSER
    | BLOCK_OPENER BLOCK_CLOSER'''
    rules_stored.append(t.slice)

def p_ExplicitConstructorInvocation(t):
    '''ExplicitConstructorInvocation : THIS L_PAREN ArgumentList R_PAREN SEMICOLON
    | THIS L_PAREN R_PAREN SEMICOLON
    | SUPER L_PAREN ArgumentList R_PAREN SEMICOLON
    | SUPER L_PAREN R_PAREN SEMICOLON'''
    rules_stored.append(t.slice)

# variables and arrays

def p_ArrayInitializer(t):
    '''ArrayInitializer : BLOCK_OPENER VariableInitializers BLOCK_CLOSER
    | BLOCK_OPENER BLOCK_CLOSER'''
    rules_stored.append(t.slice)

def p_VariableInitializers(t):
    '''VariableInitializers : VariableInitializer
    | VariableInitializers COMMA VariableInitializer'''
    rules_stored.append(t.slice)

# block

def p_Block(t):
    '''Block : BLOCK_OPENER BLOCK_CLOSER
    | BLOCK_OPENER BlockStatements BLOCK_CLOSER'''
    rules_stored.append(t.slice)

def p_BlockStatements(t):
    '''BlockStatements : BlockStatement
    | BlockStatements BlockStatement'''
    rules_stored.append(t.slice)

def p_BlockStatement(t):
    '''BlockStatement : LocalVariableDeclarationStatement
    | Statement'''
    rules_stored.append(t.slice)

def p_LocalVariableDeclarationStatement(t):
    '''LocalVariableDeclarationStatement : LocalVariableDeclaration SEMICOLON'''
    rules_stored.append(t.slice)

def p_LocalVariableDeclaration(t):
    '''LocalVariableDeclaration : Type VariableDeclarators'''
    rules_stored.append(t.slice)


# statements
def p_Statement(t):
    '''Statement : StatementWithoutTrailingSubstatement
    | LabeledStatement
    | IfThenStatement
    | IfThenElseStatement
    | WhileStatement
    | ForStatement'''
    rules_stored.append(t.slice)

def p_StatementNoShortIf(t):
    '''StatementNoShortIf : StatementWithoutTrailingSubstatement
    | LabeledStatementNoShortIf
    | IfThenElseStatementNoShortIf
    | WhileStatementNoShortIf
    | ForStatementNoShortIf'''
    rules_stored.append(t.slice)

def p_StatementWithoutTrailingSubstatement(t):
    '''StatementWithoutTrailingSubstatement : Block
    | EmptyStatement
    | ExpressionStatement
    | SwitchStatement
    | DoStatement
    | BreakStatement
    | ContinueStatement
    | ReturnStatement
    | ThrowStatement
    | TryStatement'''
    rules_stored.append(t.slice)

def p_EmptyStatement(t):
    '''EmptyStatement : SEMICOLON'''
    rules_stored.append(t.slice)

def p_ExpressionStatement(p):
    '''ExpressionStatement : StatementExpression SEMICOLON'''
    rules_stored.append(t.slice)

def p_SwitchStatement(t):
    '''SwitchStatement : SWITCH L_PAREN Expression R_PAREN SwitchBlock'''
    rules_stored.append(t.slice)

def p_SwitchBlock(t):
    '''SwitchBlock : BLOCK_OPENER BLOCK_CLOSER
    | BLOCK_OPENER SwitchBlockStatementGroups SwitchLabels BLOCK_CLOSER
    | BLOCK_OPENER SwitchBlockStatementGroups BLOCK_CLOSER
    | BLOCK_OPENER SwitchLabels BLOCK_CLOSER'''
    rules_stored.append(t.slice)

def p_SwitchBlockStatementGroups(t):
    '''SwitchBlockStatementGroups : SwitchBlockStatementGroup
    | SwitchBlockStatementGroups SwitchBlockStatementGroup'''
    rules_stored.append(t.slice)

def p_SwitchBlockStatementGroup(t):
    '''SwitchBlockStatementGroup : SwitchLabels BlockStatements'''
    rules_stored.append(t.slice)

def p_SwitchLabels(t):
    '''SwitchLabels : SwitchLabel
    | SwitchLabels SwitchLabel'''
    rules_stored.append(t.slice)

def p_SwitchLabel(t):
    '''SwitchLabel : CASE ConstantExpression COLON
    | DEFAULT COLON'''
    rules_stored.append(t.slice)

def p_DoStatement(t):
    '''DoStatement : DO Statement WHILE L_PAREN Expression R_PAREN SEMICOLON'''
    rules_stored.append(t.slice)

def p_BreakStatement(t):
    '''BreakStatement : BREAK IDENTIFIER SEMICOLON
    | BREAK SEMICOLON'''
    rules_stored.append(t.slice)

def p_ContinueStatement(t):
    '''ContinueStatement : CONTINUE IDENTIFIER SEMICOLON
    | CONTINUE SEMICOLON'''
    rules_stored.append(t.slice)

def p_ReturnStatement(t):
    '''ReturnStatement : RETURN Expression SEMICOLON
    | RETURN SEMICOLON'''
    rules_stored.append(t.slice)

def p_ThrowStatement(t):
    '''ThrowStatement : THROW Expression SEMICOLON'''
    rules_stored.append(t.slice)

def p_TryStatement(t):
    '''TryStatement : TRY Block Catches
    | TRY Block Catches Finally
    | TRY Block Finally'''
    rules_stored.append(t.slice)

def p_Catches(t):
    '''Catches : CatchClause
    | Catches CatchClause'''
    rules_stored.append(t.slice)

def p_CatchClause(t):
    '''CatchClause : CATCH L_PAREN FormalParameter R_PAREN Block'''
    rules_stored.append(t.slice)

def p_Finally(t):
    '''Finally : FINALLY Block'''
    rules_stored.append(t.slice)

def p_LabeledStatementNoShortIf(t):
    '''LabeledStatementNoShortIf : IDENTIFIER COLON StatementNoShortIf'''
    rules_stored.append(t.slice)

def p_IfThenElseStatementNoShortIf(t):
    '''IfThenElseStatementNoShortIf : IF L_PAREN Expression R_PAREN StatementNoShortIf ELSE StatementNoShortIf'''
    rules_stored.append(t.slice)

def p_WhileStatementNoShortIf(t):
    '''WhileStatementNoShortIf : WHILE L_PAREN Expression R_PAREN StatementNoShortIf'''
    rules_stored.append(t.slice)

def p_ForStatementNoShortIf(t):
    '''ForStatementNoShortIf : FOR L_PAREN ForInit SEMICOLON Expression SEMICOLON ForUpdate R_PAREN StatementNoShortIf
    | FOR L_PAREN SEMICOLON Expression SEMICOLON ForUpdate R_PAREN StatementNoShortIf
    | FOR L_PAREN ForInit SEMICOLON SEMICOLON ForUpdate R_PAREN StatementNoShortIf
    | FOR L_PAREN ForInit SEMICOLON Expression SEMICOLON R_PAREN StatementNoShortIf
    | FOR L_PAREN ForInit SEMICOLON SEMICOLON R_PAREN StatementNoShortIf
    | FOR L_PAREN SEMICOLON Expression SEMICOLON R_PAREN StatementNoShortIf
    | FOR L_PAREN SEMICOLON SEMICOLON ForUpdate R_PAREN StatementNoShortIf
    | FOR L_PAREN SEMICOLON SEMICOLON R_PAREN StatementNoShortIf'''
    rules_stored.append(t.slice)

def p_LabeledStatement(t):
    '''LabeledStatement : IDENTIFIER COLON Statement'''
    rules_stored.append(t.slice)

def p_IfThenStatement(t):
    '''IfThenStatement : IF L_PAREN Expression R_PAREN Statement'''
    rules_stored.append(t.slice)

def p_IfThenElseStatement(t):
    '''IfThenElseStatement : IF L_PAREN Expression R_PAREN StatementNoShortIf ELSE Statement'''
    rules_stored.append(t.slice)

def p_WhileStatement(t):
    '''WhileStatement : WHILE L_PAREN Expression R_PAREN Statement'''
    rules_stored.append(t.slice)

def p_ForStatement(t):
    '''ForStatement : FOR L_PAREN ForInit SEMICOLON Expression SEMICOLON ForUpdate R_PAREN Statement
    | FOR L_PAREN SEMICOLON Expression SEMICOLON ForUpdate R_PAREN Statement
    | FOR L_PAREN ForInit SEMICOLON SEMICOLON ForUpdate R_PAREN Statement
    | FOR L_PAREN ForInit SEMICOLON Expression SEMICOLON R_PAREN Statement
    | FOR L_PAREN ForInit SEMICOLON SEMICOLON R_PAREN Statement
    | FOR L_PAREN SEMICOLON Expression SEMICOLON R_PAREN Statement
    | FOR L_PAREN SEMICOLON SEMICOLON ForUpdate R_PAREN Statement
    | FOR L_PAREN SEMICOLON SEMICOLON R_PAREN Statement'''
    rules_stored.append(t.slice)

#########################End of Rules###################################
def store_output(rules_stored):
    print("Java Parser output\n")
    print(rules_stored)

def main():
    tokens = lexer.tokens
    parser = yacc.yacc()
    input = sys.argv[1]
    filename = input.split('/')[-1].split('.')[0]
    code = open(input,'r').read()
    code += '\n'
    parser.parse(code,debug = 0)
    sys.stdout = open(filename + ".txt",'w')
    store_output(rules_stored)

if __name__ == "__main__":
    main()

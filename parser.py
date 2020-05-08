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
    | CHAR'''
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
    | TypeDeclarations
    |'''
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

def p_ExpressionStatement(t):
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

def p_StatementExpression(t):
    '''StatementExpression : Assignment
    | PreDecrementExpression
    | PreIncrementExpression
    | PostDecrementExpression
    | PostIncrementExpression
    | ClassInstanceCreationExpression
    | MethodInvocation'''
    rules_stored.append(t.slice)

def p_ForInit(t):
    '''ForInit : StatementExpressionList
    | LocalVariableDeclaration'''
    rules_stored.append(t.slice)

def p_ForUpdate(t):
    '''ForUpdate : StatementExpressionList'''
    rules_stored.append(t.slice)

def p_StatementExpressionList(t):
    '''StatementExpressionList : StatementExpression
    | StatementExpressionList COMMA StatementExpression'''
    rules_stored.append(t.slice)

def p_Primary(t):
    '''Primary : PrimaryNoNewArray
    | ArrayCreationExpression'''
    rules_stored.append(t.slice)

def p_PrimaryNoNewArray(t):
    '''PrimaryNoNewArray : Literal
    | THIS
    | L_PAREN Expression R_PAREN
    | ClassInstanceCreationExpression
    | FieldAccess
    | MethodInvocation
    | ArrayAccess'''
    rules_stored.append(t.slice)

def p_ClassInstanceCreationExpression(t):
    '''ClassInstanceCreationExpression : NEW ClassType L_PAREN R_PAREN
    | NEW ClassType L_PAREN ArgumentList R_PAREN'''
    rules_stored.append(t.slice)

def p_ArgumentList(t):
    '''ArgumentList : Expression
    | ArgumentList COMMA Expression'''
    rules_stored.append(t.slice)

def p_ArrayCreationExpression(t):
    '''ArrayCreationExpression : NEW PrimitiveType DimExprs Dims
    | NEW PrimitiveType DimExprs
    | NEW ClassType DimExprs Dims
    | NEW ClassType DimExprs'''
    rules_stored.append(t.slice)

def p_DimExprs(t):
    '''DimExprs : DimExpr
    | DimExprs DimExpr'''
    rules_stored.append(t.slice)

def p_DimExpr(t):
    "DimExpr : L_SQBR Expression R_SQBR"
    rules_stored.append(t.slice)

def p_Dims(t):
    '''Dims : L_SQBR R_SQBR
    | Dims L_SQBR R_SQBR'''
    rules_stored.append(t.slice)

def p_FieldAccess(t):
    '''FieldAccess : Primary DOT IDENTIFIER
    | SUPER DOT IDENTIFIER'''
    rules_stored.append(t.slice)

def p_MethodInvocation(t):
    '''MethodInvocation : Name L_PAREN ArgumentList R_PAREN
    | Name L_PAREN R_PAREN
    | Primary DOT IDENTIFIER L_PAREN ArgumentList R_PAREN
    | Primary DOT IDENTIFIER L_PAREN R_PAREN
    | SUPER DOT IDENTIFIER L_PAREN ArgumentList R_PAREN
    | SUPER DOT IDENTIFIER L_PAREN R_PAREN'''
    rules_stored.append(t.slice)

def p_ArrayAccess(t):
    '''ArrayAccess : Name L_SQBR Expression R_SQBR
    | PrimaryNoNewArray L_SQBR Expression R_SQBR'''
    rules_stored.append(t.slice)

def p_PostfixExpression(t):
    '''PostfixExpression : Primary
    | Name
    | PostIncrementExpression
    | PostDecrementExpression'''
    rules_stored.append(t.slice)

def p_PostIncrementExpression(t):
    '''PostIncrementExpression : PostfixExpression INCR'''
    rules_stored.append(t.slice)

def p_PostDecrementExpression(t):
    '''PostDecrementExpression : PostfixExpression DECR'''
    rules_stored.append(t.slice)

def p_UnaryExpression(t):
    '''UnaryExpression : PreIncrementExpression
    | PreDecrementExpression
    | PLUS UnaryExpression
    | MINUS UnaryExpression
    | UnaryExpressionNotPlusMinus'''
    rules_stored.append(t.slice)

def p_PreIncrementExpression(t):
    "PreIncrementExpression : INCR UnaryExpression"
    rules_stored.append(t.slice)

def p_PreDecrementExpression(t):
    "PreDecrementExpression : DECR UnaryExpression"
    rules_stored.append(t.slice)

def p_UnaryExpressionNotPlusMinus(t):
    '''UnaryExpressionNotPlusMinus : PostfixExpression
    | LOGIC_NOT UnaryExpression
    | BIT_NOT UnaryExpression
    | CastExpression'''
    rules_stored.append(t.slice)

def p_CastExpression(t):
    '''CastExpression : L_PAREN PrimitiveType Dims R_PAREN UnaryExpression
    | L_PAREN Expression R_PAREN UnaryExpressionNotPlusMinus
    | L_PAREN PrimitiveType R_PAREN UnaryExpression
    | L_PAREN Name Dims R_PAREN UnaryExpressionNotPlusMinus'''
    rules_stored.append(t.slice)

def p_MultiplicativeExpression(t):
    '''MultiplicativeExpression : UnaryExpression
    | MultiplicativeExpression MULT UnaryExpression
    | MultiplicativeExpression DIV UnaryExpression
    | MultiplicativeExpression MOD UnaryExpression'''
    rules_stored.append(t.slice)

def p_AdditiveExpression(t):
    '''AdditiveExpression : MultiplicativeExpression
    | AdditiveExpression PLUS MultiplicativeExpression
    | AdditiveExpression MINUS MultiplicativeExpression'''
    rules_stored.append(t.slice)

def p_ShiftExpression(t):
    '''ShiftExpression : AdditiveExpression
    | ShiftExpression LSHIFT AdditiveExpression
    | ShiftExpression RSHIFT AdditiveExpression'''
    rules_stored.append(t.slice)

def p_RelationalExpression(t):
    '''RelationalExpression : ShiftExpression
    | RelationalExpression LESSER ShiftExpression
    | RelationalExpression GREATER ShiftExpression
    | RelationalExpression LESEQ ShiftExpression
    | RelationalExpression GREQ ShiftExpression
    | RelationalExpression INSTANCEOF ReferenceType'''
    rules_stored.append(t.slice)

def p_EqualityExpression(t):
    '''EqualityExpression : RelationalExpression
    | EqualityExpression EQUALS RelationalExpression
    | EqualityExpression NOTEQ RelationalExpression'''
    rules_stored.append(t.slice)

def p_AndExpression(t):
    '''AndExpression : EqualityExpression
    | AndExpression BIT_AND EqualityExpression'''
    rules_stored.append(t.slice)

def p_ExclusiveOrExpression(t):
    '''ExclusiveOrExpression : AndExpression
    | ExclusiveOrExpression BIT_XOR AndExpression'''
    rules_stored.append(t.slice)

def p_InclusiveOrExpression(t):
    '''InclusiveOrExpression : ExclusiveOrExpression
    | InclusiveOrExpression BIT_OR ExclusiveOrExpression'''
    rules_stored.append(t.slice)

def p_ConditionalAndExpression(t):
    '''ConditionalAndExpression : InclusiveOrExpression
    | ConditionalAndExpression LOGIC_AND InclusiveOrExpression'''
    rules_stored.append(t.slice)

def p_ConditionalOrExpression(t):
    '''ConditionalOrExpression : ConditionalAndExpression
    | ConditionalOrExpression LOGIC_OR ConditionalAndExpression'''
    rules_stored.append(t.slice)

def p_ConditionalExpression(t):
    '''ConditionalExpression : ConditionalOrExpression
    | ConditionalOrExpression QUES Expression COLON ConditionalExpression'''
    rules_stored.append(t.slice)

def p_AssignmentExpression(t):
    '''AssignmentExpression : ConditionalExpression
    | Assignment'''
    rules_stored.append(t.slice)

def p_Assignment(t):
    "Assignment : LeftHandSide AssignmentOperator AssignmentExpression"
    rules_stored.append(t.slice)

def p_LeftHandSide(t):
    '''LeftHandSide : Name
    | FieldAccess
    | ArrayAccess'''
    rules_stored.append(t.slice)

def p_AssignmentOperator(t):
    '''AssignmentOperator : ASSIGN
    | PLUSEQ
    | MINUSEQ
    | MULTEQ
    | DIVEQ
    | MODEQ
    | LSHIFTEQ
    | RSHIFTEQ'''
    rules_stored.append(t.slice)
    #check for missing

def p_Expression(t):
    "Expression : AssignmentExpression"
    rules_stored.append(t.slice)

def p_ConstantExpression(t):
    "ConstantExpression : Expression"
    rules_stored.append(t.slice)

def p_error(t):
    print("Syntax Error in line %s" %(t.value))


#########################End of Rules###################################
def print_derivation(lhs,rhs,index):
    print("<div>")
    # lhs
    for i in range (len(lhs)):
        if(index==i):
            print("<span class='tochange'>"+str(lhs[i])+"</span>")
        else:
            if str(type(lhs[i])) == "<class 'ply.yacc.YaccSymbol'>":
                print(str(lhs[i]), end=" ")
            else:
                print("<span class='final'>" + str(lhs[i].value) + "</span>", end=" ")
    # arrow
    print("&nbsp;<span class='arrow'>--></span>&nbsp;", end=" ")
    # rhs
    for i in range(len(rhs)):
        if str(type(rhs[i])) == "<class 'ply.yacc.YaccSymbol'>":
            print(str(rhs[i]), end=" ")
        else:
            print("<span class='final'>" + str(rhs[i].value) + "</span>", end=" ")

    print("</div><br>")

def store_output(rules_stored,filename):
    print('''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Java Parser output</title>
    <link rel='stylesheet' href='../style.css'>
    </head>
    <body>
    <h1>Rightmost Derivation of '''+filename+'''.java</h1><hr><br>
    ''')
    # print(rules_stored)
    rhs = []
    lhs = [rules_stored[-1][0]]
    for rule in rules_stored[::-1]:
        try:
            index = lhs.index(rule[0])
        except ValueError:
            print("Error!")
            return
        rhs_part = [sym for sym in rule[1:]]
        rhs = rhs[:index] + rhs_part + rhs[index+1:]
        print_derivation(lhs,rhs,index)
        lhs = rhs

    print("</body>\n</html>")

def main():
    tokens = lexer.tokens
    parser = yacc.yacc()
    input = sys.argv[1]
    filename = input.split('/')[-1].split('.')[0]
    code = open(input,'r').read()
    code += '\n'
    parser.parse(code,debug = 0)
    sys.stdout = open("output_html_files/"+filename + ".html",'w')
    store_output(rules_stored,filename)

if __name__ == "__main__":
    main()

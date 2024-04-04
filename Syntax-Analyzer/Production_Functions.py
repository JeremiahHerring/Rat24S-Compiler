i = 0
lexerList = [('Separator', '$'), ('Keyword', 'function'), ('Identifier', 'convertx'), ('Separator', '('), ('Identifier', 'fahr'), ('Keyword', 'integer'), ('Separator', ')'), ('Separator', '{'), ('Keyword', 'return'), ('Integer', '5'), ('Operator', '*'), ('Separator', '('), ('Identifier', 'fahr'), ('Operator', '-'), ('Integer', '32'), ('Separator', ')'), ('Operator', '/'), ('Integer', '9'), ('Separator', ';'), ('Separator', '}'), ('Separator', '$'), ('Keyword', 'integer'), ('Identifier', 'low'), ('Separator', ','), ('Identifier', 'high'), ('Separator', ','), ('Identifier', 'step'), ('Separator', ';'), ('Separator', '$'), ('Keyword', 'scan'), ('Separator', '('), ('Identifier', 'low'), ('Separator', ','), ('Identifier', 'high'), ('Separator', ','), ('Identifier', 'step'), ('Separator', ')'), ('Separator', ';'), ('Keyword', 'while'), ('Separator', '('), ('Identifier', 'low'), ('Operator', '<='), ('Identifier', 'high'), ('Separator', ')'), ('Separator', '{'), ('Keyword', 'print'), ('Separator', '('), ('Identifier', 'low'), ('Separator', ')'), ('Separator', ';'), ('Keyword', 'print'), ('Separator', '('), ('Identifier', 'convertx'), ('Separator', '('), ('Identifier', 'low'), ('Separator', ')'), ('Separator', ')'), ('Separator', ';'), ('Identifier', 'low'), ('Operator', '='), ('Identifier', 'low'), ('Operator', '+'), ('Identifier', 'step'), ('Separator', ';'), ('Separator', '}'), ('Keyword', 'endwhile'), ('Separator', '$')]

def lexer(flag=False):
    global i 
    if i != len(lexerList):
        i += 1
        if flag:
            print(f"Token: {lexerList[i-1][0]} Lexeme: {lexerList[i-1][1]}")
    else:
        print("end of list")

def rat24s():
    print("<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")
    if lexerList[i][1] == "$":
        lexer(True)
        optFunctionDefinitions()
        if lexerList[i][1] == "$":
            lexer(True)
            optDeclarationList()
            if lexerList[i][1] == "$":  
                lexer(True)
                statementList()
                if lexerList[i][1] == "$":
                    lexer(True)
                else:
                    print("$ expected")
            else:
                print("$ expected")
        else:
            print("$ expected")
    else:
        print("$ expected")

def optFunctionDefinitions():
    print("<Opt Function Definitions> ::= <Function Definitions> | <Empty>")
    functionDefinitions()
    # TODO: Find some way to fix nonterminal | nonterminal case
    empty()

def functionDefinitions():
    print("<Function Definitions> ::= <Function> <Function Definitions'>")
    function()
    functionDefinitions2()

def functionDefinitions2():
    print("<Function Definitions'> ::= <Function> <Function Definitions'> | ε")
    if lexerList[i][1] == "function":
        function()
        functionDefinitions2()

def function():
    print("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")
    if lexerList[i][1] == "function":
        lexer(True)
        if lexerList[i][0] == "Identifier":
            lexer(True)
            if lexerList[i][1] == "(":
                lexer(True)
                optParameterList()
                if lexerList[i][1] == ")":
                    lexer(True)
                    optDeclarationList()
                    body()
                else:
                    print(") expected")
            else:
                print("( expected")
        else:
            print("Error: Identifier expected")
    else:
        print("Error: function expected")
        
def optParameterList():
    print("<Opt Parameter List> ::= <Parameter List> | <Empty>")
    if lexerList[i][1] == "FIRST OF PARAM LIST":
        parameter()
    else:
        empty()

def parameterList():
    print("<Parameter List> ::= <Parameter> <Parameter List'>")
    parameter()
    parameterList2()

def parameterList2():
    print("<Parameter List'> ::= , <Parameter List> | ε")
    parameterList()

def parameter():
    print("<Parameter> ::= <IDs> <Qualifier>")
    if lexerList[i][0] == "Identifier":
        ids()
        qualifier()
    else:
        print("Error: Identifier expected")

def qualifier():
    print("<Qualifier> ::= integer | boolean | real")
    if (lexerList[i][1] == "integer" or 
        lexerList[i][1] == "boolean" or 
        lexerList[i][0] == "Real"):
        lexer(True)
    else:
        print("Error: Wrong token type")

def body():
    print("<Body> ::= { <Statement List> }")
    if lexerList[i][1] == "{":
        lexer(True)
        statementList()
        if lexerList[i][1] == "}":
            lexer(True)
        else:
            print("Error: } expected")
    else:
        print("Error: { expected")

def optDeclarationList():
    print("<Opt Declaration List> ::= <Declaration List> | <Empty>")
    declarationList()
    empty()

def declarationList():
    print("<Declaration List> ::= <Declaration> <Declaration List'>")
    declaration()
    declarationList2()

def declarationList2():
    print("<Declaration List'> ::= ; <Declaration List> | ε")
    if lexerList[i][1] == ";":
        lexer(True)
        declarationList()
    else:
        print("Error: ; expected")

def declaration():
    print("<Declaration> ::= <Qualifier> <IDs>")
    qualifier()
    ids()

def ids():
    print("<IDs> ::= <Identifier> <IDs'>")
    if lexerList[i][0] == "Identifier":
        lexer(True)
        ids2()

def ids2():
    print("<IDs'> ::= , <IDs> | ε")
    if lexerList[i][1] == ",":
        lexer(True)
        ids()
    else:
        pass
   

def statementList():
    print("<Statement List> ::= <Statement> <Statement List'>")
    statement()
    statementList2()

def statementList2():
    print("<Statement List'> ::= <Statement List> | ε")
    statementList()

def statement():
    print("<Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>")
    # TODO we need to find a way to do nonterminal | nonterminal
    pass

def compound():
    print("<Compound> ::= { <Statement List> }")
    if lexerList[i][1] == "{":
        lexer(True)
        statementList()
        if lexerList[i][1] == "}":
            lexer(True)
        else:
            print("Error: } expected")
    else:
        print("Error: { expected")

def assign():
    print("<Assign> ::= <Identifier> = <Expression> ;")
    if lexerList[i][1] == "=":
        lexer(True)
        if lexerList[i][0] == "Identifier":
            lexer(True)
            if lexerList[i][1] == "=":
                lexer(True)
                expression()
                if lexerList[i][1] == ";":
                    lexer(True)

def if1():
    print("<If> ::= if ( <Condition> ) <Statement> <If'>")
    if lexerList[i][1] == "if":
        lexer(True)
        if lexerList[i][1] == "(":
            lexer(True)
            condition()
            if lexerList[i][1] == ")":
                lexer(True)
                statement()
                if2()

def if2():
    print("<If'> ::= endif | else <Statement> endif")
    if lexerList[i][1] == "endif":
        lexer(True)
    else:
        if lexerList[i][1] == "else":
            lexer(True)
            statement()
            if lexerList[i][1] == "endif":
                lexer(True)

def return1():
    print("<Return> ::= return <Return'>")
    if lexerList[i][1] == "return":
        lexer(True)
        return1()

def return2():
    print("<Return'> ::= ; | <Expression>;")
    if lexerList[i][1] == ";":
        lexer(True)
    else:
        expression()

def print1():
    print("<Print> ::= print ( <Expression> );")
    if lexerList[i][1] == "print":
        lexer(True)
        if lexerList[i][1] == "(":
            lexer(True)
            expression()
            if lexerList[i][1] == ")":
                lexer(True)

def scan():
    print("<Scan> ::= scan ( <IDs> );")
    if lexerList[i][1] == "scan":
        lexer(True)
        if lexerList[i][1] == "(":
            lexer(True)
            ids()
            if lexerList[i][1] == ")":
                lexer(True)

def while1():
    print("<While> ::= while ( <Condition> ) <Statement> endwhile")
    if lexerList[i][1] == "while":
        lexer(True)
        if lexerList[i][1] == "(":
            lexer(True)
            condition()
            if lexerList[i][1] == ")":
                lexer(True)
                statement()
                if lexerList[i][1] == "endwhile":
                    lexer(True)
                else:
                    print("Error: expected endwhile")
            else:
                print("Error: expected )")
        else:
            print("Error: expected (")
    else:
        print("Error: expected while")

def condition():
    print("<Condition> ::= <Expression> <Relop> <Expression>")
    expression()
    relop()
    expression()

def relop():
    print("<Relop> ::= == | != | > | < | <= | =>")
    if lexerList[i][1] in ("==", "!=", ">", "<", "<=", "=>"):
        lexer(True)
    else:
        print("Error: expected valid operator")

def expression():
    print("<Expression> ::= <Term> <Expression'>")
    term()
    expression2()

def expression2():
    print("<Expression'> ::= + <Term> <Expression'> | - <Term> <Expression'> | ε")
    if lexerList[i][1] in ("+", "-"):
        lexer(True)
        term()

def term():
    print("<Term> ::= <Factor> <Term'>")
    factor()
    term2()


def term2():
    print("<Term'> ::= * <Factor> <Term'> | / <Factor> <Term'> | ε")
    if lexerList[i][1] in ("*", "/"):
        lexer(True)
        factor()
        term2()

def factor():
    print("<Factor> ::= - <Primary> | <Primary>")
    if lexerList[i][1] == "-":
        lexer(True)
        primary()
    else:
        primary()

def primary():
    pass

def empty():
    print("<Empty> ::= ε")
    print("--------", lexerList[i][1])
    lexer()

# CALL PROGRAM
rat24s()
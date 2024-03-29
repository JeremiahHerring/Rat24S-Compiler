i = 0
lexerList = [('Separator', '$'), ('Keyword', 'function'), ('Identifier', 'add'), ('Separator', '('), ('Identifier', 'a'), ('Keyword', 'integer'), ('Separator', ','), ('Identifier', 'b'), ('Keyword', 'integer'), ('Separator', ')'), ('Separator', '{'), ('Keyword', 'return'), ('Identifier', 'a'), ('Operator', '+'), ('Identifier', 'b'), ('Separator', ';'), ('Separator', '}'), ('Separator', '$'), ('Keyword', 'print'), ('Separator', '('), ('Identifier', 'add'), ('Separator', '('), ('Integer', '5'), ('Separator', ','), ('Integer', '10'), ('Separator', ')'), ('Separator', ')'), ('Separator', ';'), ('Separator', '$')]

def lexer():
    if i != len(lexerList):
        i += 1
    else:
        print("end of list")

def rat24s():
    if lexerList[i][1] == "$":
        lexer()
        optFunctionDefinitions()
        if lexerList[i][1] == "$":
            lexer()
            if lexerList[i][1] == "$":
                lexer()
                optDeclarationList()
                if lexerList[i][1] == "$":  
                    lexer()
                    statementList()
                    if lexerList[i][1] == "$":
                        lexer()

def optFunctionDefinitions():
    functionDefinitions()
    empty()

def functionDefinitions():
    function()
    functionDefinitions2()

def functionDefinitions2():
    functionDefinitions()

def function():
    if lexerList[i][1] == "function":
        lexer()
        if lexerList[i][0] == "Identifier":
            lexer()
            if lexerList[i][1] == "(":
                lexer()
                optParameterList()
                if lexerList[i][1] == ")":
                    lexer()
                    optDeclarationList()
                    body()

def optParameterList():
    pass

def parameterList():
    pass

def parameterList2():
    pass

def parameter():
    pass

def qualifier():
    pass

def body():
    pass

def optDeclarationList():
    pass

def declarationList():
    pass

def declarationList2():
    pass

def declaration():
    pass

def ids():
    pass

def ids2():
    pass

def statementList():
    pass

def statementList2():
    pass

def statement():
    pass

def compound():
    pass

def assign():
    pass

def if1():
    pass

def if2():
    pass

def return1():
    pass

def return2():
    pass

def print1():
    pass

def scan():
    pass

def while1():
    pass

def condition():
    ## <Condition> ::= <Expression> <Relop> <Expression>
    expression()
    relop()
    expression()

def relop():
    ##  <Relop> ::= == | != | > | < | <= | =>
    if lexerList[i][1] in ("==", "!=", ">", "<", "<=", "=>"):
        lexer()
    else:
        print("Error: expected valid operator")

def expression():
    ##  <Expression> ::= <Term> <Expression'>
    term()
    expression2()

def expression2():
    ## <Expression'> ::= + <Term> <Expression'> | - <Term> <Expression'> | ε
    if lexerList[i][1] in ("+", "-"):
        lexer()
        term()

def term():
    ## <Term> ::= <Factor> <Term'>
    factor()
    term2()


def term2():
    ## <Term'> ::= * <Factor> <Term'> | / <Factor> <Term'> | ε
    if lexerList[i][1] in ("*", "/"):
        lexer()
        factor()
        term2()

def factor():
    ## <Factor> ::= - <Primary> | <Primary>
    if lexerList[i][1] == "-":
        lexer()
        primary()
    else:
        primary()

def primary():
    pass

def empty():
    ## <Empty> ::= ε
    lexer()
i = 0
lexerList = [('Separator', '$'), ('Keyword', 'function'), ('Identifier', 'add'), ('Separator', '('), ('Identifier', 'a'), ('Keyword', 'integer'), ('Separator', ','), ('Identifier', 'b'), ('Keyword', 'integer'), ('Separator', ')'), ('Separator', '{'), ('Keyword', 'return'), ('Identifier', 'a'), ('Operator', '+'), ('Identifier', 'b'), ('Separator', ';'), ('Separator', '}'), ('Separator', '$'), ('Keyword', 'print'), ('Separator', '('), ('Identifier', 'add'), ('Separator', '('), ('Integer', '5'), ('Separator', ','), ('Integer', '10'), ('Separator', ')'), ('Separator', ')'), ('Separator', ';'), ('Separator', '$')]

def lexer():
    if i != len(lexerList):
        i += 1
    else:
        print("end of list")

def rat24s():
    # <Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $
    if lexerList[i][1] == "$":
        lexer()
        optFunctionDefinitions()
        if lexerList[i][1] == "$":
            lexer()
            optDeclarationList()
            if lexerList[i][1] == "$":  
                lexer()
                statementList()
                if lexerList[i][1] == "$":
                    lexer()
                else:
                    print("$ expected")
            else:
                print("$ expected")
        else:
            print("$ expected")
    else:
        print("$ expected")

def optFunctionDefinitions():
    # <Opt Function Definitions> ::= <Function Definitions> | <Empty>
    functionDefinitions()
    # Todo: Find some way to fix nonterminal | nonterminal case
    empty()

def functionDefinitions():
    #  <Function Definitions> ::= <Function> <Function Definitions'>
    function()
    functionDefinitions2()

def functionDefinitions2():
    # <Function Definitions'> ::= <Function Definitions> | ε
    functionDefinitions()

def function():
    # <Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>
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
                else:
                    print(") expected")
            else:
                print("( expected")
        else:
            print("Error: Identifier expected")
    else:
        print("Error: function expected")
        
def optParameterList():
    # <Opt Parameter List> ::= <Parameter List> | <Empty>
    parameter()
    empty()

def parameterList():
    # <Parameter List> ::= <Parameter> <Parameter List'>
    parameter()
    parameterList2()

def parameterList2():
    # <Parameter List'> ::= , <Parameter List> | ε
    parameterList()

def parameter():
    # <Parameter> ::= <IDs> <Qualifier>
    ids()
    qualifier()

def qualifier():
    # <Qualifier> ::= integer | boolean | real
    if (lexerList[i][0] == "Integer" or 
        lexerList[i][1] == "boolean" or 
        lexerList[i][0] == "Real"):
        lexer()
    else:
        print("Error: Wrong token type")

def body():
    # <Body> ::= { <Statement List> }
    if lexerList[i][1] == "{":
        lexer()
        statementList()
        if lexerList[i][1] == "}":
            lexer()
        else:
            print("Error: } expected")
    else:
        print("Error: { expected")

def optDeclarationList():
    # <Opt Declaration List> ::= <Declaration List> | <Empty>
    declarationList()
    empty()

def declarationList():
    # <Declaration List> ::= <Declaration> <Declaration List'>
    declaration()
    declarationList2()

def declarationList2():
    # <Declaration List'> ::= ; <Declaration List> | ε
    if lexerList[i][1] == ";":
        lexer()
        declarationList()
    else:
        print("Error: ; expected")

def declaration():
    # <Declaration> ::= <Qualifier> <IDs>
    qualifier()
    ids()

def ids():
    # <IDs> ::= <Identifier> <IDs'>
    if lexerList[i][0] == "Identifier":
        lexer()
        ids2()

def ids2():
    #  <IDs'> ::= , <IDs> | ε
    if lexerList == ",":
        ids()

def statementList():
    # <Statement List> ::= <Statement> <Statement List'>
    statement()
    statementList2()

def statementList2():
    # <Statement List'> ::= <Statement List> | ε
    statementList()

def statement():
    # <Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>
    # TODO we need to find a way to do nonterminal | nonterminal
    pass

def compound():
    # <Compound> ::= { <Statement List> }
    if lexerList[i][1] == "{":
        lexer()
        statementList()
        if lexerList[i][1] == "}":
            lexer()
        else:
            print("Error: } expected")
    else:
        print("Error: { expected")

def assign():
    # <Assign> ::= <Identifier> = <Expression> ;
    if lexerList[i][1] == "=":
        lexer()
        if lexerList[i][0] == "Identifier":
            lexer()
            if lexerList[i][1] == "=":
                lexer()
                expression()
                if lexerList[i][1] == ";":
                    lexer()

def if1():
    # <If> ::= if ( <Condition> ) <Statement> <If'>
    pass

def if2():
    # <If'> ::= endif | else <Statement> endif
    pass

def return1():
    # <Return> ::= return <Return'>
    pass

def return2():
    # <Return'> ::= ; | <Expression>;
    pass

def print1():
    # <Print> ::= print ( <Expression> );
    pass

def scan():
    # <Scan> ::= scan ( <IDs> );
    pass

def while1():
    # <While> ::= while ( <Condition> ) <Statement> endwhile
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
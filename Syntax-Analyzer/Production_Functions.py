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
    id()
    qualifier()

def qualifier():
    # <Qualifier> ::= integer | boolean | real
    pass

def body():
    # <Body> ::= { <Statement List> }
    pass

def optDeclarationList():
    # <Opt Declaration List> ::= <Declaration List> | <Empty>
    pass

def declarationList():
    # <Declaration List> ::= <Declaration> <Declaration List'>
    pass

def declarationList2():
    # <Declaration List'> ::= ; <Declaration List> | ε
    pass

def declaration():
    # <Declaration> ::= <Qualifier> <IDs>
    pass

def ids():
    # <IDs> ::= <Identifier> <IDs'>
    pass

def ids2():
    #  <IDs'> ::= , <IDs> | ε
    pass

def statementList():
    # <Statement List> ::= <Statement> <Statement List'>
    pass

def statementList2():
    # <Statement List'> ::= <Statement List> | ε
    pass

def statement():
    # <Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>
    pass

def compound():
    # <Compound> ::= { <Statement List> }

    pass

def assign():
    # <Compound> ::= { <Statement List> }
    pass

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
    pass

def relop():
    pass

def expression():
    pass

def expression2():
    pass

def term():
    pass

def term2():
    pass

def factor():
    pass

def primary():
    pass

def empty():
    pass

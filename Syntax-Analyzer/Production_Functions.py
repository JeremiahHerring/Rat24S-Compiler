from LexerFSM.main import lexer, tokens_and_lexemes
i = 0
lexerList = [('Separator', '$'), ('Keyword', 'function'), ('Identifier', 'add'), ('Separator', '('), ('Identifier', 'a'), ('Keyword', 'integer'), ('Separator', ','), ('Identifier', 'b'), ('Keyword', 'integer'), ('Separator', ')'), ('Separator', '{'), ('Keyword', 'return'), ('Identifier', 'a'), ('Operator', '+'), ('Identifier', 'b'), ('Separator', ';'), ('Separator', '}'), ('Separator', '$'), ('Keyword', 'print'), ('Separator', '('), ('Identifier', 'add'), ('Separator', '('), ('Integer', '5'), ('Separator', ','), ('Integer', '10'), ('Separator', ')'), ('Separator', ')'), ('Separator', ';'), ('Separator', '$')]

def lexer():
    if i != len(lexerList):
        i += 1
    else:
        print("end of list")

def rat24s():
    optFunctionDefinitions()
    optDeclarationList()
    statementList()

def optFunctionDefinitions():
    functionDefinitions()

def functionDefinitions():
    function()
    functionDefinitions2()

def functionDefinitions2():
    functionDefinitions()

def function():
    if lexeme == "function":
        lexer()
        if lexerList[i][0] == "Identifier":
            optParameterList()
            optDeclarationList()


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

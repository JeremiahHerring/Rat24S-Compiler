i = 0
flag = True
result = [('Separator', '$'), ('Keyword', 'function'), ('Identifier', 'convertx'), ('Separator', '('), ('Identifier', 'fahr'), ('Keyword', 'integer'), ('Separator', ')'), ('Separator', '{'), ('Keyword', 'return'), ('Integer', '5'), ('Operator', '*'), ('Separator', '('), ('Identifier', 'fahr'), ('Operator', '-'), ('Integer', '32'), ('Separator', ')'), ('Operator', '/'), ('Integer', '9'), ('Separator', ';'), ('Separator', '}'), ('Separator', '$'), ('Keyword', 'integer'), ('Identifier', 'low'), ('Separator', ','), ('Identifier', 'high'), ('Separator', ','), ('Identifier', 'step'), ('Separator', ';'), ('Separator', '$'), ('Keyword', 'scan'), ('Separator', '('), ('Identifier', 'low'), ('Separator', ','), ('Identifier', 'high'), ('Separator', ','), ('Identifier', 'step'), ('Separator', ')'), ('Separator', ';'), ('Keyword', 'while'), ('Separator', '('), ('Identifier', 'low'), ('Operator', '<='), ('Identifier', 'high'), ('Separator', ')'), ('Separator', '{'), ('Keyword', 'print'), ('Separator', '('), ('Identifier', 'low'), ('Separator', ')'), ('Separator', ';'), ('Keyword', 'print'), ('Separator', '('), ('Identifier', 'convertx'), ('Separator', '('), ('Identifier', 'low'), ('Separator', ')'), ('Separator', ')'), ('Separator', ';'), ('Identifier', 'low'), ('Operator', '='), ('Identifier', 'low'), ('Operator', '+'), ('Identifier', 'step'), ('Separator', ';'), ('Separator', '}'), ('Keyword', 'endwhile'), ('Separator', '$')]
def syntax_analyzer(lexerList, i):
    flag = True
    bigStr = ""
    def error(error_type):
        nonlocal flag
        print4(f"Unexpected token '{lexerList[i][0]}' with lexeme '{lexerList[i][1]}'. Error type: {error_type}")
        flag = False

    def print3(text):
        nonlocal bigStr
        if flag:
            bigStr += text + "\n"

    def print4(text):
        nonlocal bigStr
        bigStr += text + "\n"

    def lexer():
        nonlocal i
        if i < len(lexerList):
            i += 1
            if flag:
                print4(f"Token: {lexerList[i-1][0]} Lexeme: {lexerList[i-1][1]}")
        else:
            print4("end of list")
            i = 0

    def rat24s():
        print3("<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")
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
                        lexer()
                    else:
                        error("fourth $ expected")
                else:
                    error("third $ expected")
            else:
                error("second $ expected")
        else:
            error("first $ expected")

    def optFunctionDefinitions():
        print3("<Opt Function Definitions> ::= <Function Definitions> | <Empty>")
        if lexerList[i][1] == "function":
            functionDefinitions()
        else:
            empty()

    def functionDefinitions():
        print3("<Function Definitions> ::= <Function> <Function Definitions'>")
        function()
        functionDefinitions2()

    def functionDefinitions2():
        print3("<Function Definitions'> ::= <Function> | epsilon")
        if lexerList[i][1] == "function":
            function()

    def function():
        print3("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")
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
                        error(") expected")
                else:
                    error("( expected")
            else:
                error("identifier expected")
        else:
            error("keyword function expected")
            
    def optParameterList():
        print3("<Opt Parameter List> ::= <Parameter List> | <Empty>")
        if lexerList[i][0] == "Identifier":
            parameterList()
        else:
            empty()

    def parameterList():
        print3("<Parameter List> ::= <Parameter> <Parameter List'>")
        parameter()
        parameterList2()

    def parameterList2():
        print3("<Parameter List'> ::= , <Parameter List> | epsilon")
        if lexerList[i][1] == ",":
            lexer()
            parameterList()
        else:
            pass

    def parameter():
        print3("<Parameter> ::= <IDs> <Qualifier>")
        ids()
        qualifier()

    def qualifier():
        print3("<Qualifier> ::= integer | boolean | real")
        if (lexerList[i][1] == "integer" or 
            lexerList[i][1] == "boolean" or 
            lexerList[i][1] == "real"):
            lexer()
        else:
            error("wrong token type")
            
    def body():
        print3("<Body> ::= { <Statement List> }")
        if lexerList[i][1] == "{":
            lexer()
            statementList()
            if lexerList[i][1] == "}":
                lexer()
            else:
                error("} expected")
        else:
            error("{ expected")

    def optDeclarationList():
        print3("<Opt Declaration List> ::= <Declaration List> | <Empty>")
        if (lexerList[i][1] == "integer" or 
            lexerList[i][1] == "boolean" or 
            lexerList[i][1] == "real"):        
            declarationList()
        else:
            empty()

    def declarationList():
        print3("<Declaration List> ::= <Declaration> ; <Declaration List'>")
        declaration()
        if lexerList[i][1] == ";":
            lexer()
            declarationList2()
        else:
            error("; expected")

    def declarationList2():
        print3("<Declaration List'> ::= <Declaration List> | epsilon")
        if (lexerList[i][1] == "integer" or 
            lexerList[i][1] == "boolean" or 
            lexerList[i][1] == "real"):
            declarationList()
        else:
            pass

    def declaration():
        print3("<Declaration> ::= <Qualifier> <IDs>")
        qualifier()
        ids()

    def ids():
        print3("<IDs> ::= <Identifier> <IDs'>")
        if lexerList[i][0] == "Identifier":
            lexer()
            ids2()
        else:
            error("identifier expected")

    def ids2():
        print3("<IDs'> ::= , <IDs> | epsilon")
        if lexerList[i][1] == ",":
            lexer()
            ids()
        else:
            pass

    def statementList():
        print3("<Statement List> ::= <Statement> <Statement List'>")
        statement()
        statementList2()

    def statementList2():
        print3("<Statement List'> ::= <Statement List> | epsilon")
        if lexerList[i][1] in ("{", "if", "return", "print", "scan", "while") or lexerList[i][0] == "Identifier":
            statementList()
        else:
            pass

    def statement():
        print3("<Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>")
        if lexerList[i][1] == "{":
            compound()
        elif lexerList[i][0] == "Identifier":
            assign()
        elif lexerList[i][1] == "if":
            if1()
        elif lexerList[i][1] == "return":
            return1()
        elif lexerList[i][1] == "print":
            print1()
        elif lexerList[i][1] == "scan":
            scan()
        elif lexerList[i][1] == "while":
            while1()
        else:
            error("incorrect statement syntax")
        
    def compound():
        print3("<Compound> ::= { <Statement List> }")
        if lexerList[i][1] == "{":
            lexer()
            statementList()
            if lexerList[i][1] == "}":
                lexer()
            else:
                error("} expected")
        else:
            error("{ expected")

    def assign():
        print3("<Assign> ::= <Identifier> = <Expression> ;")
        if lexerList[i][0] == "Identifier":
            lexer()
            if lexerList[i][1] == "=":
                lexer()
                expression()
                if lexerList[i][1] == ";":
                    lexer()
                else:
                    error("; expected")
            else:
                error("= expected")
        else:
            error("identifier expected")

    def if1():
        print3("<If> ::= if ( <Condition> ) <Statement> <If'>")
        if lexerList[i][1] == "if":
            lexer()
            if lexerList[i][1] == "(":
                lexer()
                condition()
                if lexerList[i][1] == ")":
                    lexer()
                    statement()
                    if2()
                else:
                    error(") expected")
            else:
                error("( expected")
        else:
            error("keyword if expected")

    def if2():
        print3("<If'> ::= endif | else <Statement> endif")
        if lexerList[i][1] == "endif":
            lexer()
        else:
            if lexerList[i][1] == "else":
                lexer()
                statement()
                if lexerList[i][1] == "endif":
                    lexer()
                else:
                    error("keyword endif expected")
            else:
                error("keyword 'else' or 'endif' expected")
            
    def return1():
        print3("<Return> ::= return <Return'>")
        if lexerList[i][1] == "return":
            lexer()
            return2()
        else:
            error("keyword return expected")

    def return2():
        print3("<Return'> ::= ; | <Expression>;")
        if lexerList[i][1] == ";":
            lexer()
        else:
            expression()
            if lexerList[i][1] == ";":
                lexer()
            else:
                error("; expected")

    def print1():
        print3("<Print> ::= print ( <Expression> );")
        if lexerList[i][1] == "print":
            lexer()
            if lexerList[i][1] == "(":
                lexer()
                expression()
                if lexerList[i][1] == ")":
                    lexer()
                    if lexerList[i][1] == ";":
                        lexer()
                    else:
                        error("; expected")
                else:
                    error(") expected")
            else:
                error("( expected")
        else:
            error("keyword print expected")

    def scan():
        print3("<Scan> ::= scan ( <IDs> );")
        if lexerList[i][1] == "scan":
            lexer()
            if lexerList[i][1] == "(":
                lexer()
                ids()
                if lexerList[i][1] == ")":
                    lexer()
                    if lexerList[i][1] == ";":
                        lexer()
                    else:
                        error("; expected")
                else:
                    error(") expected")
            else:
                error("( expected")
        else:
            error("keyword scan expected")

    def while1():
        print3("<While> ::= while ( <Condition> ) <Statement> endwhile")
        if lexerList[i][1] == "while":
            lexer()
            if lexerList[i][1] == "(":
                lexer()
                condition()
                if lexerList[i][1] == ")":
                    lexer()
                    statement()
                    if lexerList[i][1] == "endwhile":
                        lexer()
                    else:
                        error("endwhile expected")
                else:
                    error(") expected")
            else:
                error("( expected")
        else:
            error("keyword while expected")

    def condition():
        print3("<Condition> ::= <Expression> <Relop> <Expression>")
        expression()
        relop()
        expression()

    def relop():
        print3("<Relop> ::= == | != | > | < | <= | =>")
        if lexerList[i][1] in ("==", "!=", ">", "<", "<=", "=>"):
            lexer()
        else:
            error("expected valid operator")

    def expression():
        print3("<Expression> ::= <Term> <Expression'>")
        term()
        expression2()

    def expression2():
        print3("<Expression'> ::= + <Term> <Expression'> | - <Term> <Expression'> | epsilon")
        if lexerList[i][1] in ("+", "-"):
            lexer()
            term()
        else:
            pass

    def term():
        print3("<Term> ::= <Factor> <Term'>")
        factor()
        term2()


    def term2():
        print3("<Term'> ::= * <Factor> <Term'> | / <Factor> <Term'> | epsilon")
        if lexerList[i][1] in ("*", "/"):
            lexer()
            factor()
            term2()
        else:
            pass

    def factor():
        print3("<Factor> ::= - <Primary> | <Primary>")
        if lexerList[i][1] == "-":
            lexer()
            primary()
        else:
            primary()

    def primary():
        print3("<Primary> ::= <Identifier> <Primary’> |  <Integer> <Primary’> | <Real> <Primary’> | true <Primary’> | false <Primary’> | ( <Expression> ) <Primary’>")
        if lexerList[i][0] in ("Identifier", "Integer", "Real") or lexerList[i][1] in ("true", "false"):
            lexer()
            primary2()
        elif lexerList[i][1] == "(":
            lexer()
            expression()
            if lexerList[i][1] == ")":
                lexer()
                primary2()
            else:
                error(") expected")
        else:
            error("incorrect primary syntax")

    def primary2():
        print3("<Primary’> ::= ( <IDs> ) <Primary’> | epsilon")
        if lexerList[i][1] == "(":
            lexer()
            ids()
            if lexerList[i][1] == ")":
                lexer()
                primary2()
            else:
                error(") expected")
        else:
            pass

    def empty():
        print3("<Empty> ::= epsilon")
    
    rat24s()
    return bigStr

if __name__ == "__main__":
    i = 0
    print(syntax_analyzer(result, i))
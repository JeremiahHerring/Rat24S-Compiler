i = 0
result = [('Separator', '$'), ('Keyword', 'function'), ('Identifier', 'convertx'), ('Separator', '('), ('Identifier', 'fahr'), ('Keyword', 'integer'), ('Separator', ')'), ('Separator', '{'), ('Keyword', 'return'), ('Integer', '5'), ('Operator', '*'), ('Separator', '('), ('Identifier', 'fahr'), ('Operator', '-'), ('Integer', '32'), ('Separator', ')'), ('Operator', '/'), ('Integer', '9'), ('Separator', ';'), ('Separator', '}'), ('Separator', '$'), ('Keyword', 'integer'), ('Identifier', 'low'), ('Separator', ','), ('Identifier', 'high'), ('Separator', ','), ('Identifier', 'step'), ('Separator', ';'), ('Separator', '$'), ('Keyword', 'scan'), ('Separator', '('), ('Identifier', 'low'), ('Separator', ','), ('Identifier', 'high'), ('Separator', ','), ('Identifier', 'step'), ('Separator', ')'), ('Separator', ';'), ('Keyword', 'while'), ('Separator', '('), ('Identifier', 'low'), ('Operator', '<='), ('Identifier', 'high'), ('Separator', ')'), ('Separator', '{'), ('Keyword', 'print'), ('Separator', '('), ('Identifier', 'low'), ('Separator', ')'), ('Separator', ';'), ('Keyword', 'print'), ('Separator', '('), ('Identifier', 'convertx'), ('Separator', '('), ('Identifier', 'low'), ('Separator', ')'), ('Separator', ')'), ('Separator', ';'), ('Identifier', 'low'), ('Operator', '='), ('Identifier', 'low'), ('Operator', '+'), ('Identifier', 'step'), ('Separator', ';'), ('Separator', '}'), ('Keyword', 'endwhile'), ('Separator', '$')]
def syntax_analyzer(lexerList, i):
    def error(error_type):
        print(f"Unexpected token '{lexerList[i][0]}' with lexeme '{lexerList[i][1]}'. Error type: {error_type}")
    
    def lexer(flag=False):
        nonlocal i
        print(i)
        if i < len(lexerList):
            i += 1
            if flag:
                print(f"Token: {lexerList[i-1][0]} Lexeme: {lexerList[i-1][1]}")
        else:
            print("end of list")
            i = 0

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
                        lexer(True)
                    else:
                        error("fourth $ expected")
                else:
                    error("third $ expected")
            else:
                error("second $ expected")
        else:
            error("first $ expected")

    def optFunctionDefinitions():
        print("<Opt Function Definitions> ::= <Function Definitions> | <Empty>")
        if lexerList[i][1] == "function":
            functionDefinitions()
        else:
            empty()

    def functionDefinitions():
        print("<Function Definitions> ::= <Function> <Function Definitions'>")
        function()
        functionDefinitions2()

    def functionDefinitions2():
        print("<Function Definitions'> ::= <Function> | ε")
        if lexerList[i][1] == "function":
            function()

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
                        error(") expected")
                else:
                    error("( expected")
            else:
                error("identifier expected")
        else:
            error("keyword function expected")
            
    def optParameterList():
        print("<Opt Parameter List> ::= <Parameter List> | <Empty>")
        if lexerList[i][0] == "Identifier":
            parameter()
        else:
            empty()

    def parameterList():
        print("<Parameter List> ::= <Parameter> <Parameter List'>")
        parameter()
        parameterList2()

    def parameterList2():
        print("<Parameter List'> ::= , <Parameter List> | ε")
        if lexerList[i][1] == ",":
            lexer(True)
            parameterList()
        else:
            pass

    def parameter():
        print("<Parameter> ::= <IDs> <Qualifier>")
        ids()
        qualifier()

    def qualifier():
        print("<Qualifier> ::= integer | boolean | real")
        if (lexerList[i][1] == "integer" or 
            lexerList[i][1] == "boolean" or 
            lexerList[i][1] == "real"):
            lexer(True)
        else:
            error("wrong token type")
            
    def body():
        print("<Body> ::= { <Statement List> }")
        if lexerList[i][1] == "{":
            lexer(True)
            statementList()
            if lexerList[i][1] == "}":
                lexer(True)
            else:
                error("} expected")
        else:
            error("{ expected")

    def optDeclarationList():
        print("<Opt Declaration List> ::= <Declaration List> | <Empty>")
        if (lexerList[i][1] == "integer" or 
            lexerList[i][1] == "boolean" or 
            lexerList[i][1] == "real"):        
            declarationList()
        else:
            empty()

    def declarationList():
        print("<Declaration List> ::= <Declaration> ; <Declaration List'>")
        declaration()
        if lexerList[i][1] == ";":
            lexer(True)
            declarationList2()
        else:
            error("; expected")

    def declarationList2():
        print("<Declaration List'> ::= <Declaration List> | ε")
        if lexerList[i][0] == "Identifier":
            declarationList()
        else:
            pass

    def declaration():
        print("<Declaration> ::= <Qualifier> <IDs>")
        qualifier()
        ids()

    def ids():
        print("<IDs> ::= <Identifier> <IDs'>")
        if lexerList[i][0] == "Identifier":
            lexer(True)
            ids2()
        else:
            error("identifier expected")

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
        if lexerList[i][1] in ("{", "if", "return", "print", "scan", "while") or lexerList[i][0] == "Identifier":
            statementList()
        else:
            pass

    def statement():
        print("<Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>")
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
        print("<Compound> ::= { <Statement List> }")
        if lexerList[i][1] == "{":
            lexer(True)
            statementList()
            if lexerList[i][1] == "}":
                lexer(True)
            else:
                error("} expected")
        else:
            error("{ expected")

    def assign():
        print("<Assign> ::= <Identifier> = <Expression> ;")
        if lexerList[i][0] == "Identifier":
            lexer(True)
            if lexerList[i][1] == "=":
                lexer(True)
                expression()
                if lexerList[i][1] == ";":
                    lexer(True)
                else:
                    error("; expected")
            else:
                error("= expected")
        else:
            error("identifier expected")

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
                else:
                    error(") expected")
            else:
                error("( expected")
        else:
            error("keyword if expected")

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
                else:
                    error("keyword endif expected")
            else:
                error("keyword 'else' or 'endif' expected")
            
    def return1():
        print("<Return> ::= return <Return'>")
        if lexerList[i][1] == "return":
            lexer(True)
            return2()
        else:
            error("keyword return expected")

    def return2():
        print("<Return'> ::= ; | <Expression>;")
        if lexerList[i][1] == ";":
            lexer(True)
        else:
            expression()
            if lexerList[i][1] == ";":
                lexer(True)
            else:
                error("; expected")

    def print1():
        print("<Print> ::= print ( <Expression> );")
        if lexerList[i][1] == "print":
            lexer(True)
            if lexerList[i][1] == "(":
                lexer(True)
                expression()
                if lexerList[i][1] == ")":
                    lexer(True)
                    if lexerList[i][1] == ";":
                        lexer(True)
                    else:
                        error("; expected")
                else:
                    error(") expected")
            else:
                error("( expected")
        else:
            error("keyword print expected")

    def scan():
        print("<Scan> ::= scan ( <IDs> );")
        if lexerList[i][1] == "scan":
            lexer(True)
            if lexerList[i][1] == "(":
                lexer(True)
                ids()
                if lexerList[i][1] == ")":
                    lexer(True)
                    if lexerList[i][1] == ";":
                        lexer(True)
                    else:
                        error("; expected")
                else:
                    error(") expected")
            else:
                error("( expected")
        else:
            error("keyword scan expected")

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
                        error("endwhile expected")
                else:
                    error(") expected")
            else:
                error("( expected")
        else:
            error("keyword while expected")

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
            error("expected valid operator")

    def expression():
        print("<Expression> ::= <Term> <Expression'>")
        term()
        expression2()

    def expression2():
        print("<Expression'> ::= + <Term> <Expression'> | - <Term> <Expression'> | ε")
        if lexerList[i][1] in ("+", "-"):
            lexer(True)
            term()
        else:
            pass

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
        else:
            pass

    def factor():
        print("<Factor> ::= - <Primary> | <Primary>")
        if lexerList[i][1] == "-":
            lexer(True)
            primary()
        else:
            primary()

    def primary():
        print("<Primary> ::= <Identifier> <Primary’> |  <Integer> <Primary’> | <Real> <Primary’> | true <Primary’> | false <Primary’> | ( <Expression> ) <Primary’>")
        if lexerList[i][0] in ("Identifier", "Integer", "Real") or lexerList[i][1] in ("true", "false"):
            lexer(True)
            primary2()
        elif lexerList[i][1] == "(":
            lexer(True)
            expression()
            if lexerList[i][1] == ")":
                lexer(True)
                primary2()
            else:
                error(") expected")
        else:
            error("incorrect primary syntax")

    def primary2():
        print("<Primary’> ::= ( <IDs> ) <Primary’> | ε")
        if lexerList[i][1] == "(":
            lexer(True)
            ids()
            if lexerList[i][1] == ")":
                lexer(True)
                primary2()
            else:
                error(") expected")
        else:
            pass

    def empty():
        print("<Empty> ::= ε")
    
    rat24s()

if __name__ == "__main__":
    i = 0
    syntax_analyzer(result, i)
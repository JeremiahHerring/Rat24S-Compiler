#TODO Add changes to compound function (idk what's supposed to go here),
# Test everything make sure it works

i = 0
flag = True
current_type = None

result = [('Separator', '$'), ('Separator', '$'), ('Keyword', 'integer'), ('Identifier', 'i'), ('Separator', ','), ('Identifier', 'max'), ('Separator', ','), ('Identifier', 'sum'), ('Separator', ';'), ('Separator', '$'), ('Identifier', 'sum'), ('Operator', '='), ('Integer', '0'), ('Separator', ';'), ('Identifier', 'i'), ('Operator', '='), ('Integer', '1'), ('Separator', ';'), ('Keyword', 'scan'), ('Separator', '('), ('Identifier', 'max'), ('Separator', ','), ('Identifier', 'sum'), ('Separator', ')'), ('Separator', ';'), ('Keyword', 'while'), ('Separator', '('), ('Identifier', 'i'), ('Operator', '<'), ('Identifier', 'max'), ('Separator', ')'), ('Separator', '{'), ('Identifier', 'sum'), ('Operator', '='), ('Identifier', 'sum'), ('Operator', '+'), ('Identifier', 'i'), ('Separator', ';'), ('Identifier', 'i'), ('Operator', '='), ('Identifier', 'i'), ('Operator', '+'), ('Integer', '1'), ('Separator', ';'), ('Separator', '}'), ('Keyword', 'endwhile'), ('Keyword', 'print'), ('Separator', '('), ('Identifier', 'sum'), ('Operator', '+'), ('Identifier', 'max'), ('Separator', ')'), ('Separator', ';'), ('Separator', '$')]
result1 = [('Separator', '$'), ('Separator', '$'), ('Keyword', 'integer'), ('Identifier', 'a'), ('Separator', ','), ('Identifier', 'b'), ('Separator', ','), ('Identifier', 'c'), ('Separator', ';'), ('Separator', '$'), ('Keyword', 'if'), ('Separator', '('), ('Identifier', 'a'), ('Operator', '<'), ('Identifier', 'b'), ('Separator', ')'), ('Identifier', 'a'), ('Operator', '='), ('Identifier', 'c'), ('Separator', ';'), ('Keyword', 'endif'), ('Separator', '$')]

def syntax_analyzer(lexerList, i):
    flag = True
    bigStr = ""
    symbol_table_str = ""
    instr_table_str = ""
    symbol_table = {}
    Memory_Address = 5000
    in_declaration = True
    instr_table = [{} for x in range(1000)]
    instruction_address = 1
    jumpstack = []

    def insert(identifier, type):
        nonlocal Memory_Address
        nonlocal symbol_table
        if identifier in symbol_table:
            print("Identifier '{}' already declared".format(identifier))
        else:
            symbol_table[identifier] = {'memory_address' : Memory_Address, 'type' : type}
            Memory_Address += 1

    def check(identifier):
        nonlocal symbol_table
        if identifier not in symbol_table:
            print("Identifier '{}' not declared".format(identifier))

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
        nonlocal in_declaration
        print3("<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")
        if lexerList[i][1] == "$":
            lexer()
            optFunctionDefinitions()
            if lexerList[i][1] == "$":
                lexer()
                optDeclarationList()
                if lexerList[i][1] == "$":  
                    in_declaration = False
                    check_identifiers_after_declaration()
                    check_type_match_after_declaration()
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
    
    def check_identifiers_after_declaration():
    # Check each identifier after the declaration section
        for token_type, lexeme in lexerList[i+1:]:
            if token_type == "Identifier":
                check(lexeme)
            elif lexeme == "$":
                break

    def check_type_match_after_declaration():
        nonlocal i
        for index in range(i+1, len(lexerList)):
            token, lexeme = lexerList[index]
            if token == "Operator":
                if index + 1 < len(lexerList):
                    prev_lexeme = lexerList[index - 1][1]
                    next_lexeme = lexerList[index + 1][1]
                    if next_lexeme in symbol_table:
                        prev_type = symbol_table[prev_lexeme]['type']
                        declared_type = symbol_table[next_lexeme]['type']
                        if declared_type != prev_type:
                            print(f"Error matching {prev_lexeme} with type {prev_type} and {next_lexeme} with type {declared_type}")
                            break
                        if declared_type == symbol_table[prev_lexeme]['type']:
                            break
                    if symbol_table[prev_lexeme]['type'] == "integer" and not next_lexeme.isdigit():
                        print(f"Error type matching with {prev_lexeme} and {next_lexeme}")
                    if symbol_table[prev_lexeme]['type'] == "boolean" and not next_lexeme in ("true", "false"):
                        print(f"Error type matching with {prev_lexeme} and {next_lexeme}")
                  
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
        global current_type
        if lexerList[i][1] in ("integer", "boolean"):
            current_type = lexerList[i][1]
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
            if in_declaration and current_type is not None:
                insert(lexerList[i][1], current_type)
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
            save = lexerList[i][1]
            lexer()
            if lexerList[i][1] == "=":
                lexer()
                expression()
                generate_instruction("POPM", get_address(save))
                if lexerList[i][1] == ";":
                    lexer()
                else:
                    error("; expected")
            else:
                error("= expected")
        else:
            error("identifier expected")

    def if1():
        nonlocal instruction_address
        print3("<If> ::= if ( <Condition> ) <Statement> <If'>")
        if lexerList[i][1] == "if":
            lexer()
            if lexerList[i][1] == "(":
                lexer()
                condition()
                if lexerList[i][1] == ")":
                    lexer()
                    statement()
                    back_patch(instruction_address)
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
            generate_instruction("LABEL", "nil")
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
                        generate_instruction("SOUT", "nil")
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
        nonlocal i
        print3("<Scan> ::= scan ( <IDs> );")
        if lexerList[i][1] == "scan":
            generate_instruction("SIN", "nil")
            lexer()
            if lexerList[i][1] == "(":
                lexer()
                for index in range(i, len(lexerList)):
                    if lexerList[index][1] == ")":
                        break
                    if lexerList[index][1] == ",":
                        continue
                    generate_instruction("POPM", get_address(lexerList[index][1]))
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
        nonlocal instruction_address
        print3("<While> ::= while ( <Condition> ) <Statement> endwhile")
        if lexerList[i][1] == "while":
            Ar = instruction_address
            generate_instruction("LABEL", "nil")
            lexer()
            if lexerList[i][1] == "(":
                lexer()
                condition()
                if lexerList[i][1] == ")":
                    lexer()
                    statement()
                    generate_instruction("JUMP", Ar)
                    back_patch(instruction_address)
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
        nonlocal instruction_address
        print3("<Condition> ::= <Expression> <Relop> <Expression>")
        expression()
        op = relop()
        expression()
        if op == "<":
            generate_instruction("LES", "nil")
            push_jumpstack(instruction_address)
            generate_instruction("JUMP0", "nil")
        elif op == ">":
            generate_instruction("GRT", "nil")
            push_jumpstack(instruction_address)
            generate_instruction("JUMP0", "nil")
        elif op == "==":
            generate_instruction("EQU", "nil")
            push_jumpstack(instruction_address)
            generate_instruction("JUMP0", "nil")
        elif op == "!=":
            generate_instruction("NEQ", "nil")
            push_jumpstack(instruction_address)
            generate_instruction("JUMP0", "nil")
        elif op == "<=":
            generate_instruction("LEQ", "nil")
            push_jumpstack(instruction_address)
            generate_instruction("JUMP0", "nil")
        elif op == "=>":
            generate_instruction("GEQ", "nil")
            push_jumpstack(instruction_address)
            generate_instruction("JUMP0", "nil")

    def relop():
        print3("<Relop> ::= == | != | > | < | <= | =>")
        if lexerList[i][1] in ("==", "!=", ">", "<", "<=", "=>"):
            op = lexerList[i][1]
            lexer()
            return op
        else:
            error("expected valid operator")

    def expression():
        print3("<Expression> ::= <Term> <Expression'>")
        term()
        expression2()

    def expression2():
        print3("<Expression'> ::= + <Term> <Expression'> | - <Term> <Expression'> | epsilon")
        if lexerList[i][1] in ("+", "-"):
            save = lexerList[i][1]
            lexer()
            term()
            if save == "+":
                generate_instruction("A", "nil")
            else:
                generate_instruction("S", "nil")
        else:
            pass

    def term():
        print3("<Term> ::= <Factor> <Term'>")
        factor()
        term2()

    def term2():
        print3("<Term'> ::= * <Factor> <Term'> | / <Factor> <Term'> | epsilon")
        if lexerList[i][1] in ("*", "/"):
            save = lexerList[i][1]
            lexer()
            factor()
            if save == "*":
                generate_instruction("M", "nil")
            else:
                generate_instruction("D", "nil")
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
        nonlocal symbol_table
        print3("<Primary> ::= <Identifier> <Primary’> |  <Integer> <Primary’> | <Real> <Primary’> | true <Primary’> | false <Primary’> | ( <Expression> ) <Primary’>")
        if lexerList[i][0] in ("Identifier", "Integer", "Real") or lexerList[i][1] in ("true", "false"):
            address = get_address(lexerList[i][1])
            if isinstance(address, str):
                generate_instruction("PUSHI", address)
            else:
                generate_instruction("PUSHM", address)
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
    
    def generate_instruction(operation, operand):
        nonlocal instruction_address
        instr_table[instruction_address]["address"] = instruction_address
        instr_table[instruction_address]["operation"] = operation
        instr_table[instruction_address]["operand"] = operand
        instruction_address += 1

    def get_address(token):
        # access symbol table at key token and return the address stored in the symbol table
        nonlocal symbol_table
        # Check if the token given to address matches the type in the symbol table
        if token in symbol_table:
            return symbol_table[token]['memory_address']
        else:
            if token.isdigit():
                return str(token)
            elif token == "true":
                return str(1)
            elif token == "false":
                return str(0)
            else:
                return f"Error:{token} not valid"

    def push_jumpstack(instr_addr):
        nonlocal jumpstack
        jumpstack.append(instr_addr)

    def pop_jumpstack():
        if jumpstack:
            return jumpstack.pop()
        else:
            print("Error: Jump stack is empty")
            return None
    
    def back_patch(jump_address):
        # ---------------------------------------------- need to create jumpstack
        addr = pop_jumpstack()
        instr_table[addr]["operand"] = jump_address

    def print_symbol_table(symbol_table):
        nonlocal symbol_table_str
        symbol_table_str = "\nSymbol Table:\n"
        symbol_table_str += "Identifier\tMemory Address\tType\n"
        for identifier, data in symbol_table.items():
            symbol_table_str += f"{identifier}\t\t{data['memory_address']}\t\t{data['type']}\n"
        return symbol_table_str

    def print_instr_table(instr_table):
        nonlocal instr_table_str
        instr_table_str = "\nInstr Table:\n"
        instr_table_str += "Address\tOperation\tOperand\n"
        for instr in instr_table:
            if instr:
                address = instr['address']
                operation = instr['operation']
                operand = instr['operand']
                if operand != "nil":
                    instr_table_str += f"{address}\t\t{operation}\t\t{operand}\n"
                else:
                    instr_table_str += f"{address}\t\t{operation}\n"
        return instr_table_str
    
    rat24s()
    print_symbol_table(symbol_table)
    print_instr_table(instr_table)

    result_str = symbol_table_str + "\n" + instr_table_str
    return bigStr, result_str

if __name__ == "__main__":
    i = 0
    #print(syntax_analyzer(result, i))

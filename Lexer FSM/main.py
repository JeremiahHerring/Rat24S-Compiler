from IdentifierLexer import IdentifierFSM
from IntegerLexer import IntegerFSM
from RealLexer import RealLexer
from Operator import validate_operator, operators
from Separator import validate_separator, separators
from Keywords import validate_keyword, keywords

identifier_fsm = IdentifierFSM()
integer_fsm = IntegerFSM()
real_fsm = RealLexer()
tokenTypes = ["operator", "separator", "keyword", "identifier", "real", "integer", "bad"]
state_machines = [validate_operator, validate_separator, validate_keyword, identifier_fsm.validate_identifier, real_fsm.validate_real, integer_fsm.validate_integer]

def lexer(content):
        indexOfFirstCharOfLexeme = 0
        inputCharTerminatesToken = False
        testingState = 0
        state = False
        i = 0
        while i < len(content):
            if inputCharTerminatesToken and state:
                lexeme = content[indexOfFirstCharOfLexeme:i - 1]
                print(f"Token : {tokenTypes[testingState]}, Lexeme: {lexeme}") # can print here or maybe append to list [(token, lexeme), etc.] to print after?

                # reset variables for next lexeme
                inputCharTerminatesToken = False
                indexOfFirstCharOfLexeme = i
                
            else:
                state, inputCharTerminatesToken = state_machines[testingState](content[i])
                if not inputCharTerminatesToken:
                    state, inputCharTerminatesToken = False, False
                    if not state and not inputCharTerminatesToken:    # and or or
                        testingState = (testingState + 1) % len(tokenTypes)
                        i = indexOfFirstCharOfLexeme - 1

                elif testingState == 1 and not inputCharTerminatesToken:
                    state, inputCharTerminatesToken = False, False
                    if not state and not inputCharTerminatesToken:   # and or or
                        testingState = (testingState + 1) % len(tokenTypes)
                        i = indexOfFirstCharOfLexeme - 1

                elif testingState == 2 and not inputCharTerminatesToken:
                    state, inputCharTerminatesToken = False, False
                    if not state and not inputCharTerminatesToken:   # and or or
                        testingState = (testingState + 1) % len(tokenTypes)
                        i = indexOfFirstCharOfLexeme - 1

                elif testingState == 3 and not inputCharTerminatesToken:
                    state, inputCharTerminatesToken = identifier_fsm.validate_identifier(content[i])
                    # print(state, inputCharTerminatesToken)
                    if not state and not inputCharTerminatesToken:   # and or or
                        testingState = (testingState + 1) % len(tokenTypes)
                        i = indexOfFirstCharOfLexeme - 1

                elif testingState == 4 and not inputCharTerminatesToken:
                    state, inputCharTerminatesToken = False, False
                    if not state and not inputCharTerminatesToken:   # and or or
                        testingState = (testingState + 1) % len(tokenTypes)
                        i = indexOfFirstCharOfLexeme - 1

                elif testingState == 5 and not inputCharTerminatesToken:
                    state, inputCharTerminatesToken = False, False
                    if not state and not inputCharTerminatesToken:   # and or or
                        testingState = (testingState + 1) % len(tokenTypes)
                        i = indexOfFirstCharOfLexeme - 1
                else:
                    print("bad")
            i += 1


def main():
    with open('./input.txt', 'r') as file:
        # content contains the whole input file, you can access each character of the inputstring -> content[i]
        content = file.read()
    
    # given a string, will print the token type and lexeme
    lexer(content)

    # Make instances of each finite state machine
    

    
    

if __name__ == "__main__":
    main()
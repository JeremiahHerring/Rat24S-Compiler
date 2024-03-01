from IdentifierLexer import IdentifierFSM
from IntegerLexer import IntegerFSM
from RealLexer import RealLexer
from Operator import validate_operator, operators
from Separator import validate_separator, separators
from Keywords import validate_keyword, keywords

def main():
    with open('./input.txt', 'r') as file:
        # content contains the whole input file, you can access each character of the inputstring -> content[i]
        content = file.read()

    # given a string, will print the token type and lexeme
    lexer(content)

    # Make instances of each finite state machine
    identifier_fsm = IdentifierFSM()
    integer_fsm = IntegerFSM()
    real_fsm = RealLexer()

    
    def lexer(char):
        lexeme = ""
        inputCharTerminatesToken = False
        for char in content:
            
            # if we are in one of the finite state machines and we get to a separator, then we should return a value we can identify from the validate_x functions
            # (not just reject or false) so we can tell if inputCharTerminatesToken
            if inputCharTerminatesToken and state == accepting:
                token = determineToken()
                print(f"Token : {token}, Lexeme: {lexeme}") # can print here or maybe append to list [(token, lexeme), etc.] to print after?
                lexeme = ""
                inputCharTerminatesToken = False
            else:
                validate_operator(char)
                validate_separator(char)
                validate_keyword(char)
                identifierState = identifier_fsm.validate_identifier(char, prevState)
                realState = real_fsm.validate_real(char, prevState)
                integerState = integer_fsm.validate_integer(char, prevState)

                # maybe for this we return 2 values to help us determine if token was terminated (token terminated when we are at accepting state in prevState and then we go to nonaccepting?)
                integerState, thingToHelpDetermineTerminatedToken = integer_fsm.validate_integer(char, prevState)

                # logic hear using the returned states that will let us know if the token was terminated.
                # ^ update inputuCharTerminatesToken
                if thingToHelpDetermineTerminatedToken:
                    inputCharTerminatesToken = True
        


        

if __name__ == "__main__":
    main()


# have a lexer for each type that iterate over the file together. have them each clasify the token as its own type or not its type -- add to a list for each type.
# then print out at the end in the order that the chars come in
def identifierLexer(char):
        lexeme = ""
        inputCharTerminatesToken = False
        for char in content:
            
            # if we are in one of the finite state machines and we get to a separator, then we should return a value we can identify from the validate_x functions
            # (not just reject or false) so we can tell if inputCharTerminatesToken
            if inputCharTerminatesToken and state == accepting: # maybe state will just be true or false so we don't have to do == accepting
                token = determineToken()
                print(f"Token : {token}, Lexeme: {lexeme}") # can print here or maybe append to list [(token, lexeme), etc.] to print after?
                lexeme = ""
                inputCharTerminatesToken = False
            else:
                state = identifier_fsm.validate_identifier(char, prevState)
                

                # logic hear using the returned states that will let us know if the token was terminated.
                # ^ update inputuCharTerminatesToken
                if something:
                    inputCharTerminatesToken = True
from IdentifierLexer import IdentifierFSM
from IntegerLexer import IntegerFSM
from RealLexer import RealLexer
from Operator import validate_operator, operators
from Separator import validate_separator, separators
from Keywords import validate_keyword, keywords

def main():
    # Make instances of each finite state machine
    identifier_fsm = IdentifierFSM()
    integer_fsm = IntegerFSM()
    real_fsm = RealLexer()

    endOfFile = False
    # while not endOfFile:
    #     lexer(string)

    def lexer(string):
        # Pass string to each FSM

        if identifier_fsm.validate_identifier(string):
            return (f"Token : Identifier, Lexeme: {string}")
        elif integer_fsm.validate_integer(string):
            return (f"Token : Integer, Lexeme: {string}")
        elif real_fsm.validate_real(string):
            return (f"Token : Real, Lexeme: {string}")
        elif validate_keyword(string):
            return (f"Token : Keyword, Lexeme: {string}")
        elif validate_operator(string):
            return (f"Token : Operator, Lexeme: {string}")
        elif validate_separator(string):
            return (f"Token : Separator, Lexeme: {string}")
        else:
            return "Invalid Token Type"

    # Going to have to implement some logic that lets the lexer know how to separate operators and separators when there is no white space between them and other tokens
        
    # Test the Lexer
    test_case = ["while", "x", "!=", "9", "123.13", "["]
    for string in test_case:
        print(lexer(string))

if __name__ == "__main__":
    main()

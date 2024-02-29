from IdentifierLexer import IdentifierFSM
from IntegerLexer import IntegerFSM
from RealLexer import RealLexer

endOfFile = False
while not endOfFile:
    lexer(char)
    print(f"token: {tokenType} lexeme: {lexeme}")

def lexer(char):
    # call the fsm's here?
    pass


identifier_fsm = IdentifierFSM()
identifier = "helloWorld"

if identifier_fsm.validate_identifier(identifier):
    print(f"{identifier} is a valid identifier")
else:
    print(f"{identifier} is not a valid identifier")

from IdentifierLexer import IdentifierFSM
from IntegerLexer import IntegerFSM
from RealLexer import RealLexer
from Operator import OperatorChecker
from Keywords import KeywordChecker
from Separator import SeparatorChecker

def lexer(content):    
    char_pointer = 0
    index_of_first_char_of_lexeme = 0
    length = len(content)

    while char_pointer < length:
        current_char = content[char_pointer]

        # Check each FSM
        identifier_fsm = IdentifierFSM()
        integer_fsm = IntegerFSM()
        real_fsm = RealLexer()
        operator_checker = OperatorChecker()
        keyword_checker = KeywordChecker()
        separator_checker = SeparatorChecker()

        # Feed the current character to each FSM
        id_current_state, id_input_char_terminates_token = identifier_fsm.validate_identifier(current_char)
        print("id stuff", id_current_state, id_input_char_terminates_token)
        int_current_state, int_input_char_terminates_token = integer_fsm.validate_integer(current_char)
        #print("integer stuff", int_current_state, int_input_char_terminates_token)
        real_current_state, real_input_char_terminates_token = real_fsm.validate_real(current_char)
        #print("real stuff", real_current_state, real_input_char_terminates_token)


        # Check if input char terminates token and it is an accepting state
        if (
            (id_input_char_terminates_token and id_current_state) or
            (int_input_char_terminates_token and int_current_state) or
            (real_input_char_terminates_token and real_current_state)
        ):
            # Isolate the token and lexeme
            token = ""
            lexeme = ""

            if int_input_char_terminates_token and int_current_state:
                token = "Integer"
                            
            elif id_input_char_terminates_token and id_current_state:
                token = "Identifier"

            elif real_input_char_terminates_token and real_current_state:
                token = "Real"
                
            lexeme = content[index_of_first_char_of_lexeme : char_pointer]


            print(f"Token: {token}, Lexeme: '{lexeme}'")

            # Update the index for the next lexeme

            while current_char.isspace():
                char_pointer = char_pointer + 1
                current_char = content[char_pointer]
            
            index_of_first_char_of_lexeme = char_pointer
        # Move the char pointer to the next character

        char_pointer += 1

    print("Finished lexer.")

if __name__ == "__main__":
    with open('./input.txt', 'r') as file:
        content = file.read()

    lexer(content)

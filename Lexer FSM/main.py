from IdentifierLexer import IdentifierFSM
from IntegerLexer import IntegerFSM
from RealLexer import RealLexer
from Operator import OperatorChecker, operators
from Keywords import KeywordChecker
from Separator import SeparatorChecker, separators

def determineTwoCharOperator(content, char_pointer):
    isTwoChar = False
    current_char = content[char_pointer]
    if current_char == "!":
        if char_pointer + 1 != len(content) and content[char_pointer + 1] == "=":
            isTwoChar = True

    elif current_char == "=":
        if char_pointer + 1 != len(content) and content[char_pointer + 1] == "=":
           isTwoChar = True

        elif char_pointer + 1 != len(content) and content[char_pointer + 1] == ">":
            isTwoChar = True

    elif current_char == "<":
        if char_pointer + 1 != len(content) and content[char_pointer + 1] == "=":
            isTwoChar = True

    return isTwoChar

def lexer(content):
    starting = True
    content += " "
    char_pointer = 0
    index_of_first_char_of_lexeme = 0
    length = len(content)
    isTwoChar = False
    in_comment = False

    identifier_fsm = IdentifierFSM()
    integer_fsm = IntegerFSM()
    real_fsm = RealLexer()
    operator_checker = OperatorChecker()
    keyword_checker = KeywordChecker()
    separator_checker = SeparatorChecker()

    # Store all the tokens and lexemes as tuples in a list
    tokens_and_lexemes = []
    
    while char_pointer < length:
        current_char = content[char_pointer]
        if starting:
            while current_char.isspace() and char_pointer != len(content) - 1:
                char_pointer += 1
                current_char = content[char_pointer]
                index_of_first_char_of_lexeme = char_pointer
            starting = False
        if current_char == "[" and char_pointer + 1 < length and content[char_pointer + 1] == "*":
            in_comment = True
            char_pointer += 2
            current_char = content[char_pointer]
            continue
        elif current_char == "*" and char_pointer + 1 < length and content[char_pointer + 1] == "]":
            in_comment = False
            char_pointer += 2
            index_of_first_char_of_lexeme = char_pointer
            starting = True
            continue
        if in_comment:
            char_pointer += 1
            current_char = content[char_pointer]
            continue
        # while current_char.isspace() and char_pointer != len(content) - 1 :
        #         char_pointer = char_pointer + 1
        #         current_char = content[char_pointer]
        #         index_of_first_char_of_lexeme = char_pointer
        # Check each FSM
        # Feed the current character to each FSM
        #print(current_char)
        
        operator_check = operator_checker.process_char(current_char)
        keyword_check = keyword_checker.validate_keyword(current_char)
        separator_check = separator_checker.validate_separator(current_char)
        id_current_state, id_input_char_terminates_token = identifier_fsm.validate_identifier(current_char)
        #print("id stuff", "state:", id_current_state, "terminates:", id_input_char_terminates_token)
        int_current_state, int_input_char_terminates_token = integer_fsm.validate_integer(current_char)
        #print("integer stuff", "state:", int_current_state, "terminates:", int_input_char_terminates_token)
        real_current_state, real_input_char_terminates_token = real_fsm.validate_real(current_char)
        #print("real stuff", "state:", real_current_state, "terminates:", real_input_char_terminates_token)


        # Check if input char terminates token and it is an accepting state

        if (
            (operator_check) or (keyword_check) or (separator_check) or 
            (id_input_char_terminates_token and id_current_state) or
            (int_input_char_terminates_token and int_current_state) or
            (real_input_char_terminates_token and real_current_state) or 
            (not operator_check and not keyword_check and not separator_check and
             not id_current_state and not real_current_state and not int_current_state and not current_char.isspace())
        ):
            # Isolate the token and lexeme
            token = ""
            lexeme = ""

            if operator_check:
                isTwoChar = determineTwoCharOperator(content, char_pointer)
                token = "Operator"
                if isTwoChar:
                    char_pointer += 2
                else:
                    char_pointer += 1
                current_char = content[char_pointer]

            elif keyword_check:
                token = "Keyword"
                char_pointer += 1
                current_char = content[char_pointer]
            elif separator_check:
                token = "Separator"
                char_pointer += 1
                current_char = content[char_pointer]


            elif int_input_char_terminates_token and int_current_state:
                token = "Integer"
                            
            elif id_input_char_terminates_token and id_current_state:
                token = "Identifier"

            elif real_input_char_terminates_token and real_current_state:
                token = "Real"
            
            elif (not operator_check and not keyword_check and not separator_check and
                not id_current_state and not real_current_state and not int_current_state and not current_char.isspace()):
                token = "Invalid"
                lexeme = ""

                while (
                    char_pointer < length and
                    (not operator_checker.process_char(current_char) and
                    not keyword_checker.validate_keyword(current_char) and
                    not separator_checker.validate_separator(current_char) and
                    not identifier_fsm.validate_identifier(current_char)[0] and
                    not integer_fsm.validate_integer(current_char)[0] and
                    not real_fsm.validate_real(current_char)[0] and
                    not current_char.isspace())
                ):
                    char_pointer += 1
                    current_char = content[char_pointer]
                
            lexeme = content[index_of_first_char_of_lexeme : char_pointer]


            tokens_and_lexemes.append((token, lexeme))

            # Move the char pointer to the next character if there is white space
            while current_char.isspace() and char_pointer != len(content) - 1:
                char_pointer += 1
                current_char = content[char_pointer]

            index_of_first_char_of_lexeme = char_pointer
        
            # print("make new instance")
            char_pointer -= 1 # Maybe have to put an if statement here later
            identifier_fsm = IdentifierFSM()
            integer_fsm = IntegerFSM()
            real_fsm = RealLexer()
            operator_checker = OperatorChecker()
            keyword_checker = KeywordChecker()
            separator_checker = SeparatorChecker()

            isTwoChar = False
        char_pointer += 1
    return tokens_and_lexemes

def write_to_output(tokens_and_lexemes, output_file_path):
    with open(output_file_path, 'w') as output_file:
        output_file.write("Token".ljust(17) + "Lexeme\n")
        output_file.write("-" * 30 + "\n")
        for token, lexeme in tokens_and_lexemes:
            output_file.write(f"{token.ljust(12)} | {lexeme}\n")

if __name__ == "__main__":
    with open('./input.txt', 'r') as file:
        content = file.read()

    result = lexer(content)
    output_file_path = './output.txt'
    write_to_output(result, output_file_path)

    print(f"Results written to {output_file_path}")

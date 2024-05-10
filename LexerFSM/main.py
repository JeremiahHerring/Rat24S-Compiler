from IdentifierLexer import IdentifierFSM
from IntegerLexer import IntegerFSM
from RealLexer import RealLexer
from Operator import OperatorChecker
from Keywords import KeywordChecker
from Separator import SeparatorChecker
from Production_Functions import syntax_analyzer

# this function helps determine if the operator has two characters in it because there are some with multiple
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

# this is the main lexer function that prints the token type and lexeme to the output files
def lexer(content):
    starting = True
    content += " "
    char_pointer = 0
    index_of_first_char_of_lexeme = 0
    length = len(content)
    isTwoChar = False
    in_comment = False

    # creates instances of each class so we have access the the finite state machines
    identifier_fsm = IdentifierFSM()
    integer_fsm = IntegerFSM()
    real_fsm = RealLexer()
    operator_checker = OperatorChecker()
    keyword_checker = KeywordChecker()
    separator_checker = SeparatorChecker()

    # Store all the tokens and lexemes as tuples in a list
    tokens_and_lexemes = []
    
    # loops over each character in the file
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
        
        # all of our validate functions are run here giving us the state of each fsm and if the input character terminates the token
        operator_check = operator_checker.process_char(current_char)
        keyword_check = keyword_checker.validate_keyword(current_char)
        separator_check = separator_checker.validate_separator(current_char)
        id_current_state, id_input_char_terminates_token = identifier_fsm.validate_identifier(current_char)
        int_current_state, int_input_char_terminates_token = integer_fsm.validate_integer(current_char)
        real_current_state, real_input_char_terminates_token = real_fsm.validate_real(current_char)

        if current_char == ".":
            test_pointer = char_pointer + 1
            while not real_input_char_terminates_token and test_pointer != len(content) - 1:
                state, term = real_fsm.validate_real(content[test_pointer])
                if state and term:
                    char_pointer = test_pointer + 1
                    real_current_state = state
                    real_input_char_terminates_token = term
                test_pointer += 1

        if current_char == "!":
            isTwoChar = False
            current_char = content[char_pointer]
            if char_pointer + 1 != len(content) and content[char_pointer + 1] == "=":
                isTwoChar = True
                operator_check = True
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

            # all of the following code in this if else chain checks to see what token type was selected
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
                char_pointer -= 1
            # this is responsible for illegal character detection
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
            
            # get the lexeme based off of the index of the first character and the current character pointer
            lexeme = content[index_of_first_char_of_lexeme : char_pointer]
            tokens_and_lexemes.append((token, lexeme))

            # Move the char pointer to the next character if there is white space
            while current_char.isspace() and char_pointer != len(content) - 1:
                char_pointer += 1
                current_char = content[char_pointer]

            # reset the character of the pointer for the next token
            index_of_first_char_of_lexeme = char_pointer
        
            # decriment the pointer to analyze the next token
            char_pointer -= 1

            # reset the finite state machines so they can track the correct values
            identifier_fsm = IdentifierFSM()
            integer_fsm = IntegerFSM()
            real_fsm = RealLexer()
            operator_checker = OperatorChecker()
            keyword_checker = KeywordChecker()
            separator_checker = SeparatorChecker()

            isTwoChar = False
        
        # go to the next character after each loop iteration
        char_pointer += 1
    return tokens_and_lexemes
    
# given a path to an output file, print all of the token types and lexemes in a nice format
def write_to_output(tokens_and_lexemes, syntax_result, result_str, output_file_path):
    with open(output_file_path, 'w') as output_file:
        # output_file.write("Token".ljust(17) + "Lexeme\n")
        # output_file.write("-" * 30 + "\n")
        # for token, lexeme in tokens_and_lexemes:
        #     output_file.write(f"{token.ljust(12)} | {lexeme}\n")

        # output_file.write("\nSyntax Analysis:\n")
        # output_file.write("-" * 30 + "\n")
        # output_file.write(syntax_result)
        # output_file.write("-" * 30 + "\n")
        output_file.write(result_str)



# main function that runs the input -> output code
if __name__ == "__main__":
    for i in range(1, 4):
        with open(f'./input/input{i}.txt', 'r') as file:
            content = file.read()

        result = lexer(content)
        output_file_path = f'./output/output{i}.txt'
        
        with open(output_file_path, 'w') as output_file:
            syntax_result, result_str = syntax_analyzer(result, 0)
            write_to_output(result, syntax_result, result_str, output_file_path)

        print(f"Results written to {output_file_path}")
from Separator import separators
from Operator import operators

class IdentifierFSM:
    def __init__(self):
        self.states = {'1', '2', '3', '4', '5', '6'}
        self.starting_state = '1'
        self.current_state = self.starting_state
        self.prev_state = ''
        self.accepting_states = {'2', '4', '5', '6'}
        self.transition_table = {
            ('1', 'letter'): '2',
            ('1', 'digit'): '3',
            ('1', '_'): '3',
            ('2', 'letter'): '4',
            ('2', 'digit'): '5',
            ('2', '_'): '6',
            ('3', 'letter'): '3',
            ('3', 'digit'): '3',
            ('3', '_'): '3',
            ('4', 'letter'): '4',
            ('4', 'digit'): '5',
            ('4', '_'): '6',
            ('5', 'letter'): '4',
            ('5', 'digit'): '5',
            ('5', '_'): '6',
            ('6', 'letter'): '4',
            ('6', 'digit'): '5',
            ('6', '_'): '6',
        }

    def process_input(self, char):
        if char.isalpha():
            return 'letter'
        elif char.isdigit():
            return 'digit'
        elif char == '_':
            return '_'
        else:
            return None

    def process_char(self, char):
        self.prev_state = self.current_state
        input_type = self.process_input(char)
        if input_type is None:
            self.current_state = '3'
        elif (self.current_state, input_type) in self.transition_table:
            self.current_state = self.transition_table[(self.current_state, input_type)]
        else:
            self.current_state = '3'

        input_char_terminates_token = (
            char in separators or char in operators or char.isspace()
        ) and self.current_state not in self.accepting_states

        return input_char_terminates_token, self.current_state

    def validate_identifier(self, identifier):
        input_char_terminates_token = False
        prev_accepting_state = self.starting_state

        for char in identifier:
            terminates_token, current_state = self.process_char(char)

            if terminates_token:
                input_char_terminates_token = True

            if current_state in self.accepting_states:
                prev_accepting_state = current_state

        is_valid = current_state in self.accepting_states
        
        #print("inside of id lexer:", self.prev_state in self.accepting_states)
        return is_valid if not input_char_terminates_token else self.prev_state in self.accepting_states, input_char_terminates_token

if __name__ == "__main__":
    identifier_fsm = IdentifierFSM()

    identifier = "+abc"
    
    for char in identifier:
        is_valid, input_char_terminates_token = identifier_fsm.validate_identifier(char)
        print(f"Char: {char}, Is Valid: {is_valid}, Terminates Token: {input_char_terminates_token}")

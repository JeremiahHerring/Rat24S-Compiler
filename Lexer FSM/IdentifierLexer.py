from Keywords import keywords
class IdentifierFSM:
    def __init__(self):
        self.states = {'1', '2', '3', '4', '5', '6'} # Initialize three states
        self.starting_state = '1' 
        self.current_state = ''
        self.accepting_states = {'2', '4', '5', '6'}
        self.transition_table = {
            ('1', 'letter') : '2',
            ('1', 'digit') : '3',
            ('1', '_') : '3',
            ('2', 'letter') : '4',
            ('2', 'digit') : '5',
            ('2', '_') : '6',
            ('3', 'letter') : '3',
            ('3', 'digit') : '3',
            ('3', '_') : '3',
            ('4', 'letter') : '4',
            ('4', 'digit') : '5',
            ('4', '_') : '6',
            ('5', 'letter') : '4',
            ('5', 'digit') : '5',
            ('5', '_') : '6',
            ('6', 'letter') : '4',
            ('6', 'digit') : '5',
            ('6', '_') : '6',
        }

    # Function to process input
    def process_input(self, char):
        if char.isalpha():
            return 'letter'
        elif char.isdigit():
            return 'digit'
        elif char == '_':
            return '_'
        else:
            return None

    # Function to validate or invalidate identifier
    def validate_identifier(self, identifier):
        # First check if the identifier is a keyword
        if identifier in keywords:
            return False
        self.current_state = self.starting_state # Have each identifier in the start position
        for char in identifier:
            input_type = self.process_input(char)
            if input_type is None:
                self.current_state = '3'
                break
            if (self.current_state, input_type) in self.transition_table:  # Check if char is valid for the state that it is in
                self.current_state = self.transition_table[(self.current_state, input_type)]   # Transition to state based on the input given
            else:
                self.current_state = '3'  # Not valid

        return self.current_state in self.accepting_states  # if current state is accept: return True else return False

if __name__ == "__main__":
    identifier_fsm = IdentifierFSM()

#     identifier = "helloWorld"

#     if identifier_fsm.validate_identifier(identifier):
#         print(f"{identifier} is a valid identifier")
#     else:
#         print(f"{identifier} is not a valid identifier")

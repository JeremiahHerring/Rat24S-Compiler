class IdentifierFSM:
    def __init__(self):
        self.states = {'start', 'accept', 'reject'} # Initialize three states
        self.current_state = 'start' 
        self.accepting_state = 'accept'
        self.transitions = {
            'start': {'letter': 'accept'}, # The identifier has to start with a letter
            'accept': {'letter': 'accept', 'digit': 'accept', '_': 'accept'}, # Every letter, digit, or _ after the first letter is accepted
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
        self.current_state = 'start' # Have each identifier in the start position
        for char in identifier:
            input_type = self.process_input(char)
            if input_type is None:
                self.current_state = 'reject'
                break
            if self.current_state in self.transitions and input_type in self.transitions[self.current_state]: # Check if char is valid for the state that it is in
                self.current_state = self.transitions[self.current_state][input_type] 
            else:
                self.current_state = 'reject'

        return self.current_state in self.accepting_state # if current state is accept: return True else return False

identifier_fsm = IdentifierFSM()










# USED FOR TESTING (REMEMBER TO DELETE BEFORE SUBMITTING)
identifier = "PEEINMYMOUTH"

if identifier_fsm.validate_identifier(identifier):
    print(f"{identifier} is a valid identifier")
else:
    print(f"{identifier} is not a valid identifier")

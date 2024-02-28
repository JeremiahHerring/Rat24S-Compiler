class IntegerFSM:
    def __init__(self):
        self.states = {'1', '2'}
        self.starting_state = '1'
        self.current_state = ''
        self.accepting_state = '2'
        self.transition_table = {
            ('1', 'digit') : '2',
            ('2', 'digit') : '2'
        }
    
    def process_input(self, char):
        if char.isdigit():
            return 'digit'
        else:
            return None
        
    def validate_integer(self, integer):
        self.current_state = self.starting_state
        for digit in integer:
            input_type = self.process_input(digit)
            if self.process_input(digit) is None:
                self.current_state = 'reject'
                break
            if (self.current_state, input_type) in self.transition_table:
                self.current_state = self.transition_table[(self.accepting_state, input_type)]
            else:
                self.current_state = 'reject'
        
        return self.current_state in self.accepting_state
    
integer_fsm = IntegerFSM()

# USED FOR TESTING (REMEMBER TO DELETE BEFORE SUBMITTING)
integer = ""

if integer_fsm.validate_integer(integer):
    print(f"{integer} is a valid integer")
else:
    print(f"{integer} is not a valid integer")

        

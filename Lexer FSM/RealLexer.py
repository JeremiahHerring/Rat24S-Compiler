class RealLexer:
    def __init__(self):
        self.states = {'1', '2', '3', '4'}
        self.alphabet = {'digit', '.'}
        self.start_state = '1'
        self.accepting_state = '4'
        self.current_state = ''
        self.transition_table = {
            ('1', 'digit'): '2',
            ('2', 'digit'): '2',
            ('2', '.'): '3',
            ('3', 'digit'): '4',
            ('4', 'digit'): '4',
        }
    
    # identify char
    def process_input(self, char):
        if char.isdigit():
            return 'digit'
        elif char == '.':
            return '.'
        else:
            return None

    # Function to validate or invalidate real number
    def validate_real(self, inputStr):
        self.current_state = self.start_state
        for char in inputStr:
            input_type = self.process_input(char)
            if input_type is None:
                self.current_state = 'reject'
                break
            if (self.current_state, input_type) in self.transition_table:
                self.current_state = self.transition_table[(self.current_state, input_type)]
            else:
                self.current_state = 'reject'

        return self.current_state in self.accepting_state # if current state is accept: return True else return False

if __name__ == "__main__":
    lexerInstance = RealLexer()
#     tests = ["234.234","234.",".2","2.a", "a.2", ".", "2", "a"]

#     for test in tests:
#         if lexerInstance.validate_real(test):
#             print(f"{test} is a valid real number")
#         else:
#             print(f"{test} is not a valid real number")


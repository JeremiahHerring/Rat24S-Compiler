# Operator List
operators = {"==", "!=", ">", "<", "<=", "=>", "*", "/", "+", "-", "="}
class OperatorChecker:
    # Initializes operator buffer that we append chars to 
    def __init__(self):
        self.operator_buffer = ""

    # Finds if operator is in operator list
    def process_char(self, char):
        self.operator_buffer += char

        if self.operator_buffer in operators:
            return True

        if len(self.operator_buffer) == 2:
            return self.operator_buffer in operators
        else:
            return False

if __name__ == "__main__":
    operator_checker = OperatorChecker()

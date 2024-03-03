class OperatorChecker:
    def __init__(self):
        self.operators = {"==", "!=", ">", "<", "<=", "=>", "*", "/", "+", "-"}
        self.operator_buffer = ""

    def process_char(self, char):
        self.operator_buffer += char

        if self.operator_buffer in self.operators:
            return True

        if len(self.operator_buffer) == 2:
            return self.operator_buffer in self.operators
        else:
            return False

if __name__ == "__main__":
    operator_checker = OperatorChecker()
    input_str = ""

    for char in input_str:
        result = operator_checker.process_char(char)
        print(result)

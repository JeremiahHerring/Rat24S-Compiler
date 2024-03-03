separators = {';', ',', '(', ')', '{', '}', "$"}
class SeparatorChecker:
    def __init__(self):
        self.separator_buffer = ""

    def validate_separator(self, char):
        self.separator_buffer += char

        if self.separator_buffer in separators:
            return True
        return False

if __name__ == "__main__":
    separator_checker = SeparatorChecker()
    inputStr = ""

    for char in inputStr:
        result = separator_checker.validate_separator(char)
        print(result)

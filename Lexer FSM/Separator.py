separators = {';', ',', '(', ')', '{', '}', '[', ']'}
class SeparatorChecker:
    def validate_separator(self, char):
        if char in separators:
            return True
        else:
            return False

    
if __name__ == "__main__":
    separator_checker = SeparatorChecker()
    inputStr = ","

    for char in inputStr:
        result = separator_checker.validate_separator(char)
        print(result)

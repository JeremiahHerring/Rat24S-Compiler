# Separator List
separators = {';', ',', '(', ')', '{', '}', "$"}
class SeparatorChecker:
    # Initialize Separator buffer that we append chars to 
    def __init__(self):
        self.separator_buffer = ""

    # Determines if char is a valid separator or not
    def validate_separator(self, char):
        self.separator_buffer += char

        if self.separator_buffer in separators:
            return True
        return False

if __name__ == "__main__":
    separator_checker = SeparatorChecker()
 
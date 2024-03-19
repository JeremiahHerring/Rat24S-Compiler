# List of all possible keywords for RAT24
keywords = {
        'integer', 'if', 'else', 'endif', 'while',
        'return', 'scan', 'print', 'boolean', 'real',
        'function', 'true', 'false', 'endwhile'
        }
class KeywordChecker:
    # Initialize a keywordBuffer that we append chars to 
    def __init__(self):
        self.keywordBuffer = ""

    # Validates if a keyword is found or not
    def validate_keyword(self, char):
        self.keywordBuffer += char

        if self.keywordBuffer in keywords:
            return True
        else:
            return False

    
if __name__ == "__main__":
    keyword_checker = KeywordChecker()


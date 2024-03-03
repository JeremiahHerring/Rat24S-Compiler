class KeywordChecker:
    def __init__(self):
        self.keywords = {
        'integer', 'if', 'else', 'endif', 'while',
        'return', 'scan', 'print', 'boolean', 'real',
        'function', 'true', 'false'
        }
        self.keywordBuffer = ""

    def validate_keyword(self, char):
        self.keywordBuffer += char

        if self.keywordBuffer in self.keywords:
            return True
        else:
            return False

    
if __name__ == "__main__":
    keyword_checker = KeywordChecker()
    inputStr = "scan"

    for char in inputStr:
        result = keyword_checker.validate_keyword(char)
        print(result)

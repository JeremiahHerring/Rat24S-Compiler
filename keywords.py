import re
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"{self.type:15} {self.value}"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.keywords = ['while']  # Extend this list with more keywords if necessary

    def next_token(self):
        if self.position >= len(self.text):
            return None  # End of file

        # Skip whitespace
        while self.position < len(self.text) and self.text[self.position].isspace():
            self.position += 1

        if self.position >= len(self.text):
            return None

        # Match keywords and identifiers
        if self.text[self.position].isalpha():
            word = re.match(r'\w+', self.text[self.position:]).group(0)
            self.position += len(word)
            if word in self.keywords:
                return Token("keyword", word)
            return Token("identifier", word)

        # Match integers
        if self.text[self.position].isdigit():
            num = re.match(r'\d+', self.text[self.position:]).group(0)
            self.position += len(num)
            return Token("integer", num)

        # Unrecognized token
        self.position += 1  # Move past the unrecognized character
        return self.next_token()  # Skip the unrecognized character

def main():
    input_text = "while 123 while234 567"
    lexer = Lexer(input_text)
    
    print(f"{'token':15} {'lexeme'}")
    while True:
        token = lexer.next_token()
        if not token:
            break
        print(token)

if __name__ == "__main__":
    main()



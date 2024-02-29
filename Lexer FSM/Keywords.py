keywords = {
    'integer', 'if', 'else', 'endif', 'while',
    'return', 'scan', 'print', 'boolean', 'real',
    'function', 'true', 'false'
    }

def validate_keyword(keyword):
    if keyword in keywords:
        return True
    return False

# testing
keyword = "while"
if validate_keyword(keyword):
    print(f"{keyword} is a keyword")
else:
    print(f"{keyword} is a not keyword")

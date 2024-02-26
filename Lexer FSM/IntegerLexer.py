def validate_integer(integer):
    return False if not isinstance(integer, int) else True


# Test the integer lexer 
x = 34
if validate_integer(x):
    print(f"{x} is a valid identifier")
else:
    print(f"{x} is not a valid identifier")


# Q

    

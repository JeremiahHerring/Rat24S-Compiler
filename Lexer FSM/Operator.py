operators = {"==", "!=", ">", "<", "<=", "=>", "*", "/", "+", "-"}

def validate_operator(operator):
    if operator in operators:
        return True
    return False
    
# testing
operator = "!="
if validate_operator(operator):
    print(f"{operator} is a operator")
else:
    print(f"{operator} is a not operator")

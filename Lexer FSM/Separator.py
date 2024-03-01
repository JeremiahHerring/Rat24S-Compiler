separators = {';', ',', '(', ')', '{', '}', '[', ']'}

def validate_separator(separator):
    if separator in separators:
        return True
    return False
    
# # testing
# separator = ","
# if validate_separator(separator):
#     print(f"{separator} is a separator")
# else:
#     print(f"{separator} is a not separator")

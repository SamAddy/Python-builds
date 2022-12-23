"""
Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.
"""

def double_letters(string):
    for i in range(len(string) - 1):
        if(string[i] == string[i + 1]):
            return True
    
    return False


print(double_letters('Hello'))

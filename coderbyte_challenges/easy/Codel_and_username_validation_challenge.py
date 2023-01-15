"""
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false. 
"""
import re


def codel_and_username_validation(strParam):
    # code goes here
    pattern = "^[A-Za-z0-9_]*$"
    passed = False

    for i in range(len(strParam)):
        if len(strParam) > 4 and len(strParam) < 25:
            if strParam[0].isalpha():
                if bool(re.match(pattern, strParam)) and strParam[-1] != "_":
                    passed = True
                    
    
    return "true" if passed else "false"


expressions = {
    "b3333434_", # false
    "u__hello_world123",  # true
    "usernamehello123", # true
    "aaaaaaaaaa" # true
}

for strpar in expressions:
    print(f"{strpar} returns {codel_and_username_validation(strpar)}")



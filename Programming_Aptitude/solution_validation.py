"""
Solution validation

The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too hard.

Write a function named validate that takes code represented as a string as its only parameter.

Your function should check a few things:

    the code must contain the def keyword
        otherwise return "missing def"
    the code must contain the : symbol
        otherwise return "missing :"
    the code must contain ( and ) for the parameter list
        otherwise return "missing paren"
    the code must not contain ()
        otherwise return "missing param"
    the code must contain four spaces for indentation
        otherwise return "missing indent"
    the code must contain validate
        otherwise return "wrong name"
    the code must contain a return statement
        otherwise return "missing return"

If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.
"""

def validate(string):
    param = "()"
    open_para = "("
    closed_para = ")"
    if "def" not in string:
        return "missing def"
    elif ":" not in string:
        return "missing :"
    elif open_para not in string and closed_para not in string:
        return "missing paren"
    elif "def" in string and string.index("def") == string.index("("):
        return "missing param"
    elif "    " not in string:
        return "missing indent"
    elif "validate" not in string:
        return "wrong name"
    elif "return" not in string:
        return "missing return"
    else:
        return True

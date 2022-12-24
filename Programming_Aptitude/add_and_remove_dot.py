"""
Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".
"""

def add_dots(string):
    # Joining with "." 
    return ".".join(string)


def remove_dots(string):
    # replace all instances of "." with ""
    return string.replace(".", "")


string = "Python"
print(add_dots(string))
print(remove_dots(add_dots(string)))

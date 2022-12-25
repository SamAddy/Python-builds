"""
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.
"""
def triple_and(x, y, z):
    return x and y and z


print(triple_and(True, True, False))

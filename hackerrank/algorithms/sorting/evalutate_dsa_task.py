def evaluate(string):
    operations = ['+', '-', '*', '/']
    vals = []

    # Iterate though the string
    for char in string.split():
        if char in operations:
            # Get top two values
            val1 = vals.pop()
            val2 = vals.pop()

            if char == '+':
                vals.append(val2 + val1)
            elif char == '*':
                vals.append(val2 * val1)
            elif char == '/':
                vals.append(val2 / val1)
            elif char == '-':
                vals.append(val2 - val1)
        else:
            # Value to stack
            vals.append(int(char))

    return int(vals[0])


print(evaluate('5 5 +'))
print(evaluate('8 2 /'))
print(evaluate('5 4 *'))
print(evaluate('5 2 3 + *'))
print(evaluate('5 2 + 3 *'))
print(evaluate('1 2 3 4 + + +'))
print(evaluate('2 2 + 3 + 4 +'))

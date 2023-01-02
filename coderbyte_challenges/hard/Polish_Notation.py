"""
Polish notation, also known as prefix notation, is a way of writing mathematical expressions in which the operator is
placed before the operands. In contrast to infix notation, which is the most common way of writing mathematical
expressions (e.g. 2 + 3), the operator in Polish notation is not bound to the operands with parentheses or other symbols

For example, the expression 2 + 3 can be written in Polish notation as + 2 3. In this notation, the operator + is
placed before the operands 2 and 3.
"""


def evaluate_expression(expression: str) -> int:
    """Evaluate a mathematical expression in Polish notation (prefix notation)."""
    # Split the expression into a list of tokens
    tokens = expression.split()

    # Define a stack to hold the operands
    stack = []

    # Iterate over the tokens
    for token in tokens:
        # If the token is an operand, convert it to an integer and push it onto the stack
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        # If the token is an operator and the stack has at least two operands,
        # pop the last two operands from the stack, apply the operator,
        # and push the result back onto the stack
        if len(stack) >= 2:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == "+":
                result = operand1 + operand2
            elif token == "-":
                result = operand1 - operand2
            elif token == "*":
                result = operand1 * operand2
            else:
                result = operand1 / operand2
            stack.append(result)
        # If the token is an operator but the stack has fewer than two operands,
        # raise a ValueError
       # else:
           # raise ValueError("Invalid expression: not enough operands")

    # The final result should be the only element on the stack
    return stack[0]


# Define a few test expressions in Polish notation
expressions = [
    "+ 2 3",
    "* + 2 3 4",
    "/ - * + 2 3 4 5 6",
    "* - + 1 2 3 4 5",
]

# Evaluate each expression and print the result
for expression in expressions:
    result = evaluate_expression(expression)
    print(f"{expression} = {result}")

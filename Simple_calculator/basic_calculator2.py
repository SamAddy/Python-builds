 # A basic calculator

def calculator(num1, operator, num2):
    """
    This function takes in the parameters and calculate the resulting value based on the provided operator.

    Parameters:
    num1 (int) -- first number 
    num2 (int) -- second number
    operator (str) -- the operation to be perfomed

    Retruns:
    int -- the program returns the results based on the operator provided

    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid operator"

# Read the user's input as string
input_str = input("Enter a calculation (e.g. 4 - 2): ")

# split the input string into the operands and operator
values = input_str.split(" ")
num1 = int(values[0])
operator = values[1]
num2 = int(values[2])

# print out result by calling calculator function
print(calculator(num1, operator, num2))

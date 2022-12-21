
class Calculator:
    """
    This class contains all possible methods for the calculator
    
    classes:
    add
    subtract
    multiply 
    divide

    parameters:
    x -- for first number
    y -- for second number
    """

    def add(self, x, y):
        """
        This function adds the two integers provided in the parameter and returns the results

        Parameters:
        x -- int for first integers
        y -- int for second integers

        Returns:
        int: the sum of x and y.

        Example:
        add(9, 3)
        12
        """
        return x + y

    def subtract(self, x, y):
        """
        This function subtracts the secondnumber from the first number provided in the parameter and returns the results

        Parameters:
        x -- int for first number to be subtracted from
        y -  second number to subtract

        Example:
        subtract(9, 3)
        6
        """
        return x - y

    def multiply(self, x, y):
        """
        This function multiplies the two integers in the parameter

        Parameters:
        x(int) -- the first integer to be multiplied
        y(int) -- second integer to be multiplied by the first integer
        
        Returns:
        int - it returns the multiplication of x and y

        Example:
        multiply(9, 3)
        27
        """
        return x * y

    def divide(self, x, y):
        """
        This function divides the first number by the second number and returns the results

        Parameters:
        x(int) -- the first number serving as numerator 
        y(int) -- second number serving as denominator 

        Returns:
        int- division of x by y

        Example:
        divide(9, 3)
        3
        """
        return int(x / y)

# create an instance of the calculator class
calculator = Calculator()



x = 9
y = 3

print(calculator.add(x, y))
print(calculator.subtract(x, y))
print(calculator.multiply(x, y))
print(calculator.divide(x, y))

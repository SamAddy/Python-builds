
def FirstFactorial(num):
    # If num is 0 or 1, return 1
    if num in [0, 1]:
        return 1
    # Otherwise, return the product of num and the factorial of num - 1
    return num * FirstFactorial(num - 1)


print(FirstFactorial(4))

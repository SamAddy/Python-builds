"""
Have the function Stringchallenge (str) read str which will be a string of roman numerals in decreasing order. The numerals being used are: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and M for 1000. Your program should return the same number given by str using a smaller set of roman numerals. For example: if str is
LLLXXXVVIV" this is 200, so your program should return CC because this is the shortest way to write 200 using the roman numeral system given above.
If a string is given in its shortest form, just return that same string.
Look more into dictionary
"""


def string_challenge(param):
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0

    for i in range(len(param)):
        result += roman_numerals[param[i]]

    return result


def to_roman(num):
    # Create a list of roman numerals
    roman_numerals = ['M', 'CM', 'D', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    # Create a list of matching int values to the numerals
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    result = ''
    # Iterate through the values and roman numerals
    for roman, value in zip(roman_numerals, values):
        # While the number is greater than or equal to the value, add the roman numeral to the result and subtract
        # the value
        while num >= value:
            result += roman
            num -= value
    # Return the result
    return result


# print(string_challenge("XXXVVIIIIIIIIII"))
# print(string_challenge("LLLXXXVVVV"))
print(string_challenge("L"))

print(to_roman(200))
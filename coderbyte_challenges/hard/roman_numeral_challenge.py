"""
Have the function string_challenge (str) read str which will be a string of roman numerals in decreasing order.
The numerals being used are: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and M for 1000. 
Your program should return the same number given by str using a smaller set of roman numerals. For example: if str is
"LLLXXXVVIV" this is 200, so your program should return CC because this is the shortest way to write 200 using the roman 
numeral system given above. If a string is given in its shortest form, just return that same string.

"""


def string_challenge(param):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    # Store the result of the roman numerals
    num = 0
    # Iterate through characters
    for i, ch in enumerate(param):
        value = roman_numerals[ch]
        if i + 1 < len(param) and roman_numerals[param[i + 1]] > value:
            num -= value
        else:
            num += value

    # Convert the number to a roman numeral string
    result = ''
    # Create a list of roman numeral strings
    roman_numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    # Create a list of integer values
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    # Iterate over the values and roman numerals
    for roman, value in zip(roman_numerals, values):
        # While the number is greater than or equal to the value, add the roman numeral to the result and
        # subtract the value
        while num >= value:
            result += roman
            num -= value
    # Return the result
    return result


print(string_challenge("LLLXXXVVVV"))
print((string_challenge('XXXVVIIIIIIIIII')))
print((string_challenge('DDLL')))

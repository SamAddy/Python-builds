import random

def count_lines(filename):
    """
     This a program which reads a file and counts the number of line in the file

     Parameters: 
     filename (str) - the file to be processed

     Returns:
     int: The number of lines in the file

    """
    # open and read CSV file
    with open(filename, "r") as file:
        # Use a generator expression to count the number of lines in the file
        # This avoids loading the entire file into memory at once
        line_count = sum(1 for _ in file)

    return line_count


def generate_text(length):
    """
    Generates random test of a given length.

    Parameters:
    length (int) -- the length of text to generate.

    Returns: 
    str: The generated text.
    """
    # Define a list of possible characters to use in the text
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

    # Use a list comprehension to generrate a list of random characters
    text = "".join(random.choice(characters) for _ in range(length))

    return text

# Generate random text of length 1000
text = generate_text(1000)

# Write teh text to a file which will be later passed to count_lines() function
with open("random.txt", "w") as file:
    file.write(text)

# Testing the function with the random file generated.
line_count = count_lines("random.txt" )
print(f"Number of lines: {line_count}")

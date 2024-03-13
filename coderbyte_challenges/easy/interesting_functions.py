import collections


def ask_ok(prompt, retries=4, reminder='Please try again! '):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# Lambda Expressions
def make_increment(n):
    return lambda x: x + n


f = make_increment(60)
print(f(5))

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

ask_ok("Do you really want to end the game? ")
ask_ok('OK to overwrite the file? ', 2)
ask_ok('OK to overwrite the file? ', 2, 'Come on, only yes or no!')


# test input question
class TextInput:
    def __init__(self):
        self.character = ""

    def add(self, character):
        self.character += character

    def get_value(self):
        return self.character


class NumericInput(TextInput):
    def add(self, character):
        if character.isnumeric():
            self.character += character


if __name__ == '__main':
    input = NumericInput()
    input.add("1")
    input.add("*")
    input.add("0")
    print(input.get_value())  # Output: "10"


def simulate(entries):
    """
    :param entries: (list(int)) The numerical record files
    :returns: (list(int)) The record files after running the malware
    """
    result = entries
    t2 = 4
    t1 = 3
    for val in range(len(result)):
        if (val - t1) < 3:
          if result[val] <= result[val + t2]:
              result[val] = 0
        if (val - t1) > 3 and (val + t2) <= len(result) -1:
            if result[val] <= result[val - t1] | result[val] >= result[val + t2]:
                result[val] = 0
        # elif (val - t1) > 3 and (val + t2) in range(len(result)):
        #     if result[val] <= result[val - t1]:
        #         result[val] = 0
        # else:
        #     if ((val - t1) >= 0) and (val + t2) in range(len(result)):
        #         result[val] = 0
    # Write your code here
    return result


records = [1, 2, 0, 5, 0, 2, 4, 3, 3, 3]
print(simulate(records))
# Expected output
# [1, 0, 0, 5, 0, 0, 0, 3, 3, 0]

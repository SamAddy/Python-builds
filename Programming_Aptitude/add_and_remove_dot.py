
def add_dots(string):
    results = ""
    for i in range(len(string)):
        results.append(string[i] + ".")

    return results


print(add_dots("test"))

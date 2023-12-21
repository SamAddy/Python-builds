# import string
#
# text = 'BANANA'
#
# vowels = set('AEIOU')
# consonants = set(string.ascii_uppercase) - vowels
# persons = {'Stuart': 0, 'Kevin': 0}
#
#
# oneliner = list(set(text[i:j] for i in range(len(text)) for j in range(i+1, len(text) + 1)))
#
# for s in oneliner:
#     counter = text.count(s)
#     if s[0] in vowels:
#         persons['Kevin']+= counter
#     elif s[0] in consonants:
#         persons['Stuart'] += counter
#
# if persons['Stuart'] == persons['Kevin']:
#     print('Draw')
# elif persons['Stuart'] > persons['Kevin']:
#     print(f"Stuart {persons['Stuart']}")
# else:
#     print(f"Kevin {persons['Kevin']}")
#
# print(oneliner, len(oneliner))
#
# print(persons)
# max_score = max(persons.values())


# ------ Best solution -------------------------

def minion_game(text):
    # your code goes here
    persons = {'Stuart': 0, 'Kevin': 0}
    # all_words = list(set(text[i:j] for i in range(len(text)) for j in range(i+1, len(text) + 1)))

    vowels = set('AEIOU')

    for i in range(len(text)):
        if text[i].upper() in vowels:
            persons['Kevin'] += len(text) - i
        else:
            persons['Stuart'] += len(text) - i

    if persons['Stuart'] == persons['Kevin']:
        print('Draw')
    elif persons['Stuart'] > persons['Kevin']:
        print(f"Stuart {persons['Stuart']}")
    else:
        print(f"Kevin {persons['Kevin']}")


if __name__ == '__main__':
    s = input()
    minion_game(s)

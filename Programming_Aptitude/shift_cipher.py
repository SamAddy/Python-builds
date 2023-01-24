def decrypt_shift_cipher(cryptotext, key):
    plaintext = ""
    for c in cryptotext:
        if c.isalpha():
            plaintext += chr((ord(c) - key - ord('a')) % 26 + ord('a'))
        else:
            plaintext += c
    return key, plaintext


def count_characters(cryptotext):
    alphabets = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }

    for ch in cryptotext.lower():
        if ch in alphabets:
            alphabets[ch] += 1

    return {key: value for key, value in alphabets.items() if value > 0}


cryptotext1 = "exdei ecued uxqih uluqb utcoi ushuj qdtco fbqdi qhuve ybut"
cryptotext2 = "cvksx nktau rvqvc pxnkx ulxpp dhxpj rumvz ubxtj xzpxc kxfzx qnrxp vcgxu uxkp"
key = 26

# for i in range(key):
#    print(decrypt_shift_cipher(cryptotext, i))


#print(decrypt_shift_cipher(cryptotext, 16))

print(count_characters(cryptotext1))


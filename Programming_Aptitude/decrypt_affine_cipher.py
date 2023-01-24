def decrypt_affine(cryptotext):
    for a in range(1, 26):
        for b in range(0, 26):
            if (a * a % 26 == 1):
                plaintext = ""
                for c in cryptotext:
                    if c.isalpha():
                        plaintext += chr(((ord(c) - ord('a') - b) * a % 26) + ord('a'))
                    else:
                        plaintext += c
                print("a:", a, "b:", b, "plaintext:", plaintext)
                

cryptotext = "cvksx nktau rvqvc pxnkx ulxpp dhxpj rumvz ubxtj xzpxc kxfzx qnrxp vcgxu uxkp"
decrypt_affine(cryptotext)

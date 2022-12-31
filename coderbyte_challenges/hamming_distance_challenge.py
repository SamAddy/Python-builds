"""
Have the function ArrayChallenge (strArr)
take the array of strings stored in strArr, which will only contain two strings of equal length and return the Hamming distance between them. The Hamming distance is the number of positions where the corresponding characters are different.
For example: if strArr is ['coder', "codec'] then your program should return 1. The string will always be of equal length and will only contain lowercase characters from the alphabet and numbers.
"""

def ArrayChallenge(strArr):
    # store hamming distance
    hamming_distance = 0
    
    # itereate through the characters in  strArr
    for i in range(len(strArr[0])):
        # check if teh characters are different and increase hamming_distance counter by 1
        if strArr[0][i] != strArr[1][i]:
            hamming_distance += 1

    # return the Hamming distance
    return hamming_distance

strArr = ['Coder', 'Codec']
print(ArrayChallenge(['10100', '10011']))
print(ArrayChallenge(strArr))


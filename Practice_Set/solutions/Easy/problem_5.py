# read file using file i/o , display number of words , characters , lines , alphabets , digits , special characters, spaces , vowels , consonants , 

def isvowel(char):
    return char.lower() in ['a','e','i','o','u']
# print(isvowel("a"))

def isconsonant(char):
    return char.isalpha() and not isvowel(char)
# print(isconsonant("a"))

def isSpecial(char):
    return not char.isalpha() and not char.isdigit() and not char.isspace()
# print(isSpecial(" "))

def count_lines(data):
    count = 0
    for i in data:
        if i == "\n":
            count += 1
    return count

with open("test.txt","r") as file:
    data = file.read()
    print("file content : \n",data)
    print()
    print("Data Analysis :")
    print("number of words :",len(data.split(" ")))
    print("number of characters:",len(data))
    print("number of Lines:",count_lines(data))
    alpha = 0
    digit = 0
    special = 0
    space = 0
    vowel = 0
    consonant = 0
    for i in data:
        # print(i)
        if i.isalpha():
            alpha += 1
        elif i.isdigit():
            digit += 1
        elif i.isspace():
            space += 1
        if isvowel(i):
            vowel += 1
        elif isconsonant(i):
            consonant += 1
        elif isSpecial(i):
            special += 1
    print("number of alphabets:",alpha)
    print("number of Digits:",digit)
    print("number of special characters:",special)
    print("number of spaces:",space)
    print("number of vowels:",vowel)
    print("number of consonants:",consonant)


    
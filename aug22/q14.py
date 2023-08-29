def validator(letter):
    checker = ""
    vowels = ('a', 'e', 'i', 'o', 'u')
    for element in vowels:
        if str.upper(element) == str.upper(letter):
            checker = 'true'
            break
        else:
            checker = 'false'
    print(checker)


validator('z')

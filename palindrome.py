string1 = 'ada'
string2 = 'java'


def palindrome(string):
    string3 = string[::-1]
    if string == string3:
        print("The letter is a palindrome")
    else:
        print("The letter is not a palindrome")


palindrome(string1)
palindrome(string2)

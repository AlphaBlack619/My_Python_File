word1 = input('What your Problem?: ')
word2 = input('Have you had this problem before? ("Yes" OR "No")')
if word2.capitalize() == "Yes":
    print("Well, You Have Its Again")
elif word2.capitalize() == "No":
    print("Well, You Have Its Now")

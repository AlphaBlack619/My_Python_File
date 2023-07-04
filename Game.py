import random
Name = input("Wellcome to Nero Casino\nWhat Your Name?: \n")
print(Name, " Are You Ready To Make Some Money\nEnter The Winning Number To Win")
counter = 0
while counter < 10:
    counter = counter + 1
    number = random.randint(1, 100)
    game = int(input("Guess The Winning Number\n"))
    if game == number:
        print('You Won $1,000,000!')
        exit()
    elif counter == 1 and game != number:
        print('You Still Have 9 More Chance')
    elif counter == 2 and game != number:
        print('Sorry Try Again 8 Chances Left')
    elif counter == 3 and game != number:
        print('Sorry Try Again 7 Chances Left')
    elif counter == 4 and game != number:
        print('Sorry Try Again 6 Chances Left')
    elif counter == 5 and game != number:
        print('Sorry Try Again')
        print("Five Chances Remaining")
    elif counter == 6 and game != number:
        print('Sorry 4 Shots Left')
    elif counter == 7 and game != number:
        print('3 More To Try')
    elif counter == 8 and game != number:
        print('Red Warning 2 Last Chances')
    elif counter == 9 and game != number:
        print('Last Chance')
    elif counter == 10 and game != number:
        print('Sorry You Lose! The Wining Number Is', number)
        
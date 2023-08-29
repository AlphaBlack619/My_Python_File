def checker1(creditcard_number):
    if not (char.isupper() for char in creditcard_number):
        print('Creditcard Number Must Be Digit')
    if len(creditcard_number) < 13 or len(creditcard_number) > 16:
        print('Invalid Card length')
    checker = 0
    for numbers in reversed(range(len(creditcard_number))):
        if numbers % 2 == 0:
            figure = int(creditcard_number[numbers])
            if figure < 5:
                checker += figure * 2
            if figure >= 5:
                temp = str(figure * 2)
                temp2 = int(temp[0]) + int(temp[1])
                checker += temp2
    for numbers2 in range(len(creditcard_number)):
        if numbers2 % 2 != 0:
            figure2 = int(creditcard_number[numbers2])
            checker += figure2
    return checker


def checker2(creditcard_number):
    type_status = "none"
    if creditcard_number[0] == "4":
        type_status = "Visa Card"
    elif creditcard_number[0] == '5':
        type_status = 'Master Card'
    elif creditcard_number[0] == '6':
        type_status = 'Discover Card'
    elif creditcard_number[0] == '3' and creditcard_number[1] == '7':
        type_status = 'American Express Card'
    else:
        type_status = 'Invalid Card Type'
    return type_status


def checker3():
    creditcard_number = input("Hello, Kindly Enter Card To verify: ")
    valid_type = ''
    if checker1(creditcard_number) % 10 == 0:
        valid_type = 'Valid'
    else:
        valid_type = "Invalid"
    length = str(len(creditcard_number))
    print("**************************************************************************\n" +
          "************** Credit Card Type: " + checker2(creditcard_number) + "\n" +
          "************** Credit Card Number: " + creditcard_number + "\n" +
          "************** Credit Card Digit Length: " + length + "\n" +
          "************** Credit Card Digit Validity Status: " + valid_type + "\n" +
          "**************************************************************************")


def creditcard_validator():
    checker3()


creditcard_validator()

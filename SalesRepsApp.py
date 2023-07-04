Item = int(input('Welcome To Alpha Shopping Mail...\nEnter Item Price: '))
A = Item * 0.1
Discount = Item - A
payment1 = Discount * 0.1
B = Item * 0.25
Discount1 = Item - B
PaymentOption = input('Your Debit is $%d\nEnter Select DisAccount Option A OR B: ' % Item)
if PaymentOption.lower() == 'a':
    print('Your discount price is %d' % Discount)
    price1 = int(input('please make a down payment of $%d or more sir: ' % payment1))
    if price1 >= payment1:
        print('Thanks for shopping with us\nTry and complete your payment')
    else:
        print('You are not serious sir')
        exit()
if PaymentOption.capitalize() == 'B':
    price2 = int(input('No Discount Price Sir Please Make A Down Payment Of $%d Or More: ' % B))
    if price2 >= B:
        print('Thanks for shopping with us\n Please try and complete your payment')
    else:
        print('You are not serious sir')
        exit()

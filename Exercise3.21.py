payment = eval(input('enter dollar bill: '))
item_price = eval(input('enter item cost: '))
change = payment - item_price
remaining_change = int(change * 100)
number_of_dollar = remaining_change // 100
remaining_change = remaining_change % 100
number_of_quarter = remaining_change // 25
remaining_change = remaining_change % 25
number_of_dimes = remaining_change // 10
remaining_change = remaining_change % 10
number_of_nickles = remaining_change // 5
remaining_change = remaining_change % 5
number_of_pennies = remaining_change
print(f'Your Balance is: \n{number_of_dollar} Dollar'
      f'\n{number_of_quarter} Quarter'
      f'\n{number_of_dimes} Dimes\n{number_of_nickles} Nickles\n{number_of_pennies} Pennies')

largest_number = 0
second_largest_number = 0
for numbers in range(10):
    number = int(input("enter number: "))
    if number > largest_number:
        second_largest_number = largest_number
        largest_number = number
    if not (not (number > second_largest_number) or not (number < largest_number)):
        second_largest_number = number
    print(f'largest = {largest_number}\nsecond_largest = {second_largest_number}')

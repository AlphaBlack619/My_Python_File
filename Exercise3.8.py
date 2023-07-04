number = 1
sum_of_number = 0
average = 0
product = 0
largest_number = 0
smallest_number = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
while number < 5:
    incoming_number = int(input("enter number: "))
    number += 1
    sum_of_number += incoming_number
    product = incoming_number * incoming_number * incoming_number
    average = sum_of_number/number
    if incoming_number > largest_number:
        largest_number = incoming_number
    if incoming_number <= smallest_number:
        smallest_number = incoming_number
print(f'Product is {product}\nAverage is {average}\n Sum of numbers is {sum_of_number}\nLargest number is {largest_number}\nSmallest number {smallest_number}')

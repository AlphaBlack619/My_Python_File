miles = 0
gallon = 0
incoming_gallon = 0
while incoming_gallon != -1:
    incoming_gallon = float(input('enter the gallon used or -1 to end: '))
    incoming_miles = float(input('enter the miles driven: '))
    print(f'The gallon/mile for this tank was {incoming_miles/incoming_gallon}')
    if incoming_gallon != -1:
        miles += incoming_miles
        gallon += incoming_gallon
print(f'The overall average gallons/miles is {miles/gallon}')

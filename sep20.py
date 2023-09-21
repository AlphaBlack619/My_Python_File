def sorter(number: []):
    checker = 0
    for num in range(len(number)):
        count = 0
        for num1 in range(len(number)):
            if number[num] == number[num1]:
                count += 1
        if count <= 1:
            checker = number[num]
    return checker


input1 = [2, 2, 1]
print(sorter(input1))
input2 = [3, 4, 2, 2, 3, 2]
print(sorter(input2))
input3 = [1]
print(sorter(input3))

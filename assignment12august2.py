def list_checker(arrays, arrays2):
    new_arrays = []
    for element in arrays:
        for elements in arrays2:
            if element == elements:
                new_arrays.append(element)
    print(set(new_arrays))


a = [1, 2, 3, 3, 4, 5, 6]
b = [1, 2, 3, 0, 9, 7, 8]
list_checker(a, b)

def length_finder(collection):
    number = 0
    for element in collection:
        number = number + 1
    return number


def unique_element(collection: []):
    return set(collection)


a = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9, 9]
b = {0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9, 9}
print('The length of the collection is', length_finder(b))
print('The unique elements are', unique_element(a))
print('The length of the collection is', length_finder(a))

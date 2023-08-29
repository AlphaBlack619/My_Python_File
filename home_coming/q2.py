a = 1500
b = 2700


def finder():
    print(a)
    for x in range(a, b):
        if x % 7 == 0 and x % 5:
            print(x)
    print(b)


finder()

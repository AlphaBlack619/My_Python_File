list1 = (["white", 'Black', 'Red'])
list2 = (['Red', 'Green'])


def printer(l1, l2):
    l3 = ([])
    for x in range(len(l1)):
        for element2 in range(len(l2)):
            if l1[x] != l2[element2]:
                l3.append(l1[x])
    print(set(l3))


printer(list1, list2)

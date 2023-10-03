def name_sorter(name):
    first_name = ''
    last_name = ''
    middle_name = ''
    cont = 0
    for x in range(len(name)):
        if name[x] == ' ' and cont <= 0:
            middle_name = name[x+1]
            cont = 1
        if name[x] == ' ' and cont == 1:
            last_name = last_name + name[x]
    return name[0] + '.' + middle_name + '.' + last_name


print(name_sorter("Grace Martins Akpan"))

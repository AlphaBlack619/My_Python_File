def extension(file_name):
    a = 0
    b = ''
    for x in range(len(file_name)):
        if file_name[x] == ".":
            a = x
    for x in range(len(file_name)):
        if x > a:
            b += file_name[x]
    print(b)


c = "okon.java"
extension(c)

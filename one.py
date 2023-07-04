counter = int(input('enter command or -1 to exit application:'))
while counter != -1:
    counter = input(input('enter command or -1 to exit application: '))
    if counter == 1:
        def a(x=input('x =: ')):
            if x == '1':
                print(b())
            elif x == '0':
                return c()

        def b(y=input()):
            if y == '1':
                return '3'
            elif y == '0':
             return c()


        def c(z=input()):
            if z == '1':
             return '8'
            elif z == '2':
                print(a())

    counter = input(input('enter command or -1 to exit application: '))


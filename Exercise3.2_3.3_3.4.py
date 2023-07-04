a = b = 7
print('a =', a, '\nb =', b)
# Nothing so far cause a and b as the same value
# Exercise3.3
#(What Does This Code Do?) What does the following program print?
for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
print()
# Exercise3.4
#(Fill in the Missing Code) In the code below
for row in range(2):
    print()
    for column in range(7):
        print("@", end='')
print()

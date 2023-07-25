b = 4
c = 8
sum3 = 0
sum4 = 0

for y in range(1, 10):
    if y < 5:
        a = 4
        b *= a
        sum3 += b
    if y > 5:
        a = 8
        c *= a
        sum4 += c

print(sum3)
print(sum4)

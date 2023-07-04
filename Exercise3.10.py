investment = 10000
rate = 7 / 100
for year in range(1, 31):
    print(f'Money made in {year} years is ₦{investment * (1 + rate) ** year}')

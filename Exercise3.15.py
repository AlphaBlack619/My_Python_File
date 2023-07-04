def summing_terms_of_constant_e(term=int(input('enter prefer term: '))):
    var = 2.718281828
    for x in range(1, term):
        var += var/x
    print(f'The sum of {term}th terms of e constant is {var}')


summing_terms_of_constant_e()

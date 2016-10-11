def isfibo(number):
    m = 1
    n = 1
    i = 1
    while n<number:
        n += m
        m = n - m
        i += 1
    else:
        if n - number == 0:
            print 'Yes! Fibonacci series number:',i
        else:
            print 'No!'
number = input('Enter 1 to initiate or 0 to quit:')
while number !=0:
    number = input('Enter number to check (0 to quit):')
    isfibo(number)




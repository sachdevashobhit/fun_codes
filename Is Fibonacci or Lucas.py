
# coding: utf-8

# In[11]:

def isfibo(number):
    m = 1
    n = 1
    i = 1
    while n<number:
        n = m + n
        m = n - m
        i += 1
    else:
        if n - number == 0:
            return True
#             print 'Yes! Fibonacci series number:',i
        else:
            return False
#             print 'No!'
# number = input('Enter 1 to initiate or 0 to quit:')
# while number !=0:
#     number = input('Enter number to check (0 to quit):')
#     if isfibo(number) == True:
#         print 'Yes, Fibonacci'
#     else:
#         print 'Nah!'


# In[12]:

def isLucas(number):
    m = 2
    n = 1
    i = 1
    while n<number:
        n = m + n
        m = n - m
        i += 1
    else:
        if n - number == 0:
            return True
#             print 'Yes! Lucas series number:',i
        else:
            return False
#             print 'No!'
# number = input('Enter 1 to initiate or 0 to quit:')
# while number !=0:
#     number = input('Enter number to check (0 to quit):')
#     if isLucas(number) == True:
#         print 'Yes, Lucas!'
#     else:
#         print 'Nah'


# In[13]:

number = input('Enter 1 to initiate or 0 to quit:')
while number !=0:
    number = input('Enter number to check (0 to quit):')
    if isLucas(number) is True:
        print 'It is Lucas!'
    elif isfibo(number) is True:
        print 'It is Fibonacci!'
    else:
        print 'None'


# In[ ]:




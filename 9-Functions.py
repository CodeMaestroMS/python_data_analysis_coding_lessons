from math import sqrt


def double(x):
    """This function multiplies its argument by two."""
    return x*2

print(double(4), double(1.2), double('abc'))


print(f'The docstring is: {double.__doc__}')

help(double) #Another way to access the docstring

help(print)


def sum_of_squares(x, y):
    """Compute the sum of arguments squared"""
    return pow(x,2) + pow(y,2)
print(sum_of_squares(3, 4))


def sum_of_squares(lst):
    """Computes the sum of squares of elements in the list given as parameter"""
    total = 0
    for i in lst:
        total += pow(i, 2)
    return total
print(sum_of_squares([-2]))
print(sum_of_squares([-2, 4, 5]))


def sum_of_squares(*t):
    total = 0
    for i in t:
        total += pow(i, 2)
    return total
print(sum_of_squares(-2))
print(sum_of_squares(2, 4, 5))


def  named(a,b,c):
    print(f'First: {a}, Second: {b}, Third: {c}')
named(5, c=7, b=8)


print(1,2,3,end=' |', sep=' -*- ')
print('first','second','third', end=' |', sep=' -*- ')


print('============================')

def length(*t,degree=2):
    """Compute the length of the vector given as paramtere.By default, it computes
    the Euclidean distance"""
    s=0
    for x in t:
        s+=pow(abs(x), degree)
    return pow(s, 1/degree)
print(length(-4,3))
print(length(-4,3,degree=3))
x=input('Give an Integer: ')
x=int(x)

if x>=0:
    a=x
else:
    a=-x
print(f'The absolute value of {x} is {a}')


c=float(input('Give a number: '))

if c>0:
    print('c is positive')
elif c<0:
    print('c is negative')
else:
    print('c is zero')
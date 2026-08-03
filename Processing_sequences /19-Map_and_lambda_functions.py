def double(x):
    return 2*x

L=[12,4,-1]

print(map(double,L))
print(list(map(double,L)))

s='12 43 64 6'
L=s.split()

print(L)
print(sum(map(int,L)))


def add_double_and_square(x):
    return 2*x+x**2

L=[2,3,5]
print(list(map(lambda x: 2*x+x**2, L)))

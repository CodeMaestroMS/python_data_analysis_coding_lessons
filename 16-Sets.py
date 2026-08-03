S={1,1,1}
print(S)

S=set([1,2,2,'a'])
print(S)

S=set()   # empty set
print(S)
S.add(7)  # add one element
print(S)

s='mississippi'
print(f'There are {len(set(s))} distinct characters in {s}')


print('===============================')
s={1,2,7}
t={2,8,9}

print(f's={1,2,7}')
print(f't={2,8,9}')
print(f'Union: {s|t}')
print(f'Intersection: {s&t}')
print(f'Difference: {s-t}')
print(f'Symmetric difference: {s^t}')


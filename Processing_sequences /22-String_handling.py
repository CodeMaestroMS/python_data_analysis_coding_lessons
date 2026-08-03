s='menik sabeeshan'
print(s.isalnum())

print(s.title())
print(s.capitalize())

s=' missis sippi'
print(s.find('issi'))

print(s)
print(s.strip())

s='menik sabeeshan'
print('|' + s.ljust(20)+'|')

L=[1,3,5,7,9,1,1]
print('-'*11)
for i in L:
    s='*'*i
    print(f'|{s.center(9)}|')
print('-'*11)

print('---'.join(['abc','def','ghi']))


# L = { string of x | x ∈ (0,1,2...,99) }
L = [str(x) for x in range(100)]
print(' '.join(L))

import re

S='ApplePie'
result = re.match(r'[A]pple',S)
print(result)
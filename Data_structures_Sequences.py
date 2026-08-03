l = [2,100,'hello',1.0]

t1=(3,)
t2=(1,3)
t3=(1,'Hello',1.0)

s='abcdefg'
print(s[1:4])

print([0,1,2,3,4,5,6,7,8,9][::3])

# Modifying List

L=[11,13,22,32]
print(L)

L[2]=10
print(L)

# L[1:3] -> [13,10]
L[1:3]=[4]
print(L)


print('Mutation Methods')
# Mutation Methods

# append
L = [1,2,3]
L.append(4)
print(L)

L.append([5,6])
print(L)

L=[1,2,3]
L.extend([4,5])
print(L)

L=[1,2,3]
L.insert(1,99)
print(L)

L=[1,2,3,2]
L.remove(2)
print(L)

L=[1,2,3]
last=L.pop()
print(f'list = {L}, last = {last}')

first=L.pop(0)
print(f'list = {L}, first = {first}')

L=[3,1,2]
L.reverse()
print(L)

L=[3,1,2]
L.sort()
print(L)

L.sort(reverse=True)
print(L)

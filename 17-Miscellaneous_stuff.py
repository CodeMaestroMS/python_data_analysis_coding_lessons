# find out whether a container includes an element,

print(1 in [1,2])

d= dict(a=1, b=2)
print("b" in d)

s=set()
print(1 in s)
print('x' in 'text')

print('issi' in 'mississippi')
print('issp' in 'mississippi')

# Elements of a container can be unpacked into variables:

first,second = [4,5]
a,b,c='bye'
print(c)

d=dict(a=1,b=3)
key1,key2 = d
print(key1, key2)

for key, value in d.items():
    print(f'For key {key} value {value} was stored')

#To remove the binding of a variable,

s='hello'
del s
# print(s) This would cause an error

L=[13,23,40,100]
del L[1]
print(L)
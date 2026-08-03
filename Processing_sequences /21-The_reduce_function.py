from functools import reduce

L=[1,2,3,4]

print(reduce(lambda x,y: x+y, L , 0))

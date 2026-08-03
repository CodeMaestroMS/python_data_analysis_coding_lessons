def is_odd(x):
    """Return True if x is odd and False if x is even"""
    return x%2==0

L=[1,4,5,9,10]
print(list(filter(is_odd,L)))

# O = {x | x ∈ L, x%2==0}
Q=[x for x in L if is_odd(x)]
print(Q)
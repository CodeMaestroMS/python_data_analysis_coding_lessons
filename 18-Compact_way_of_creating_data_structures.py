L=[]

for i in range(10):
    L.append(i**2)

print(L)

# { a³ | a ∈ a ≥ 1 and a ≤ 10

L = [a**3 for a in range(1,11)]
print(L)

# L = { 100*a + 10*b + c | a,b,c ∈ {1,2,...9}, a ≤ b ≤c}

L= [ 100*a + 10*b + c for a in range(0,10) for b in range(0,10) for c in range(0,10) if a<=b<=c]
print(L)

G= ( 100*a + 10*b + c for a in range(0,10) for b in range(0,10) for c in range(0,10) if a<=b<=c)
print(sum(G))
print(sum(G))

#D = { k: k**2 | k ∈ {1,2,...9} }
D = {k: k**2 for k in range(1,10)}
print(D)

# S = {i*j | i,j ∈ {1,2,...9}}
S={i*j for i in range(1,10) for j in range(1,10)}
print(S)

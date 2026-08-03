a=1
print(a)

type_of_a = type(a)
print(type_of_a.__name__)

a='some text'

type_of_a = type(a)
print(type_of_a.__name__)

'''
int
float
str
bool
complex
bytes
'''

i=5
f=1.5

s='conca'+'tenation'
print(s)

b= i==4
print('Result of the comparison:', b)

c=0+2j # j=√-𝟷
print('Complex multiplication:', c*c)


print(int(-2.8))
print(float(2))
print(int('123'))
print(bool(-2))
print(bool(0))
print(str(234))

print("===================")

b = 'ä'.encode('utf-8') # Convert character(s) to a sequence of bytes
print(b)                # Prints bytes in hexadecimal notation
print(list(b))          # Prints bytes in decimal notation

print(ord('A'))
print(chr(65))

a = bytes.decode(b,'utf-8')
print(a)
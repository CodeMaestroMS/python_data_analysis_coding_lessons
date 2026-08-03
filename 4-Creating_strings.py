print("I don't want to go")
print('I don\'t want to go')

print('One\tTwo\nThree\tFour')

s= """ 
   A string spanning over 
   several lines
"""

print(s)

a='first'
b='second'

print(a+b)
print(' '.join([a,b]))

print('=============================')

print("%i plus %i is equal to %i" % (1,3,4))            # Format syntax
print("{} plus {} is equal to {}".format(1,3,4))  # Format method
print(f'{1} plus {3} is equal to {4}')                  # f-string

print(f'{4:3d}')

#1.6, 1.7, 1.8

print('%.1f %.2f %.3f'%(1.6,1.7, 1.8))
print('{:.1f} {:.2f} {:.3f}'.format(1.6, 1.7, 1.8))
print(f'{1.6:.1f} {1.7:.2f} {1.8:.3f}')

print('===============================')

#water concatenated with melon produces watermelon
print('%s concatenated with %s produces %s.'%('water','melon','water'+'melon'))
print('{} concatenated with {} produces {}.'.format('water','melon','water'+'melon'))
print(f'{'water'} concatenated with {'melon'} produces {'water'+'melon'}.')





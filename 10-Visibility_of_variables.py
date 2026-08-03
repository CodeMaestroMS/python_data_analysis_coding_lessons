i=2          #Global variable
def func():
    i=3      # this creates a new variable, it does not rebind the global i
    print(i) # this will print 3
func()
print(i)     # this will print 2

print('=================================================')

def f():
    global i
    i=5
    print(i)
f()
print(i)

print('=================================================')

def f1():           # outer function
    b=2
    def g():        # inner function
        #nonlocal b # Without this nonlocal statement,
        b=3         # this will create a new local variable
        print(b)
    g()
    print(b)
f1()
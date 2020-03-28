x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
    return lambda a : a * n
    
dobro = myfunc(2)
print(dobro(11))
# lambda expresion

# x = lambda a , b , c : a + b + c
# print(x(5,10,15))

def myFunction(n):
    return lambda a : a * n # a : a * 10

y = myFunction(10)

print(y(5))
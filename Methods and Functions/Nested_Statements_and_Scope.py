x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

#lambda num:num**2

#Global
name = 'THIS IS A GLOBAL STRING'

def greet():
    #Enclosing
    name = 'Sammy'

    def hello():
        #LOCAL
        #name = 'IM A LOCAL'
        print('Hello ' + name)

    hello()

greet()

x = 50

def func(x):

    print(f'X is {x}')
    x = 'NEW VALUE'
    print(f'I just locally changed global x to {x}')
    return x

print(func(x))
func(x)
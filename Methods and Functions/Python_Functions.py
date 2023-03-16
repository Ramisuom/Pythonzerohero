def say_hello():
    print('hello')
    print('are')
    print('you')

print(say_hello())

def say_hello(name='Default'):
    print(f'Hello {name}')
    return name

print(say_hello('Tomi'))
print(say_hello())

def add_num(num1,num2):
    return num1+num2

result = add_num(10,20)
print(result)

def print_result(a,b):
    print(a+b)
    return a+b

def return_result(a,b):
    return a+b

print(print_result(10,20))
result = return_result(10,20)
print(result)

def myfunc(a,b):
    print(a+b)
    return a+b

result = myfunc(10,30)
print(result)

def sum_numbers(num1,num2):
    return num1+num2

print(sum_numbers(10,20))
print(sum_numbers('10','20'))
print(type(sum_numbers))
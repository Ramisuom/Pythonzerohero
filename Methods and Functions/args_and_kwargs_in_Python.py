def myfunc(a,b,c=0,d=0,e=0):
    # returns 5% of the sum a and b
    return sum((a,b,c,d),e) * 0.05

print(myfunc(40,60,100,100))

def myfunc(*args):
    return sum(args) * 0.05
print(myfunc(40,60,100,1,34,500,400))

def myfunc(*args):
    for item in args:
        print(item)
print(myfunc(40,60,100,1,34,500,400))

def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choise is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruits in here')
myfunc(fruit='apple',veggie = 'lettuce')

def myfunc(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['foods']))
myfunc(10,20,30,fruit='orange',foods='eggs',animal='dog')



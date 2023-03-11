mylist = [1,2,3,4,5,6,7,8,9,10]
for jelly in mylist:
    print('hello')

for num in mylist:
    #Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print(list_sum)

mystring = 'Hello world'

for _ in 'Hello world':
    print('Cool')

tup = (1,2,3)

for item in tup:
    print(item)

mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))

for (a,b) in mylist:
    print(a)
    print(b)

mylist = [(1,2,3),(5,6,7),(8,9,10)]
for a,b,c in mylist:
    print(c)

d = {'k1':1, 'k2':2, 'k3':3}

for key,value in d.values():
    print(value)
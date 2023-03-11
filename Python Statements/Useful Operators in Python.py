mylist = [1,2,3]
for num in range(0,11,2):
    print(num)

print(list(range(0,11,2)))

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

word = 'abcde'
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for item in zip(mylist1, mylist2, mylist3):
    #print(item)
    print(list(zip(mylist1,mylist2)))

print('x' in [1,2,3])
print('x' in ['x','y','z'])
print('a' in 'a world')
print('mykey' in {'mykey':345})

d = {'mykey':345}
print(345 in d.keys())

mylist = [10,20,30,40,100]
print(min(mylist))
print(max(mylist))

from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,100))
mynum = randint(0,10)
print(mynum)

result = print(input('What is your name: '))

result = print(input('Favorite number: '))
print(type(result))
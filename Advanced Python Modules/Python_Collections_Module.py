from collections import Counter
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3,3,3]
print(Counter(mylist))

mylist = ['a','a',10,10,10]
print(Counter(mylist))

print(Counter('aaaabbbbbshshshsjs'))

sentence = 'How many times does each word show up in this sentence with a word'
print(Counter(sentence.lower().split()))

letters = 'aaaaabbbbbbccccccdddddddd'
c = Counter(letters)
print(c)
print(c.most_common())
print(list(c))

from collections import defaultdict
d = {'a':10}
print(d)
print(d['a'])

d = defaultdict(lambda: 0)
d['corrext'] = 100
print(d['corrext'])
print(d['WRONG KEY!'])

mytuple = (10,20,30)
print(mytuple[0])

from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'])
print(Dog)
sammy = Dog(age=5,breed='Husky',name='Sam')
print(sammy)
print(sammy.age)
print(sammy.breed)
print(sammy.name)
print(sammy[0])
print(sammy[2])
print(sammy[1])
#Iterators and Generators Homework
#Problem 1
#Create a generator that generates the squares of numbers up to some number N.

def gensquares(N):
    for x in range(N):
        yield x**2

for x in gensquares(10):
    print(x)

#Problem 2
#Create a generator that yields "n" random numbers between a low and high number (that are inputs).
#Note: Use the random library. For example:

import random

random.randint(1,10)

def rand_num(low,high,n):
    for i in range(n + 1):
        yield random.randint(low, high)

for num in rand_num(1, 10, 12):
    print(num)

#Problem 3
#Use the iter() function to convert the string below into an iterator:

s = 'hello'
for letter in s:
    print(letter)

s_iter = iter(s)

#Problem 4
#Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.
#A generator, utilizing a yield statement, returns an iterator object. The iterator object will yield/return a value each time it is called upon to iterate
# through its code. So in cases where a return statement would be used to return the entirely of a list, the generator would only return the current iteration of the
# list, remembering its state where it was last yielded.

#Extra Credit!
#Can you explain what gencomp is in the code below? (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)
#a generator expression is similar to a list comprehension. However it returns a generator rather than a list.
# Syntactically they are very similar with the exception being that list comps use [] and gen comps use ().




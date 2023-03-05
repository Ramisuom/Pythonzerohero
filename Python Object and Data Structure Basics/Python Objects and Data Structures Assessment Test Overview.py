#Test your knowledge.
#** Answer the following questions **

#Write (or just say out loud to yourself) a brief description of all the following Object Types and Data Structures we've learned about.

#Numbers: Integers. whole numbers

#Strings: Words, names, object etc.

#Lists: List of values

#Tuples: Used to store multiple items in a single variable

#Dictionaries: Used to store objects and valuables

#Numbers!!!

#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
print((60 + (10**2) / 4 * 7) - 134.74)

#Answer these 3 questions without typing code. Then type code to check your answer.

#What is the value of the expression 4 * (6 + 5)
print(4 * (6 + 5))
#What is the value of the expression 4 * 6 + 5
print(4 * 6 + 5)

#What is the value of the expression 4 + 6 * 5
print(4 + 6 * 5)

#What is the type of the result of the expression 3 + 1.5 + 4?
#Floating point number


#What would you use to find a number’s square root, as well as its square?
# Square root:
#100**0.5

# Square:
#10**2

#Strings!!!

#Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
print(s[1])

#Reverse the string 'hello' using slicing:
print(s[::-1])

#Given the string hello, give two methods of producing the letter 'o' using indexing.
print(s[4])
print(s[-1])

#Lists!!
#Build this list [0,0,0] two separate ways.
list = [0,0,0]
list2 = [0]*3

#Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'

#Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()

#Dictionaries!!!!
#Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

#d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

#Tuples!!!!
#What is the major difference between tuples and lists?
#Tuples are immutable as opposed to lists which are mutable

#How do you create a tuple?
#Placing all the items (elements) inside parentheses () , separated by commas

#Sets!!!!
#What is unique about a set?
#A set is uniquely determined by its elements

#Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

#Booleans!!!
#What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# Answer before running cell
print(2 > 3) #False
# Answer before running cell
print(3 <= 2) #False
# Answer before running cell
print(3 == 2.0) #False
# Answer before running cell
print(3.0 == 3) #True
# Answer before running cell
print(4**0.5 != 2) #False

#Final Question: What is the boolean output of the cell block below?
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print(l_one[2][0] >= l_two[2]['k1']) #False
#Functions and Methods Homework
#Complete the following questions: ____ Write a function that computes the volume of a sphere given its radius.

#The volume of a sphere is given as

def vol(rad):
    return (4/3)*(3.14)*(rad**3)

print(vol(2))

#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    #Check if num is between low and high (including low and high)
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')

(ran_check(5,2,7))

def ran_bool(num,low,high):
    return num in range(low,high+1)

print(ran_bool(3,1,10))

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

#Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

print(multiply([1,2,3,-4]))

#Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
    s = s.replace(' ',
                  '')  # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1]  # Check through slicing


print(palindrome('nurses run'))
print(palindrome('abcba'))

#Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    # Create a set of the alphabet
    alphaset = set(alphabet)

    # Remove spaces from str1
    str1 = str1.replace(" ", '')

    # Lowercase all strings in the passed in string
    # Recall we assume no punctuation
    str1 = str1.lower()

    # Grab all unique letters in the string as a set
    str1 = set(str1)

    # Now check that the alpahbet set is same as string set
    return str1 == alphaset

print(ispangram("The quick brown fox jumps over the lazy dog"))
print(string.ascii_lowercase)
example = [1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)
print(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(result)

mylist = ['','O','']
shuffle_list(mylist)
print(mylist)

def player_guess():

    guess=''

    while guess not in ['0','1','2']:
        guess = input('Pick a number: 0,1, or 2')

    return int(guess)

myindex = player_guess()
print(myindex)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong guess!')
        print(mylist)

#Initial list
mylist = ['','O','']

#Shuffle list
mixedup_list = shuffle_list(mylist)

#User guess
guess = player_guess()

#Check guess
check_guess(mixedup_list,guess)
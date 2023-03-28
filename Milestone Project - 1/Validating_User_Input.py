def user_choise():
    #VARIABLES

    #Initial
    choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False

    #TWO CONDITIONS TO CHECK
    #DIGIT OR WITHIN RANGE==FALSE
    while choice.isdigit() == False or within_range==False:

        choice = input("Please enter a number (0-10): ")

        #DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")

        #RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry you are out of acceptable range (0-10)')
                within_range = False

    return int(choice)
print(user_choise())


#result = 'WRONG VALUE'
#acceptable_values = [0,1,2]
#print(result in acceptable_values)
#print(result not in acceptable_values)

#some_value = '100'
#print(some_value.isdigit())
#print(int(some_value))


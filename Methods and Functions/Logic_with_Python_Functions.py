def even_check(number):
    result = number % 2 == 0
    return result

print(even_check(20))
print(even_check(21))

#Return True if any number is even inside a list
def check_even_list(num_list):
    #Return all the even numbersin a list

    #Placeholder variables
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers

print(check_even_list([1,2,3,4,5]))
print(check_even_list([1,3,5]))
print(check_even_list([2,1,1,1]))
print(check_even_list([1,1,1,2]))
def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

display(row1,row2,row3)

row2[1] = 'X'

display(row1,row2,row3)

result = input('Please enter a value: ')
print(type(result))

result = input('Enter Value: ')
result_int = int(result)
print(type(result_int))

position_index = int(input("Choose an index position: "))
print(type(position_index))
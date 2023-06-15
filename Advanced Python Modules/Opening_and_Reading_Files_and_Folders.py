#f = open('practice.txt','w+')
#f.write('This is a test string')
#f.close()
import os
#print(os.getcwd())
#print(os.listdir('C:\\Users\\Rami'))

import shutil
#shutil.move('practice.txt','C:\\Users\\Rami')
import send2trash
#send2trash.send2trash('C:\\Users\\Rami\\practice.txt')
#print(os.listdir('C:\\Users\\Rami'))
print(os.getcwd())
file_path = 'C:\\Users\\Rami\\PycharmProjects\\pythonzerohero\\Advanced Python Modules'
for folder, sub_folders,files in os.walk(file_path):
    print(f"Currently looking at {folder}")
    print("\n")
    print('The subfolders are: ')
    for sub_fold in sub_folders:
        print(f"Subfolder: {sub_fold}")

    print('\n')
    print('the files are: ')
    for f in files:
        print(f"File: {f}")
    print('\n')
import csv
#Open the file
data = open('example.csv',encoding='utf-8')

#csv.reader
csv_data = csv.reader(data)
#refomart it into a python object list of listst
data_lines = list(csv_data)
print(data_lines)
print(len(data_lines))

for line in data_lines[:5]:
    print(line)

print(data_lines[10])[3]

all_emails = []

for lines in data_lines[1:]:
    all_emails.append(line[3])

print(all_emails)

full_names = []

for line in data_lines[1:]:
    full_names.append(line[1]+' '+ line[2])

file_to_output = open('to_save_file.csv' ,mode='w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows(['1','2','3'],['4','5','6'])
file_to_output.close()
f = open('to_save_file.csv',mode='a',newline='')
csv_writer.writerow(['1','2','3'])
f.close()
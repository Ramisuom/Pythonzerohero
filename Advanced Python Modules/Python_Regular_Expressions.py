text = "The agent's phone number is 408-555-1234. Call soon!"
print('phone' in text)
import re
pattern = 'phone'
print(re.search(pattern,text))
pattern = 'NOT IN TEXT'
print(re.search(pattern,text))
pattern = 'phone'
match = re.search(pattern,text)
print(match)
print(match.span())
print(match.end())
text = "my phone once, my phone twice"
match = re.search('phone',text)
print(match)
matches = re.findall('phone',text)
print(matches)
print(len(matches))
for match in re.finditer('phone',text):
    print(match.group())
text = 'My phone number is 408-555-1234'
phone = re.search(r'\d{3}-\d{3}-\d{4}',text)
print(phone.group())
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
print(results.group())
print(results.group(2))
re.search(r'cat|dog','The dog is here')
re.findall(r'...at','the cat in the hat went splat')
print(re.findall)
re.findall(r'^\d','2 is a number')
print(re.findall)
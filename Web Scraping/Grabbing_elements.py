#Crapping a Title
import requests
result = requests.get('https://www.example.com/')
print(type(result))
#print(result.text)

import bs4
soup = bs4.BeautifulSoup(result.text,'lxml')
#print(soup)
print(soup.select('title'))
print(soup.select('p'))
print(soup.select('h1'))
print(soup.select('title')[0].getText)
site_paragraphs = soup.select('p')
print(site_paragraphs[0])
print(site_paragraphs[0].getText())

#Crapping a Class
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text,'lxml')
#print(soup)
first_item = soup.select('.mw-headline')[0]
print(type(soup.select('.mw-headline')[0]))
for item in soup.select('.mw-headline'):
    print(item.text)

#Crapping a image
res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
print(soup.select('.thumbimage'))
computer = soup.select('.thumbimage')[0]
print(computer)
print(computer['src'])
#<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg'>
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
print(image_link.content)

f = open('my_computer_image.jpg','wb')
print(f.write(image_link.content))
f.close()
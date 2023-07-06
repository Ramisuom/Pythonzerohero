#GOAL: Get the title of every book with a 2 star rating
import requests
import bs4
'https://books.toscrape.com/catalogue/page-2.html'
'https://books.toscrape.com/catalogue/page-3.html'
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
#page_num = 12
#base_url.format(page_num)
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')
products = soup.select('.product_pod')
example = products[0]
print('star-rating Three' in str(example))
print(example.select('.star-rating.Three'))
print(example.select('a')[1]['title'])
two_star_title = []

for n in range(1,51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.star.rating.Two')) != 0:
            book_title = example.select('a')[1]['title']
            two_star_title.append(book_title)

print(two_star_title)
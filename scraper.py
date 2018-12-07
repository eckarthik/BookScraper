import re,requests,json,csv
from bs4 import BeautifulSoup
req = requests.get("https://www.indiabookstore.net/categories/computerScience")
soup = BeautifulSoup(req.text,"html.parser")
books_counter = 0
books = []
for book in soup.find_all("a",{'class':'bookPageLink'}):
    book_link = book.get("href")
    if str(book_link).startswith("/isbn"):
        books_counter+=1
        book = []
        req2 = requests.get("https://www.indiabookstore.net"+book_link)
        soup = BeautifulSoup(req2.text,"html.parser")
        getImageAndTitle = soup.find("img",{'class':'bookMainImage'})
        imageLink = getImageAndTitle.get('src')
        bookTitle = getImageAndTitle.get('title')
        getAuthor = soup.find("div",{'itemprop':'author'})
        authorName = str(getAuthor.text).split(":")[1]
        print authorName
        getBookDescription = soup.find("span",{"itemprop":"description"})
        try:
            bookDescription = getBookDescription.text
        except AttributeError:
            bookDescription = ""
        '''book[str("image")] = imageLink
        book[str("title")] = bookTitle
        book[str("author")] = authorName
        book[str("description")] = bookDescription.encode('ascii','ignore')
        book[str("category")] = "Computer Science"'''
        book.append(imageLink)
        book.append(bookTitle)
        book.append(authorName)
        book.append(bookDescription.encode('ascii','ignore'))
        book.append("Computer Science")
        book.append(str(book_link).replace("/isbn/",""))
        books.append(book)
print books
ofile = open('ttest.csv', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

for row in books:
    writer.writerow(row)
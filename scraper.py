import re,requests,json,csv
from bs4 import BeautifulSoup
books_counter = 0

ofile = open('ttest.csv', "wb",)
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL,lineterminator='\n')
for i in range(1,6):
    books = []
    req = requests.get("https://www.indiabookstore.net/categories/romance?page="+str(i))
    soup = BeautifulSoup(req.text,"html.parser")
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
            try:
                authorName = str(getAuthor.text).split(":")[1]
            except Exception:
                continue
            print authorName
            getBookDescription = soup.find("span",{"itemprop":"description"})
            try:
                bookDescription = getBookDescription.text
            except AttributeError:
                bookDescription = ""
                continue
            '''book[str("image")] = imageLink
            book[str("title")] = bookTitle
            book[str("author")] = authorName
            book[str("description")] = bookDescription.encode('ascii','ignore')
            book[str("category")] = "Computer Science"'''
            book.append(imageLink)
            book.append(bookTitle)
            book.append(authorName)
            book.append(bookDescription.encode('ascii','ignore'))
            book.append("Romance")
            book.append(str(book_link).replace("/isbn/",""))
            books.append(book)
    print books


    for row in books:
        try:
            writer.writerow(row)
        except Exception:
            continue
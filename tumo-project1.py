from bs4 import BeautifulSoup
import urllib2
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'
}
url = "http://www.packtpub.com/books"
req = urllib2.Request (url, headers=hdr)
page = urllib2.urlopen(req)
soup = BeautifulSoup (page, features="html.parser")
bb = soup.find_all(class_="product details product-item-details")
oo = soup.find(class_="short-description")
linkss = soup.find(class_="product-item-link")
for s in range(len(bb)):
    book = bb[s]
    name= (book.strong)
    print("name="+" "+book.strong.a.string+"  "+"deskription="+" "+ oo.string+"  "+ "pice="+" "+book.span.span.span.string+"  ")
    
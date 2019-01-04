'''
使用原生爬虫爬取电子书信息，
每一本书的信息都需要爬取，
包括书名、作者、内容简介...等。
参考地址：http://d81fb43e-d.parkone.cn/
'''
import re
from urllib import request
class Book():
    url = 'http://d81fb43e-d.parkone.cn/book/'
    root_pattern = ''
    book_pattern = '<h2>([\s\S]*?)</h2>'
    name_pattern = '<a href="/author/[\s\S]*?">([\s\S]*?)</a>'
    number_pattern = '<span>出版社:([\s\S]*?)</span>'
    eyse_pattern = '<p class="description">([\s\S]*?)</p>'
    out_pattern = '<p>出版日期:([\s\S]*?)</p>'

    def __fetch_content(self):
        url = Book.url+str(i)
        r = request.urlopen(url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls
    
    def __analysis(self,htmls):
        authors = []
        bookname = re.findall(Book.book_pattern,htmls) 
        name = re.findall(Book.name_pattern,htmls)
        number = re.findall(Book.number_pattern,htmls)
        eyse = re.findall(Book.eyse_pattern,htmls)
        out = re.findall(Book.out_pattern,htmls) 
        author = {'书名':bookname,'作者':name,'出版社':number,'出版日期':out,'简介':eyse}
        authors.append(author)
        print(authors)
    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)

for i in range(1,254):
    book = Book()
    book.go()

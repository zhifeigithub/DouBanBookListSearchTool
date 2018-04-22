#coding=utf-8
#from selenium import webdriver
from selenium import webdriver
from time import sleep
 
class DoubanBookList:
 
    def __init__(self):
        self.dr = webdriver.Chrome(executable_path=r"D:/Program Files/chromedriver/chromedriver.exe")
        self.popular_books_list = self.get_douban_popular_books()
 
    def get_douban_popular_books(self):
        self.dr.get('https://book.douban.com/subject_search?search_text=%E5%86%99%E4%BD%9C&cat=1001')
        sleep(3)
        popular_books_list = [] #定义一个空list用于存放获取的书籍信息
        i = 0
        #while i < 10:
            #book_info = self.dr.find_elements_by_css_selector("[class='list-col list-col2 list-summary s']>li")[i].text #通过css用class属性和标签li组合来获取书籍所有文本信息
            #popular_books_list.append(book_info.split('\n')) #向空list追加书籍信息用并换行符隔开
            #i += 1

        book_infos = self.dr.find_elements_by_class_name('sc-bZQynM.gPYOKF.sc-bxivhb.eHmSYu')
        #title = self.dr.find_elements_by_class_name('sc-bZQynM fQQXdG sc-bxivhb eHmSYu')
        print('dff')
        for item in book_infos:
            book_info = []
            book_info.title = item.find_elements_by_class_name('title')[0].text
            book_info.rating_nums = item.find_elements_by_class_name('rating_nums')[0].text 
            book_info.pl = item.find_elements_by_class_name('pl')[0].text
            book_info.pl_num = int(book_info.pl[1:-4])
            book_info.meta_abstract = item.find_elements_by_class_name('meta abstract')[0].text
            popular_books_list.append(book_info)
        
        popular_books_list.sort(key=lambda x:x.pl_num, reverse=True) #用sort中key方法根据书籍评分从高到低进行排序
        #popular_books_list = sorted(popular_books_list, key=lambda book: book[1][0:3], reverse=True)
        return popular_books_list
 
    def get_popular_books_rank_file(self):
        self.file_title = '豆瓣某个主题的搜索评论排行'
        self.file = open(self.file_title + '.txt', 'wb')
        for item in self.popular_books_list:
            separate_line = '~~~~~~~~~~~~~~~~~~~~~~~~\r\n'
            self.file.write(separate_line.encode('utf-8'))
            self.file.write(('书籍名称:'+item[0]+'\r\n').encode('utf-8'))
            self.file.write(('评分:'+item[1]+'\r\n').encode('utf-8'))
            self.file.write(('评论数:'+item[2]+'\r\n').encode('utf-8'))
            self.file.write(('体裁:'+item[4]+'\r\n').encode('utf-8'))
            #if item[4] == '有电子书':
            #    self.file.write(('一句话评论:'+item[5]+'\r\n').encode('utf-8'))
            #else:
            #    self.file.write(('一句话评论:'+item[4]+'\r\n').encode('utf-8'))
        self.file.close()
 
 
    def quit(self):
        self.dr.quit()
 
if __name__ == '__main__':
    popular_books = DoubanBookList()
    popular_books.get_popular_books_rank_file()
    popular_books.quit()
     



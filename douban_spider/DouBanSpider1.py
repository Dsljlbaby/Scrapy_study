# -*- encoding:utf-8 -*-

import re
import urllib2
from bs4 import BeautifulSoup
class DoubanSpider_1:
    def __init__(self):
        self.url = "http://movie.douban.com/chart"
        self.request = urllib2.Request(self.url)
        self.reponse = urllib2.urlopen(self.request)
        self.douban_page = self.reponse.read().decode("utf-8")
        print '''
                  author:  Dsljlbaby
                  time:    2016-01-08
                  target:  douban grab
                  about:   BeautifulSoup and re's study
              '''
    def getNewMovies(self,pattern):
        douban_list = re.findall(pattern,self.douban_page)
        return douban_list
    def getWeekMovie(self):
        soup = BeautifulSoup(self.douban_page,"lxml")
        NAranking1 = soup.find('div',id="ranking").find('ul',id="listCont1")
        print "\n--------北美票房榜--------"
        print NAranking1.find('li').get_text()
        num1 = 1
        money = NAranking1.find_all('span')
        for item in NAranking1.find_all('a'):
            print 'Top %d' % num1
            print u'影片名:%s' % item.get_text().strip()
            print u'票房销量:%s' % money[num1].get_text()
            num1 += 1
    def getBeiMovies(self):
        soup = BeautifulSoup(self.douban_page,"lxml")
        NAranking2 = soup.find('div',id="ranking").find('ul',id="listCont2")
        time2 = NAranking2.find('li').get_text()
        print "\n--------本周口碑榜--------"
        print time2
        num2 = 1
        for item in NAranking2.find_all('a'):
            print 'Top %d' % num2
            print u'影片名:%s' % item.get_text().strip()
            num2 += 1
def main():
    douban=DoubanSpider_1()
    name = r'<img src=".*?" alt="(.*?)" class=""/>'
    names = douban.getNewMovies(name)
    intro = r'<p class="pl">(.*?)</p>'
    intros = douban.getNewMovies(intro)
    score = r'<span class="rating_nums">(.*?)</span>'
    scores = douban.getNewMovies(score)
    Comment = r'<span class="pl">(.*?)</span>'
    numcomments = douban.getNewMovies(Comment)
    num = 0
    print '\n----豆瓣新片榜单----\n'
    for items in names:
        print u'影片名：'+names[num]
        print u'电影阵容:'+intros[num]
        print u'豆瓣评分：'+scores[num]
        print u'评价人数:'+numcomments[num]
        print '\n'
        num += 1
    douban.getWeekMovie()
    douban.getBeiMovies()
if __name__ == '__main__':
    main()
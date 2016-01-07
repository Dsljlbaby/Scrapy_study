# -*- encoding:utf-8 -*-

import re
import urllib2

class DoubanSpider_1:
    def __init__(self):
        print 'DouBanSpider Start!'
    def getMovies(self,pattern):
        url = "http://movie.douban.com/chart"
        request = urllib2.Request(url)
        reponse = urllib2.urlopen(request)
        douban_page = reponse.read().decode("utf-8")
        douban_list = re.findall(pattern,douban_page)
        return douban_list
def main():
    douban=DoubanSpider_1()
    name = r'<img src=".*?" alt="(.*?)" class=""/>'
    names = douban.getMovies(name)
    intro = r'<p class="pl">(.*?)</p>'
    intros = douban.getMovies(intro)
    score = r'<span class="rating_nums">(.*?)</span>'
    scores = douban.getMovies(score)
    Comment = r'<span class="pl">(.*?)</span>'
    numcomments = douban.getMovies(Comment)
    num = 0
    print '\n豆瓣新片榜单如下\n'
    for items in names:
        print u'影片名：'+names[num]
        print u'电影阵容:'+intros[num]
        print u'豆瓣评分：'+scores[num]
        print u'评价人数:'+numcomments[num]
        print '\n'
        num += 1
if __name__ == '__main__':
    main()
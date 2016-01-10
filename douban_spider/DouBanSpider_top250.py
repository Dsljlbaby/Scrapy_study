#!/usr/bin/env python
# -*- coding:utf-8 -*-


import re
import urllib2
from bs4 import BeautifulSoup

class DouBanSpider_top():
	def __init__(self):
		print '''
        ---------------------------------------
        author:  Dsljlbaby
        time:    2016-01-09
        target:  DouBan_top250
        about:   BeautifulSoup's study
        ---------------------------------------
              '''
		print '\n-------------豆瓣电影TOP250-------------\n'
	def getPage(self,start):
		try:
			url = 'http://movie.douban.com/top250?start=' + str(start)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			my_page = response.read().decode('utf-8')
		except urllib2.URLError, e :
			if hasattr(e, "code"):
				print "The server couldn't fulfill the request."
				print "Error code: %s" % e.code
			elif hasattr(e, "reason"):
				print "We failed to reach a server. Please check your url and read the Reason"
				print "Reason: %s" % e.reason
		return my_page
	def Output(self,my_page):
		soup = BeautifulSoup(my_page,'lxml')
		for tag in soup.find_all('div', class_='item'):
			num = int(tag.em.get_text())
			name = tag.span.get_text()
			scores = tag.find('span', class_="rating_num").get_text()
			comments = tag.find("span", class_="inq").get_text()
			url = str(tag.find('a')).split('"')[1]
			print (u"Top %d\n片名: %s \n评分: %s\n短评: %s\n链接: %s\n" %(num, name,scores,comments,url))
def main():
	my_spider = DouBanSpider_top()
	start_num = 0
	while start_num <= 250:
		page = my_spider.getPage(start_num)
		my_spider.Output(page)
		start_num = start_num +25
	print '爬取结束......'
if __name__ == '__main__':
	main()
# -*- encoding:utf-8 -*-

import urllib2
import re
import time
class DMSpider():
    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
    def getPage(self,num):
        try:
            URL = 'http://share.dmhy.org/topics/view/'+str(num)+'_.html'
            request = urllib2.Request(URL,headers=self.headers)
            response = urllib2.urlopen(request)
            page = response.read().decode('utf-8')
            print u'第%d条' % num
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print "The server couldn't fulfill the request."
                print "Error code: %s" % e.code
                if e.code == 502:     
                    print "Start : %s" % time.ctime()
                    time.sleep(5)
                    print "End : %s" % time.ctime()
            elif hasattr(e, "reason"):
                print "We failed to reach a server. Please check your url and read the Reason"
                print "Reason: %s" % e.reason
        return page
    def find_title(self,cur_page):
        pattern = r'<h3>(.*?)</h3>(.*?)id="a_magnet" href="([^">s]+)&dn'
        items = re.findall(pattern,cur_page,re.S)
        for item in items:
            print u'片名:' + item[0]
            print u'链接:' + item[2]
def main():
    my_spider = DMSpider()
    start_num = 0
    while start_num <= 600000:   # 建议从200000开始，前面的主题已经不存在
        page = my_spider.getPage(start_num)
        my_spider.find_title(page)
        start_num = start_num + 1
if __name__ == '__main__':
    main()
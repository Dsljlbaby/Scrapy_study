# -*- coding:utf-8 -*-

import urllib2
import re

#糗事百科爬虫类
class QSBKSpider:
    def __init__(self):
        '''初始化方法'''
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : self.user_agent }
        #存放阅读内容
        self.stories = []
        #程序是否进行判断标志
        self.enable = False

    def getPage(self,pageIndex):
        '''传入某一页的索引获得页面代码'''
        try:
            url = 'http://www.qiushibaike.com/text/page/' + str(pageIndex)
            request = urllib2.Request(url,headers = self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode

        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接糗事百科失败,失败原因：",e.reason
            if hasattr(e,"code"):
                print u"程序执行失败，失败原因：",e.code
                return None
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败...."
            return None
        #使用complie对象将正则表达式编译并存入一个pattern变量中，这里使用四个正则完成
        pattern = re.compile(r'<h2>(.*?)</h2>.*?' + '<div.*?class="content">(.*?)<!.*?'
                         ''+'<div.*?class="stats".*?class="number">(.*?)</i>.*?'+
                         '<span.*?class="dash".*?class="number">(.*?)</i>.*?',re.S)
        items = re.findall(pattern,pageCode)
        #存储阅读页面内容
        pageStories = []
        #遍历正则表达式匹配的信息
        for item in items:
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR,"\n",item[1])
                pageStories.append([item[0].strip(),text.strip(),item[2].strip(),item[3].strip()])
        return pageStories

    def loadPage(self):
        '''加载并提取页面的内容，加入到列表中'''
        if self.enable == True:
            if len(self.stories) < 2:
                #获取新一页
                pageStories = self.getPageItems(self.pageIndex)
                #将该页的段子存放到全局list中
                if pageStories:
                    self.stories.append(pageStories)
                    #更新阅读页码
                    self.pageIndex += 1

    def getOneStory(self,pageStories,page):
        ''' 获取阅读词条'''
        for story_item in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "Q":
                self.enable = False
                return
            print u"第%d页\n发布人:%s\n点赞数:%s  评论:%s\n内容:\n%s" %(page,story_item[0],
                                                            story_item[2],story_item[3],story_item[1])


    def start(self):
        print u"回车查看糗事百科词条.Q退出"
        self.enable = True
        #加载页面内容
        self.loadPage()
        #记录阅读页面进度
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                #获取阅读当前页面全部内容
                pageStories = self.stories[0]
                #当前阅读页面+1
                nowPage += 1
                #输出阅读内容
                self.getOneStory(pageStories,nowPage)

def main():
    my_spider = QSBKSpider()
    my_spider.start()
if __name__ == '__main__':
    main()
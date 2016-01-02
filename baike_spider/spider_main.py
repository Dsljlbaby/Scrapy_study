# coding:utf8
import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager() #url管理器
        self.downloader = html_downloader.HtmlDownloader() #html下载器
        self.parser = html_parser.HtmlParser() #html解析器
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self,root_url):
        count = 1 #当前爬取url
        
        self.urls.add_new_url(root_url) #添加入口url
        #当有新的url时
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url() #从urls获取行的url
                print 'craw %d : %s'%(count,new_url)
                html_cont = self.downloader.download(new_url) #下载url页面
                new_urls,new_data = self.parser.parse(new_url,html_cont) #解析下载页面
                self.urls.add_new_urls(new_urls) #添加批量url
                self.outputer.collect_data(new_data) #收集新的数据
            
                if count == 100:
                    break
                count += 1
            except Exception as e:
                print 'craw failed--',e
            
        self.outputer.output_html() #输出收集好的数据

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/6687996.htm" #入口url
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

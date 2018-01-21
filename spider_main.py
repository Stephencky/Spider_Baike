# -*- coding: utf-8 -*-
# encoding="utf-8"
import html_downloader
import html_outputer
import html_parser
import html_manager

class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.urls = html_manager.HtmlManager()
        self.outputer = html_outputer.HtmlOutputer()
        self.parser = html_parser.HtmlParser()
    def crawl(self, root_url):
        count = 1
        try:
            self.urls.add_new_url(root_url)
            while self.urls.has_new_url():
                new_url = self.urls.get_new_url()
                print "crawled %d: %s"%(count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                #print new_urls, new_data
                self.outputer.collect_data(new_data)
                self.urls.add_new_urls(new_urls)
                if count > 1000:
                    break
                count += 1
                
            self.outputer.output_html()
        except Exception, e:
            print repr(e)
            print 'crawled failed %s'
            

if __name__ == '__main__':
    
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)
    

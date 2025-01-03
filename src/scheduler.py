from datasave import DataSave
from htmldownloader import HtmlDownloader
from htmlparse import HtmlParse
from urlmanager import URLmanager

class Scheduler:
    def __init__(self,path, root_url, count):
        #inititaling
        self.url_manager = URLmanager()
        self.downloader = HtmlDownloader()
        self.data_save = DataSave(path)
        self.html_parser = HtmlParse()
        self.root_url = root_url
        self.count = 1 #staring from 1
        self.max_count = count #scrapy max count

    def run_spider(self):
        #Adding root url to url manager, otherwise it will be None
        self.url_manager.save_new_url(self.root_url)
        print(self.count)
        while self.url_manager.get_new_url_num() and self.count <= self.max_count:
            try:
                print('start!!!')
                url = self.url_manager.get_new_url()

                response = self.downloader.download(url)
                new_urls, data = self.html_parser.parse_data(url, response)

                self.url_manager.save_new_urls(new_urls)

                self.data_save.save(data)
                print('Already scrap {0} articles'.format(len(self.url_manager.old_urls)))
                self.count += 1
                print(self.count)
            except Exception as e:
                print('Stopping at {0}th articles'.format(e))
                break


if __name__ == '__main__':
    root_url = 'https://www.cnbeta.com.tw/articles/science/1468030.htm'
    save_path = '/Users/user000_1/Desktop/Github/cnBeta scrapy/cnbeta.txt'
    spider = Scheduler(save_path,root_url,5)
    spider.run_spider()

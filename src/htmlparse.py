from bs4 import BeautifulSoup
from datasave import DataSave
import re
import requests

class HtmlParse:
    def parse_data(self, page_url, data):
        #Return None if the url is not valid
        if page_url is None or data is None:
            return None
        #Bs4 to parse html
        soup = BeautifulSoup(data,'lxml') 

        urls = self.get_urls(soup) #get url
        data = self.get_data(page_url,soup) #get text content

        return urls, data
    
    def get_urls(self, soup):
        #Get all urls in the page, and list() will keep distinct urls
        urls = list()

        #using selector to find all urls under Science tag
        links = soup.select('a[href*="/science"]')
        for link in links:
            url = link['href']
            urls.append(url) #add url to list

        return urls
    
    def get_data(self, page_url, soup):
        data = {}
        data['url'] = page_url
        #title
        title = soup.select_one('.cnbeta-article > header > h1') 
        #release_date
        release_date = soup.select_one('.cnbeta-article > header > .meta > span')

        #saving data to dict
        data['title'] = title.get_text()
        data['release_date'] = release_date.get_text()

        print('article url:{0}'.format(page_url))
        print('data: {0}'.format(data))

        return data
    
if __name__ == '__main__':
    url = 'https://www.cnbeta.com.tw/articles/science/1468030.htm'
    save = DataSave('/Users/user000_1/Desktop/Github/cnBeta scrapy/cnbeta.txt')
    response = requests.get(url)
    response.encoding = 'utf-8'
    parse = HtmlParse()
    u, d = parse.parse_data(url, response.text)
    save.save(d)
    print(u,d)

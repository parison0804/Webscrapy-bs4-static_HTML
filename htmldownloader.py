import requests

class HtmlDownloader:

    def download(self, url):

        if url is None:
            return None
        
        print('Start downloading, url{0}'.format(url))
        response = requests.get(url)

        #start download when 200
        if response.status_code == 200:
            print('Downloaded successfully')

            response.encoding = 'utf-8'
            return response.text
        return None
    
if __name__ == "__main__":
    url = 'http://www.bing.com'
    d = HtmlDownloader()
    bing_html = d.download(url)
    print(bing_html)
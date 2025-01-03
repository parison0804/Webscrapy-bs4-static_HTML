class URLmanager(object):
    def __init__(self):

        self.new_urls = set()
        self.old_urls = set()

    def save_new_url(self, url):
        #saving single URL to waite list
        if url is not None:
            if url not in self.new_urls and url not in self.old_urls:
                print('Saving new URL:{}'.format(url))
                self.new_urls.add(url)

    def save_new_urls(self, url_list):
        #saving list of URLs to waite list
        for url in url_list:
            self.save_new_url(url)

    def get_new_url(self):
        if self.get_new_url_num() > 0:
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None
    
    def get_new_url_num(self):
        #return # of unscrap url
        return len(self.new_urls)
    
    def get_old_url_num(self):
        #return processed url
        return len(self.old_urls)

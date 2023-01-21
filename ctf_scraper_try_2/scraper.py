import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

class Page:
    def __init__(self,url,type):
        self.url = url
        self.real = False
        self.stCode = 0
        self.type = type
        self.title = ""
        self.raw = ""
        self.body = ""
        


class Crawler:

    def __init__(self, urls=[]):
        self.visited_pages = []
        self.pages_to_visit = []
        for url in urls:
            self.pages_to_visit.append(Page(url,"html"))

    def download_url(self, page):
        resp = requests.get(page.url)
        page.stCode = resp.status_code
        

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            
            yield Page(path,"html")
        

    def add_url_to_visit(self, url):
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    def crawl(self, url):
        html = self.download_url(url)
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)

    def run(self):
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.visited_urls.append(url)

if __name__ == '__main__':
    Crawler(urls=['https://www.imdb.com/']).run()
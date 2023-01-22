import logging
import urllib.parse
import requests
from bs4 import BeautifulSoup
import os
domain = "ea1bbd87be43bc2df877415c773072ee.ctf.hacker101.com"

output = "# Recon Report: "+domain+"\n\n\n## Notes\n\n\n## Paths\n\n\n"
logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)


class Page:
    def __init__(self, url, type):
        self.path = url
        self.real = False
        self.stCode = 0
        self.type = type
        self.title = ""
        self.headers = ""
        self.body = ""


class Crawler:

    def __init__(self, urls=[]):
        self.visited_pages = []
        self.pages_to_visit = []
        self.visited_urls = []
        self.urls_to_visit = []

        for url in urls:
            self.pages_to_visit.append(Page(url, "html"))

    def download_pages(self, page):
        resp = requests.get("https://"+domain+page.path,allow_redirects=False)
        page.stCode = resp.status_code
        page.body = resp.text
        page.headers = resp.headers
        if (resp.status_code != 404):
            page.real = True
        

    def get_linked_pages(self, page, html):
        
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if (not path or path[:4] == "http"):
                continue;
            if (not path.startswith("/")):
               inter = "/"
               if(os.path.dirname(page.path) == "/"):
                   inter = ""
               path = os.path.dirname(page.path)+inter+path
            #else:
                #path = "/"+path
            path = os.path.normpath(path)

            yield Page(path, "html")

    def add_page_to_visit(self, page):
        if page.path not in self.visited_urls and page.path not in self.urls_to_visit:
            self.pages_to_visit.append(page)
            self.urls_to_visit.append(page.path)

    def crawl(self, page):
        self.download_pages(page)
        if (page.stCode == 200):
            for pageI in self.get_linked_pages(page, page.body):
                self.add_page_to_visit(pageI)
        elif(int(str(page.stCode)[0]) == 3 and page.headers['Location']):
            self.add_page_to_visit(Page(urllib.parse.urlparse(page.headers['Location']).path,"html"))          

    def run(self):
        while self.pages_to_visit:
            page = self.pages_to_visit.pop(0)
            logging.info(f'Crawling: {page.path}')
            try:
                self.crawl(page)
            except Exception:
                logging.exception(f'Failed to crawl: {page.path}')
            finally:
                self.visited_pages.append(page)
                self.visited_urls.append(page.path)



if __name__ == '__main__':
    site = Crawler(urls=['/'])
    site.run()
    filtered = []
    for page in site.visited_pages:
        dup = False
        for page2 in filtered:
           
            if(page.body == page2.body):
                dup = True

            
        if(not dup and page.real):
            filtered.append(page)

    for page in filtered:
        
        output+= "\n\n### "+page.path+"\n\n"
        output += "<details>\n<summary>Headers</summary>\n```html\n"+"\n".join(page.headers)+"\n```\n</details>\n"

        output += "<details>\n<summary>Response</summary>\n```html\n"+page.body+"\n```\n</details>\n"
        output += "<details>\n<summary>Rendered</summary>\n\n"+page.body+"\n</details>"

output += "\n\n\n## Flag\n"
with open("output/recon.md","w") as f:
    f.write(output)
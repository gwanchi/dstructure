import re
import requests
from bs4 import BeautifulSoup

def in_stock(title, topic):
    homepage = requests.get("http://books.toscrape.com")
    soup = BeautifulSoup(homepage.text, 'html.parser')
    links = soup.find_all("a", href=True)
    for link in links:
        if link.text.strip().lower() == topic.lower():
            href = "http://books.toscrape.com/%s" % link['href']
            page = 1
            href = href.replace("index.html", "page-%s.html" % page) if requests.get(href.replace("index.html", "page-%s.html" % page)).status_code == 200 else href
            while (requests.get(href).status_code == 200):
                topicpage = requests.get(href)
                topicsoup = BeautifulSoup(topicpage.text, 'html.parser')
                ptitles = topicsoup.find_all("a", href=True)
                for ptitle in ptitles:
                    if ptitle.get("title") and ptitle.get("title").strip().lower() == title.lower():
                        return True
                if "index.html" in href:
                    break
                href = href.replace("page-%s.html" % page, "page-%s.html" % str(page + 1))
                page += 1
            break
    return False

print(in_stock("While You Were Mine", "Historical Fiction"))
print(in_stock("Online Marketing for Busy Authors: A Step-By-Step guide", "Self help"))
import sys
import requests
from bs4 import BeautifulSoup

class  roads_to_philosophy:
    def __init__(self):
        self.wikiTitles = []

    def get_wiki_title(self, title):
        URL = "https://en.wikipedia.org{title}".format(title=title)

        try:
            requestWiki = requests.get(url=URL)
            requestWiki.raise_for_status()
        except requests.HTTPError as error:
            if requestWiki.status_code == 404:
                return print("It's a dead end !")
            return print(error)

        soup = BeautifulSoup(requestWiki.text, "html.parser")
        newTitle = soup.find('h1').text
        print(newTitle)
        if newTitle == 'Philosophy':
            return print("{number} roads from {title} to Philosophy".format(number=len(self.wikiTitles), title=self.wikiTitles[0] if len(self.wikiTitles) > 0 else 'Philosophy'))
        if newTitle in self.wikiTitles:
            return print("It leads to an infinite loop !")
        self.wikiTitles.append(newTitle)

        content = soup.find(id="mw-content-text")
        links = content.find_all('a')
        hrefs = [link.get('href') for link in links if link.find_parent('p')
            and not link.find_parent(class_="hatnote navigation-not-searchable")
            and not link.find_parent('table') ]
        filteredHrefs = [href for href in hrefs if href and href.startswith('/wiki/')
            and ':' not in href
            ]
        return self.get_wiki_title(filteredHrefs[0])

def main():
    if len(sys.argv) != 2:
        print("Need one argument")
        return
    test = roads_to_philosophy()
    test.get_wiki_title('/wiki/' + sys.argv[1])

if __name__ == '__main__':
    main()

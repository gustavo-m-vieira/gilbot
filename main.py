from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import json

wikipediaSearchUrl = "https://pt.wikipedia.org/w/rest.php/v1/search/title?q={}&limit=1"
wikipediaPageUrl = "https://pt.wikipedia.org/wiki/{}"

def filterKey(page):
  return page["key"]


def getPageKey(topic):
  topic = quote_plus(topic)
  print(topic)

  pageTxt = urlopen(wikipediaSearchUrl.format(topic)).read().decode('utf-8')
  pages = json.loads(pageTxt)["pages"]

  return list(map(filterKey, pages))[0]

def getPageHtml(key):
  html = urlopen(wikipediaPageUrl.format(key))
  return BeautifulSoup(html, 'html.parser')

def getFirstParagraph(bs):
  div = bs.find('div', id="mw-content-text").div
  return div.p.text

def main(topic):
  key = getPageKey(topic)
  bs = getPageHtml(key)
  firstParagraph = getFirstParagraph(bs)

  print(firstParagraph)

main('one direction')





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

  pageTxt = urlopen(wikipediaSearchUrl.format(topic)).read().decode('utf-8')
  pages = json.loads(pageTxt)["pages"]

  pagesList = list(map(filterKey, pages))

  if (len(pagesList) != 0):
    return pagesList[0]

  raise Exception('Not found topic "{}"'.format(topic))

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

main('minecraft')





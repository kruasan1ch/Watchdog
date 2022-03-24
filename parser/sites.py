from parser.parsable import Parsable
from bs4 import BeautifulSoup
from core.enums import *
import requests


def get_results(chapters, site):
    result = []
    startIndex = 0
    if site is PageTypes.Mangakakalot:
        startIndex = 1
    for index in range(startIndex, len(chapters)):
        result.append(list(filter(None, chapters[index].text.split('\n'))))
    return result


class Mangakakalot(Parsable):

    def __init__(self, link):
        self.link = link

    def get_soup(self):
        page = requests.get(self.link)
        soup = BeautifulSoup(page.text, "html.parser")
        return soup

    def parse(self):
        chapters = self.get_soup().findAll('div', class_='row')
        return get_results(chapters, PageTypes.Mangakakalot)

    def get_name(self):
        return self.get_soup().find('ul', class_='manga-info-text').find('h1').text


class Readmanganato(Parsable):

    def __init__(self, link):
        self.link = link

    def get_soup(self):
        page = requests.get(self.link)
        soup = BeautifulSoup(page.text, "html.parser")
        return soup

    def parse(self):
        chapters = self.get_soup().findAll('li', class_='a-h')
        return get_results(chapters, PageTypes.Readmanganato)

    def get_name(self):
        return self.get_soup().find('div', class_='story-info-right').find('h1').text

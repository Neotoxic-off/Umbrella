import requests
from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self):
        self.soup = None

    def scrap(self, html, fields: list[str]):
        self.soup = BeautifulSoup(html, "html.parser")

        return (self.soup.find_all(fields))


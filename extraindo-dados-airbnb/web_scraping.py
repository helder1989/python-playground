
# classe que tem o objetivo de extrair os dados da página web deixando em um dicionário pra nós

from bs4 import BeautifulSoup
import requests


class WebScraping:
    def __init__(self): # vai permite que instancie os objetos a partir da class
        self.url = url
        self.soup = self.get_html()

    def get_html(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, "html.parser")
        return soup

    def get_rooms(self):
        return self.soup.find_all("div", class_ = "_lunac3l") # informando qual tag queremos buscar

